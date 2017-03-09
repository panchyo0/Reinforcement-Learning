import mountaincar
from Tilecoder import numTilings, numTiles, tilecode
from pylab import *  # includes numpy

numRuns = 1
n = numTiles * 3
numEpisodes=200
gamma=1
stepsArray = zeros(numEpisodes)
returnsArray = zeros(numEpisodes)

def Qs (f,theta1):
    Q=[0,0,0];
    
    for action in range(3):
        for index in f:
            Q[action]=(Q[action]+(theta1[index+action*324]))
    return Q



def learn(alpha=.1/numTilings, epsilon=0, numEpisodes=200):
    theta1 = -0.001*rand(n)
    theta2 = -0.001*rand(n)
    #Q=zeros(3)
    
   
    returnSum = 0.0
    for episodeNum in range(numEpisodes):
        G = 0
        step=0
        S=mountaincar.init()
        tileindec=tilecode(S[0],S[1],[-1] * numTilings)
#        Q=Qs(tileindec,theta1)
#        act=argmax(Q)

#derivate=zeros(n)
        
        while S!=None:
            step+=1
            #derivate=zeros(n)
            #tileindec=tilecode(S[0],S[1],[-1] * numTilings)
            #Q=Qs(tileindec,theta1)
            if random()<epsilon:
                act=randint(0,3)
            else:
                act=argmax(Qs(tileindec,theta1+theta2))

            R,Stemp=mountaincar.sample(S,act)
            
            G+=R
            if Stemp==None:
                pro=randint(0,2)
                if pro==1:

                    q1=Qs(tileindec,theta1)
                    q2=Qs(tileindec,theta2)
                    update=alpha*(R+q2[argmax(q1)]-q1[act])
                for i in tileindec:
                    theta1[i+act*324]+=update
                break

                if pro==0:

                    q1=Qs(tileindec,theta1)
                    q2=Qs(tileindec,theta2)
                    update=alpha*(R+q2[argmax(q1)]-q1[act])
                for i in tileindec:
                    theta2[i+act*324]+=update
                break
            else:
                tileindec_tem=tilecode(Stemp[0],Stemp[1],[-1] * numTilings)
#            for i in tileindec:
#                derivate[i+act*324]=1
                pro=randint(0,2)
                if pro==1:
                    if Stemp!=None:
                        q1=Qs(tileindec_tem,theta1)
                        q2=Qs(tileindec_tem,theta2)
                        update=alpha*(R+q2[argmax(q1)]-q1[act])
                    for i in tileindec:
                        theta1[i+act*324]+=update
            
                else:
                    if Stemp!=None:
                        q1=Qs(tileindec_tem,theta1)
                        q2=Qs(tileindec_tem,theta2)
                        
                        update=alpha*(R+q1[argmax(q2)]-q2[act])
                    for i in tileindec:
                        theta2[i+act*324]+=update
                S=Stemp
                tileindec=tileindec_tem
            
#            for i in tileindec:
#                derivate[i+act*324]=1
#        
#            if Stemp==None:
#                #print(Stemp)
#                for i in range(n):
#                    theta1[i]=theta1[i]+alpha*(R-Q[act])*derivate[i]
#                break;
#            else:
#
#                tileindec_tem=tilecode(Stemp[0],Stemp[1],[-1] * numTilings)
#                Q_tem=Qs(tileindec_tem,theta1)
#                #print(Q_tem)
#                act_tem=argmax(Q_tem)
#
#                for i in range(n):
#                    theta1[i]=theta1[i]+alpha*(R+gamma*(Q_tem[act_tem])-Q[act])*derivate[i]
#                S=Stemp
#                #print(S)

                
#        ...
#        your code goes here (20-30 lines, depending on modularity)
#        ...
        print("Episode: ", episodeNum, "Steps:", step, "Return: ", G)
        returnSum = returnSum + G
    print("Average return:", returnSum / numEpisodes)
    return returnSum, theta1, theta2

learn()

#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data
#def writePerfData():
#    fret = open('avgret.dat', 'w')
#    fstep = open('steps.dat', 'w')
#    for i in range(numEpisodes):
#        fret.write(repr(i) + '	' + repr(returnsArray[i]/numRuns))
#        fstep.write(repr(i) + '	' + repr(stepsArray[i]/numRuns))
#        fret.write('\n')
#        fstep.write('\n')
#    fret.close()
#    fstep.close()
#
#def writeF(theta1, theta2):
#    fout = open('value', 'w')
#    steps = 50
#    for i in range(steps):
#        for j in range(steps):
#            F = tilecode(-1.2 + i * 1.7 / steps, -0.07 + j * 0.14 / steps)
#            height = -max(Qs(F, theta1, theta2))
#            fout.write(repr(height) + ' ')
#        fout.write('\n')
#    fout.close()
#
#
#if __name__ == '__main__':
#    runSum = 0.0
#    for run in range(numRuns):
#        returnSum, theta1, theta2 = learn()
#        runSum += returnSum
#    print("Overall performance: Average sum of return per run:", runSum/numRuns)
