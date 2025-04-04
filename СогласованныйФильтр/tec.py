import random
import numpy as np
import matplotlib.pyplot as plt


def akf(a, b):
    signal=[0]*100+[a]*100
    signal+=signal[::-1]
    data=[0]*1000 + signal +[0]*1000
    data=[elem+random.randint(-b, b)*random.random() for elem in data]
    plt.plot(np.arange(len(data)), data)
    plt.savefig('data'+str(b)+'.png')
    plt.close()
    #plt.show()
    akf=[]
    for i in range(0, len(data)-len(signal)):
        s=0
        for j in range(len(signal)):
            s+=data[i+j]*signal[j]
        akf+=[s]

    plt.plot(np.arange(len(akf)), akf)
    plt.savefig('akf'+str(b)+'.jpg')
    #plt.show()
    plt.close()
    




i=0
for i in range(0, 36, 5):
    akf(2, i)
for i in range(20, 25):
    akf(2, i)