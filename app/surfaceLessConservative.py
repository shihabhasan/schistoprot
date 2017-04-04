from __future__ import absolute_import
from celery import task

import os, sys, subprocess
import time
import sqlite3
import hashlib
from featuresLessConservative import features
from duplicate_seq_remover import duplicate_seq_remover
from Bio import SeqIO
from StringIO import StringIO
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.neighbors import NearestCentroid
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis  
from sklearn.linear_model import RidgeClassifier, SGDClassifier, Perceptron, PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neural_network import MLPClassifier
import json
import numpy as np
from datetime import datetime

from app.models import SurfaceLessConservative

featuresList ="Percentage of alanine, Percentage of cysteine, Percentage of aspartic acid, \
Percentage of glutamic acid, Percentage of phenylalanine, Percentage of glycine, Percentage of histidine, Percentage of isoleucine, \
Percentage of lysine, Percentage of leucine, Percentage of methionine, Percentage of asparagine, Percentage of proline, \
Percentage of glutamine, Percentage of arginine, Percentage of serine, Percentage of threonine, Percentage of valine, \
Percentage of tryptophan, Percentage of tyrosine, Molecular Weight, Aromaticity, Instability Index, Isoelectric Point, \
Grand average of hydropathy (GRAVY), Secondary helix fraction, Secondary turn fraction, Secondary sheet fraction, \
Average Residue Weight, Average carbon sparing, Average nitrogen sparing, Average sulphur sparing, \
Average oxygen sparing, Average hydrogen sparing, Charge, Molar Extinction Coefficient A280, \
Absobance A280, Probability of Expression Inclusion Bodies, DayhoffStat of alanine, DayhoffStat of cysteine, DayhoffStat of aspartic acid, \
DayhoffStat of glutamic acid, DayhoffStat of phenylalanine, DayhoffStat of glycine, DayhoffStat of histidine, DayhoffStat of isoleucine, \
DayhoffStat of lysine, DayhoffStat of leucine, DayhoffStat of methionine, DayhoffStat of asparagine, DayhoffStat of proline, DayhoffStat of glutamine, \
DayhoffStat of arginine, DayhoffStat of serine, DayhoffStat of threonine, DayhoffStat of valine, DayhoffStat of tryptophan, DayhoffStat of tyrosine, \
Percentage of tiny mole, Percentage of small mole, Percentage of aliphatic mole, Percentage of aromatic mole , Percentage of polar mole, \
Percentage of non polar mole, Percentage of charged mole, Percentage of acidic mole, Percentage of basic mole, Percentage of secondary helix, \
Percentage of secondary sheet, Percentage of secondary turns, Percentage of secondary coil, C-mannosylation sites, Proteasomal cleavages (MHC ligands), \
N-linked glycosylation sites, Arginine and lysine propeptide cleavage sites, Binding Regions in Disordered Proteins, \
Mitochondrial targeting peptide (mTP), Secretory pathway signal peptide (SP), Other subcellular location, \
Linear B-cell epitopes, Class I Immunogenicity Score"

idx="Sequence ID, "+featuresList



amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
for a1 in str(amino_acids):
    for a2 in str(amino_acids):
        idx=idx+","+a1+a2



#---------------------SURFACE LESS CONSERVATIVE------------------

def run_surface_less_conservative(filename, surface_email, feature_mode, task_id):
    parameter=""
    test_features=""
    test_para=""
    seqID_list=[]
    result_dict={}
    result_file=open(filename+"_result.csv", 'w')
    result_file.write("Sequence_ID,Gradient Boosting Machine (GBM) Prediction,GBM Decision Score,GBM Probability,\
    Radial Bias Function (RBF) Support Vector Machine (SVM) Prediction,RBF SVM Decision Score,RBF SVM Probability,\
    Linear Support Vector Machine (SVM) Prediction,Linear SVM Decision Score,Linear SVM Probability,\
    Decision Tree Prediction,Decision Tree Decision Score,Decision Tree Probability,\
    Random Forest Prediction,Random Forest Decision Score,Random Forest Probability,\
    AdaBoost Prediction,AdaBoost Decision Score,AdaBoost Probability,\
    Gaussian Naive Bayes Prediction,Gaussian Naive Bayes Decision Score,Gaussian Naive Bayes Probability,\
    Linear Discriminant Analysis Prediction,Linear Discriminant Analysis Decision Score,Linear Discriminant Analysis Probability,\
    Ridge Regression Prediction,Ridge Regression Decision Score,Ridge Regression Probability,\
    Stochastic Gradient Descent Prediction,Stochastic Gradient Descent Decision Score,Stochastic Gradient Descent Probability,\
    Perceptron Prediction,Perceptron Decision Score,Perceptron Probability,\
    Passive Aggressive Prediction,Passive Aggressive Decision Score,Passive Aggressive Probability,\
    BernoulliNB Prediction,BernoulliNB Decision Score,BernoulliNB Probability,\
    MultinomialNB Prediction,MultinomialNB Decision Score,MultinomialNB Probability,\
    Nearest Centroid Prediction,Nearest Centroid Decision Score,Nearest Centroid Probability,\
    Multi-layer Perceptron Prediction,Multi-layer Perceptron Decision Score,Multi-layer Perceptron Probability\n")

    records=SeqIO.parse(filename, "fasta")
    for record in records:
        hash_sequence=hashlib.md5(str(record.seq)).hexdigest()
        data=SurfaceLessConservative.objects.filter(sequence=hash_sequence)
        if len(data)==0:
            run_para=features(record.id, str(record.seq))
            parameter=parameter+run_para+"\n"
            seqID_list.append(record.id)
            test_features=test_features+run_para+"\n"
            test_para=test_para+record.id+","+run_para+"\n"
        else:
            for p in data:
                p.access=p.access+1
                p.time=datetime.now()
                p.save()
                test_features=test_features+p.features+"\n"
                test_para=test_para+record.id+","+p.features+"\n"
                result_dict[str(record.id)]=p.prediction
    records.close()
    
   #---------------------WORKING WITH SCIKIT-LEARN------------
    if parameter!="":
        parameters=StringIO(parameter)
        train_positive_file="surface_positive_less_conservative.csv"
        train_negative_file="surface_negative_less_conservative.csv"
        train_positive=np.genfromtxt(train_positive_file, delimiter=",")[1:,1:]
        train_negative=np.genfromtxt(train_negative_file, delimiter=",")[1:,1:]
        
        train_data=np.concatenate((train_positive,train_negative))
        train_label=np.concatenate((np.ones(len(train_positive)), np.zeros(len(train_negative))))
        test_data=np.genfromtxt(parameters, delimiter=",")
        
        min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
        
        train_data_scaled = min_max_scaler.fit(train_data).transform(train_data)

        test_data_scaled = min_max_scaler.fit(train_data).transform(test_data)
        
        #-------------------------------------------------------------
        duplicate_seq_remover(filename)
        fasta_rec=SeqIO.index(filename+"_nodups", "fasta")
        param=parameter.split("\n")
        #-------------------------------------------------------------
        
        gbm={}
        svm_rbf={}
        svm_linear={}
        decision_tree={}
        random_forest={}
        ada_boost={}
        naive_bayes={}
        lda={}
        ridge_regression={}
        sgd={}
        perceptron={}
        passive_aggressive={}
        bernoulliNB={}
        multinomialNB={}
        nearest_centroid={}
        mlp={}

        names = [gbm, svm_rbf, svm_linear, decision_tree, random_forest, ada_boost, \
                 naive_bayes, lda, ridge_regression, sgd, perceptron, \
                 passive_aggressive, bernoulliNB, multinomialNB, nearest_centroid, mlp]

        k=int(round(np.sqrt(len(train_data)/2.0)))

        classifiers = [
            GradientBoostingClassifier(),
            SVC(kernel='rbf', C=12.0, gamma=2.0, probability=True),
            SVC(kernel="linear", C=100, probability=True),
            DecisionTreeClassifier(max_depth=k),
            RandomForestClassifier(max_depth=k, n_estimators=k, max_features=481),
            AdaBoostClassifier(),
            GaussianNB(),
            LinearDiscriminantAnalysis(),
            RidgeClassifier(),
            SGDClassifier(),
            Perceptron(),
            PassiveAggressiveClassifier(),
            BernoulliNB(),
            MultinomialNB(),
            NearestCentroid(),
            MLPClassifier()]
        
        #-------------------------------------------------------------
        for name, clf in zip(names, classifiers):
            clf.fit(train_data_scaled, train_label)
            test_predicted = clf.predict(test_data_scaled)
            if hasattr(clf, "decision_function"):
                decisions = clf.decision_function(test_data_scaled)
                
            if hasattr(clf, "predict_proba"):
                probabilities = clf.predict_proba(test_data_scaled)

        #-----------------
            i=0
            for pred in test_predicted:
                if hasattr(clf, "decision_function"):
                    decision=str(decisions[i]).replace("[","").replace("]","")
                else:
                    decision='NA'
                if hasattr(clf, "predict_proba"):
                    probability=probabilities[:,1][i]
                else:
                    probability='NA'
                if pred==1.0:
                    pred='Surface Protein'
                if pred==0.0:
                    pred='Non-Surface Protein'

                if probability=='NA':
                    if decision=='NA':
                        name[seqID_list[i]]=pred+","+decision+","+probability
                    else:
                        name[seqID_list[i]]=pred+","+str(round(float(decision),4))+","+probability
                else:
                    if decision=='NA':
                        if probability>0.5:
                            name[seqID_list[i]]=pred+","+decision+","+str(round(probability,4))
                        else:
                            name[seqID_list[i]]=pred+","+decision+","+str(round(1-probability,4))
                    else:
                        if probability>0.5:
                            name[seqID_list[i]]=pred+","+str(round(float(decision),4))+","+str(round(probability,4))
                        else:
                            name[seqID_list[i]]=pred+","+str(round(float(decision),4))+","+str(round(1-probability,4))
                      
                i=i+1
        #-----------------
        j=0
        for seqID in seqID_list:
            result_dict[seqID]=gbm[seqID]+"\t"+svm_rbf[seqID]+"\t"+svm_linear[seqID]+"\t"+decision_tree[seqID]+"\t"+\
                                random_forest[seqID]+"\t"+ada_boost[seqID]+"\t"+naive_bayes[seqID]+"\t"+lda[seqID]+"\t"+\
                                ridge_regression[seqID]+"\t"+sgd[seqID]+"\t"+perceptron[seqID]+"\t"+passive_aggressive[seqID]+"\t"+bernoulliNB[seqID]+"\t"+\
                                multinomialNB[seqID]+"\t"+nearest_centroid[seqID]+"\t"+mlp[seqID]
            p=SurfaceLessConservative(sequence=hashlib.md5(str(fasta_rec[seqID].seq)).hexdigest(), prediction=result_dict[seqID], features=str(param[j]), access=0, time=datetime.now())
            p.save()
            j=j+1

        fasta_rec.close()
        os.remove(filename+"_nodups")

    #--------------------PLOT--------------------------------------

    train_positive_file="surface_positive_less_conservative.csv"
    train_negative_file="surface_negative_less_conservative.csv"
    train_positive=np.genfromtxt(train_positive_file, delimiter=",")[1:,1:]
    train_negative=np.genfromtxt(train_negative_file, delimiter=",")[1:,1:]
    test_feat=StringIO(test_features)
    test_parameters=np.genfromtxt(test_feat, delimiter=",")
    train_data=np.concatenate((train_positive,train_negative))
    
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
    
    train_positive_scaled = min_max_scaler.fit(train_data).transform(train_positive)
    train_negative_scaled = min_max_scaler.fit(train_data).transform(train_negative)
    test_parameters_scaled = min_max_scaler.fit(train_data).transform(test_parameters)

    x1=np.mean(train_positive_scaled, axis=0).tolist()
    x2=np.mean(train_negative_scaled, axis=0).tolist()
    x3={}

    duplicate_seq_remover(filename)
    records=SeqIO.parse(filename+ "_nodups", "fasta")
    if test_parameters_scaled.ndim==1:
        for record in records:
            x3[record.id]=test_parameters_scaled.tolist()
            result_file.write(record.id+","+result_dict[record.id].replace("\t",",")+"\n")
    else:
        j=0
        for record in records:
            x3[record.id]=test_parameters_scaled[j].tolist()
            result_file.write(record.id+","+result_dict[record.id].replace("\t",",")+"\n")
            j=j+1
    result_file.close()
    records.close()


    #--------------------EMAIL SENDING--------------------------------------
    prediction_file=open(filename+"_prediction.csv", 'w')
    prediction_file.write("Sequence_ID,Prediction,Score \n")
    f = open(filename+"_result.csv",'r')
    all_lines=f.readlines()
    header, lines = all_lines[:1], all_lines[1:]
    duplicate_seq_remover(filename)
    fasta_record = SeqIO.index(filename + "_nodups", "fasta")
    for line in lines:
        prediction_count=line.count('Non-Secretory Protein')
        l=line.split(",")
        if prediction_count>8:
            if len(str(fasta_record[l[0]].seq))<20:
                predicted = l[0] + ',Too short sequence,Unable to predict'
            else:
                predicted=l[0]+',Non-Secretory Protein,'+str(16-prediction_count)+" / 16"
        else:
            if len(str(fasta_record[l[0]].seq))<20:
                predicted = l[0] + ',Too short sequence,Unable to predict'
            else:
                predicted=l[0]+',Secretory Protein,'+str(16-prediction_count)+" / 16"
        prediction_file.write(predicted+"\n")
    f.close()
    fasta_record.close()
    os.remove(filename + "_nodups")
    prediction_file.close()
    f1=open(filename+"_features.csv",'w')
    f1.write(idx+"\n"+test_para)
    f1.close()
    ids = []
    for feature in featuresList.split(", "):
        ids.append(feature)
    json_ids = json.dumps(ids)
    feature_cutoff = len(ids)

    if surface_email!="":
        command = "echo 'Your SchistoProt surface protein prediction result is ready for job ID: "+task_id+"\n\n"+\
                "You can view the interactive tables and plots by the link: http://schistoprot.net/surface_results/"+task_id+"\n\n\n"+\
                "Kind regards,\n\nLutz Krause & Shihab Hasan\nComputational Medical Genomics Group, The University of Queensland Diamantina Institute' | mutt -a "+filename+"'_prediction.csv' -a "+filename+"'_result.csv' -a "+filename+"'_features.csv' -s 'SchistoProt Surface Protein Prediction Result for job ID '"+task_id+" -- "+surface_email
        subprocess.call(command, shell=(sys.platform!="Linux"))


    f2 = open(filename+"_features.csv",'r')
    allLines=f2.readlines()
    fh, fd = allLines[:1], allLines[1:] 
    f2.close()
    
    f3=open(filename+"_prediction.csv", 'r')
    prediction_lines=f3.readlines()[1:] 
    f3.close()
    os.remove(filename)
    os.remove(filename+"_prediction.csv")
    os.remove(filename+"_result.csv")
    os.remove(filename+"_features.csv")
    feature_mode = "Less Conservative"
    return (prediction_lines, header, lines, x1, x2, x3, fh, fd, feature_mode, json_ids, feature_cutoff)
