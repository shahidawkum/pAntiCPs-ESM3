from numpy.core.fromnumeric import shape
import pandas as pd
import random
from sklearn.model_selection import KFold
import math
from scipy import interp
from sklearn.metrics import roc_curve,auc
import os
import matplotlib.pyplot as plt
from pylab import *
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, matthews_corrcoef
from sklearn.ensemble import RandomForestClassifier as RF

def load_data():
    data1 = pd.read_csv('F:\DeepAIPs-Pred\Feature Extraction\ProtBert_BFD\ProtBert_BFD_Features-training.csv.csv',header=None)
    data2 = pd.read_csv('F:\DeepAIPs-Pred\Feature Extraction\LBP_SMR\LBP_SMR_Features-training.csv',header=None)
    data3 = pd.read_csv('F:\DeepAIPs-Pred\Feature Extraction\PSSM_LBP\LBP_PSSM_Features-training.csv',header=None)
    data4 = pd.read_csv('F:\DeepAIPs-Pred\Feature Extraction\QLC\QLC_Features-training.csv',header=None)
    labels = data1.iloc[:,1240:].values
    labels = labels.ravel()
    features1 = data1.iloc[:,0:1240].values
    features2 = data2.iloc[:,0:256].values
    features3 = data3.iloc[:,0:256].values
    features4 = data4.iloc[:,0:147].values
    
    return features1, features2, features3, features4, labels


features1, features2, features3, features4, labels = load_data()

def fit_fun(X): 
    combined_features = np.concatenate((X[0]*features1,X[1]*features2,X[2]*features3,X[3]*features4), axis=1)
    def classfier():
        kf = KFold(n_splits=5, shuffle=True)
        index = kf.split(X=combined_features ,y=labels)
        dur = []
        acc1 = []
        precision1 = []
        npv1 = []
        sensitivity1 = []
        specificity1 = []
        mcc1 = []
        aucs=[]
        total_error_rate = 0
        allMCC = []
        totMCC = 0
        mean_fpr=np.linspace(0,1,100)
        
        for train_index, test_index in index:
            X_train, X_test = combined_features[train_index], combined_features[test_index]
            y_train, y_test = labels[train_index], labels[test_index]
        
            ## Please write the code for your Function here
            
        
            # Calculate error rate (1 minus accuracy)
            # accuracy = accuracy_score(y_test, y_pred)
            # print("accuracy:", accuracy)
            # error_rate = 1 - accuracy
            # total_error_rate += error_rate
            
            # Calculate MCC
            mcc = matthews_corrcoef(y_test, y_pred)
            allMCC.append(mcc)

        meanMCC = np.mean(allMCC)
          # Average error rate across folds (minimize this value)
        # print("mean_error_rate:", total_error_rate / kf.n_splits)
        # return total_error_rate / kf.n_splits
        return meanMCC
    return classfier()



#print(func3([-2,-3]))
################################
NP=50                              
D=4                                 
G=20                                
f=0.5                                
CR=0.5                               
Xs=2                                 
Xx=-2                               
ob = np.zeros(NP)  
ob1 = np.zeros(NP)
##################Initialization##############
X = np.zeros((NP, D)) 
v = np.zeros((NP, D))
u = np.zeros((NP, D));
#X = np.random.randint(Xx, Xs, (NP, D))
X = np.random.uniform(Xx, Xs, (NP, D))

trace = [] 
###################Calculate the individual objective function value of the current group#############
for i in range(NP): 
    print("i:",i)
    ob[i] = fit_fun(X[i, :])
trace.append(np.max(ob))

###################Steps of DE#############
for gen in range(G): 
    print("gen:", gen)
    ############Mutation###########
    for m in range(NP): 
        r1 = np.random.randint(0, NP, 1)
        while r1 == m:
            r1 = np.random.randint(0, NP, 1)

        r2 = np.random.randint(0, NP, 1)
        while (r2 == m) or (r2 == r1):
            r2 = np.random.randint(0, NP, 1)
        r3 = np.random.randint(0, NP, 1)
        while (r3 == m) or (r3 == r2) or (r3 == r1):
            r3 = np.random.randint(0, NP, 1)
#        v[m, :] = np.floor(X[r1, :] + f * (X[r2, :] - X[r3, :])) 
        v[m, :] = X[r1, :] + f * (X[r2, :] - X[r3, :]) 


     ######Crossover######
    r = np.random.randint(0, D, 1)  
    for n in range(D):  
        cr = np.random.random() 
        if (cr < CR) or (n == r): 
            u[:, n] = v[:, n] 
        else:
            u[:, n] = X[:, n] 


    for m in range(NP): 
        for n in range(D): 
            if (u[m, n] < Xx) or (u[m, n] > Xs):  
                u[m, n] = np.random.randint(Xx, Xs) 
    #####Selection####
    for m in range(NP): 
        print("m1:",m)
        ob1[m] = fit_fun(u[m, :]) 
    for m in range(NP):  
        if ob1[m] > ob[m]: 
            X[m, :] = u[m, :]  
    for m in range(NP):
        print("m2:",m)
        ob[m] = fit_fun(X[m, :]) 

    trace.append(max(ob)) 

index = np.argmax(ob) 
print('Optimized Solution:\n', X[index, :])
print('The optimal value:\n', fit_fun(X[index, :]))
plt.plot(trace)
plt.title('iteration curve')
plt.show()

feature_names = ["ProtBERT", "LBP_SMR", "LBP_PSSM", "QLC"]
optimezed_solution = pd.DataFrame([X[index, :]], columns=feature_names)
optimezed_solution.to_csv("optimezedSolutionDE.csv", index=False)
