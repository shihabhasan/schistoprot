import os, sys, subprocess
import hashlib, time
sys.path.append('/home/shihab/schistoprot/app')
from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext

from app.tasks import run_surface, run_secretory



def index(request):
    return render_to_response('index.html')

def home(request):
    return render_to_response('index.html')

def manual(request):
    return render_to_response('help.html')

def contact(request):
    return render_to_response('contact.html', context_instance=RequestContext(request))

def thanks(request):
    name=request.POST['name']
    email=request.POST['email']
    message=request.POST['message']
    command = "echo 'Name: '"+name+"'\nEmail: '"+email+"'\nMessage: '"+message+" | mutt -s 'SchistoProt Prediction Query' -- pharm.shihab@gmail.com"
    subprocess.call(command, shell=(sys.platform!="Linux"))
    return render_to_response('thanks.html', { 'name': name })

#-----------SURFACE PREDICTION-----------------------------

def surface_app(request):
    return render_to_response('surface.html', context_instance=RequestContext(request))
	
def surface(request):
    if request.POST['surface_sequences'].replace(" ","") == "" and request.POST['surface_file'].replace(" ","") == "":
        message="Enter either fasta sequences in text area or upload fasta file!!!"
        return render_to_response('surface.html', { 'message': message }, context_instance=RequestContext(request))

    feature_mode = request.POST.getlist('featureMode')
    if len(feature_mode) > 0:
        feature_mode = 'moreConservative'
    else:
        feature_mode='lessConservative'

    surface_email=request.POST['surface_email'].replace(" ","")
    if request.POST['surface_sequences'].replace(" ","")!="":
        filename="test_"+hashlib.md5(time.asctime()).hexdigest()
        file_in=open(filename, 'w')
        file_in.write(request.POST['surface_sequences'].replace(" >",">"))
        file_in.close()
    else:
        file = request.FILES['surface_file']
        filename = file.name+"_"+hashlib.md5(time.asctime()).hexdigest()
        destination=open(filename,'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
    task=run_surface.delay(filename, surface_email, feature_mode)
    task_id=task.id
    return HttpResponseRedirect('/surface_progress/'+task_id, { 'task_id': task_id })

def surface_progress(request, task_id):
   result = run_surface.AsyncResult(task_id)
   while not  result.ready():
      return render_to_response('surface_progress.html', { 'task_id': task_id })
   return HttpResponseRedirect('/surface_results/'+task_id, { 'task_id': task_id })
   
def surface_results(request, task_id):
    result = run_surface.AsyncResult(task_id)
    result_data=result.get()
    prediction_lines, header, lines, x1, x2, x3, fh, fd, feature_mode, json_ids, feature_cutoff = result_data
    return render_to_response('surface_result.html', { 'surface_result': prediction_lines, 'header':header, 'all_predictions': lines, 'x1': x1, 'x2': x2, 'x3': x3, 'fh':fh, 'fd':fd, 'feature_mode': feature_mode, 'json_ids': json_ids, 'feature_cutoff': feature_cutoff })


#-----------SECRETORY PREDICTION-----------------------------

def secretory_app(request):
   return render_to_response('secretory.html', context_instance=RequestContext(request))

def secretory(request):
    if request.POST['secretory_sequences'].replace(" ", "") == "" and request.POST['secretory_file'].replace(" ", "") == "":
        message = "Enter either fasta sequences in text area or upload fasta file!!!"
        return render_to_response('secretory.html', {'message': message}, context_instance=RequestContext(request))

    feature_mode = request.POST.getlist('featureMode')
    if len(feature_mode) > 0:
        feature_mode = 'moreConservative'
    else:
        feature_mode = 'lessConservative'
    secretory_email=request.POST['secretory_email'].replace(" ","")

    if request.POST['secretory_sequences'].replace(" ","")!="":
      filename="test_"+hashlib.md5(time.asctime()).hexdigest()
      file_in=open(filename, 'w')
      file_in.write(request.POST['secretory_sequences'].replace(" >",">"))
      file_in.close()
    else:
      file = request.FILES['secretory_file']
      filename = file.name+"_"+hashlib.md5(time.asctime()).hexdigest()
      destination=open(filename,'wb+')
      for chunk in file.chunks():
         destination.write(chunk)
    task=run_secretory.delay(filename, secretory_email, feature_mode)
    task_id=task.id
    return HttpResponseRedirect('/secretory_progress/'+task_id, { 'task_id': task_id })

def secretory_progress(request, task_id):
    result = run_secretory.AsyncResult(task_id)
    while not  result.ready():
        return render_to_response('secretory_progress.html', { 'task_id': task_id })
    return HttpResponseRedirect('/secretory_results/'+task_id, { 'task_id': task_id })
   
def secretory_results(request, task_id):
    result = run_secretory.AsyncResult(task_id)
    result_data=result.get()
    prediction_lines, header, lines, x1, x2, x3, fh, fd, feature_mode, json_ids, feature_cutoff = result_data
    return render_to_response('secretory_result.html', { 'secretory_result': prediction_lines, 'header':header, 'all_predictions': lines, 'x1': x1, 'x2': x2, 'x3': x3, 'fh':fh, 'fd':fd, 'feature_mode': feature_mode, 'json_ids': json_ids, 'feature_cutoff': feature_cutoff })


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


















