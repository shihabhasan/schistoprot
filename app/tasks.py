from __future__ import absolute_import
from celery import task
import sys
sys.path.append('/home/shihab/schistoprot/scripts/moreConservative')
sys.path.append('/home/shihab/schistoprot/scripts/lessConservative')
from .surfaceMoreConservative import run_surface_more_conservative
from .secretoryMoreConservative import run_secretory_more_conservative
from .surfaceLessConservative import run_surface_less_conservative
from .secretoryLessConservative import run_secretory_less_conservative


#---------------------SURFACE BACKGROUND TASK------------------
@task
def run_surface(filename, surface_email, feature_mode):
    task_id = run_surface.request.id
    if feature_mode=="lessConservative":
        result = run_surface_less_conservative(filename, surface_email, feature_mode, task_id)
    if feature_mode=="moreConservative":
        result = run_surface_more_conservative(filename, surface_email, feature_mode, task_id)
    return result


#---------------------SECRETORY BACKGROUND TASK------------------
@task
def run_secretory(filename, secretory_email, feature_mode):
    task_id = run_secretory.request.id
    if feature_mode=="lessConservative":
        result = run_secretory_less_conservative(filename, secretory_email, feature_mode, task_id)
    if feature_mode=="moreConservative":
        result = run_secretory_more_conservative(filename, secretory_email, feature_mode, task_id)
    return result