import json
import numpy as np
import csv
from collections import OrderedDict
from collections import Counter
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


def read_file(path):
    file = open(path, "r")
    data = file.read()
    data = json.loads(data)
    siteName = data["SiteName"]
    tag = data["Tag"]
    cache = data["Cache_Probe"]
    return [[siteName,tag],cache]

def seperateCache(alldata, seconds):
    dataprocessed = []
    chunk = 500*seconds
    start=0
    end = chunk
    for data in alldata:
        while len(data[1]) != 0:
            if chunk < len(data[1]):
                temp = data[1][start:end]
                data[1] = data[1][chunk:]
                dataprocessed.append([data[0],temp])
                start = start+chunk
                end=end+chunk
            else:
                break
        chunk = 500 * seconds
        start=0
    return dataprocessed

def toCsv(data,name):
    with open(name+".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def histogram(lst):
    res = [(el, lst.count(el)) for el in lst]
    return list(OrderedDict(res).items())

def prepareCsvFiles():
    jsonsData = []
    alldata = []
    cachedata = []
    data1 = read_file("data/chromeBrowsingVNew1.txt")
    data2 = read_file("data/chromeBrowsingVNew2.txt")
    data3 = read_file("data/chromeBrowsingVNew3.txt")
    data4 = read_file("data/ftps-download.txt")
    data5 = read_file("data/ftps-upload.txt")
    data6 = read_file("data/youtubeStream1.txt")
    data7 = read_file("data/youtubeStream2.txt")
    data8 = read_file("data/chat-icq1.txt")
    data9 = read_file("data/chat-icq2.txt")
    data10 = read_file("data/voipskype1.txt")
    data11 = read_file("data/voipskype2.txt")

    alldata.append(data1)
    alldata.append(data2)
    alldata.append(data3)
    alldata.append(data4)
    alldata.append(data5)
    alldata.append(data6)
    alldata.append(data7)
    alldata.append(data8)
    alldata.append(data9)
    alldata.append(data10)
    alldata.append(data11)

    # d=[]
    # for l in alldata:
    #     d.extend(l[1])
    # hst=histogram(np.random.choice(d,75000).tolist() )
    # print(hst)
    # exit(0)

    ffff=0
    alldataprocessed = seperateCache(alldata,15)
    for i in range (0,len(alldataprocessed)):
        with open('DataForModel1.txt','a') as f:
            d={"SiteName":alldataprocessed[i][0][0],"Cache_Probe":alldataprocessed[i][1]}
            z=json.dumps(d)+'\n'
            f.write(z)
            ffff=ffff+1
    print(ffff)


def main():
    prepareCsvFiles()


    # neigh = sklearn.ensemble.RandomForestClassifier()

if __name__ == '__main__':
    main()