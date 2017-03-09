#from random import randint


import blackjack
from pylab import *

row_action=2
coloum_state=182
Q1 = zeros((coloum_state,row_action)) # NumPy array of correct size
Q2 = zeros((coloum_state,row_action)) # NumPy array of correct size

def learn(alpha, eps, numTrainingEpisodes):
    
    # Fill in Q1 and Q2
    gamma=1

    for i in range(1,181):
        Q1[i][0] =random()* 0.00001
        Q1[i][1] =random()* 0.00001
        
        Q2[i][0] =random()* 0.00001
        Q2[i][1] =random()* 0.00001
    
    
    returnSum=0
    for episodeNum in range(numTrainingEpisodes):
        state=blackjack.init()
        G=0
        R,S = blackjack.sample(state,1)
        if S==False:
            G=G+R
        
        Q=Q1+Q2
        while S!=False:
            if eps > random() :
                A= randint(0,2) #esp bigger then do random action
            else:               #else choose the biggest one in perious

                if Q[S,0]>Q[S,1]:
                    A=0
                else:
                    A=1

   
            RR, nexstate = blackjack.sample(S,A)
            G=G+RR
            pro=randint(0,2)
            if pro==1:
                error = RR+gamma*Q2[nexstate][argmax(Q1[nexstate])]-Q1[S][A]
                Q1[S][A] = Q1[S][A]+alpha*(error)

            else:
                error = RR+gamma*Q1[nexstate][argmax(Q2[nexstate])]-Q2[S][A]
                Q2[S][A] = Q2[S][A]+alpha*(error)
            S=nexstate
    # Fill in Q1 and Q2

        returnSum = returnSum + G
        
        #if episodeNum % 10000 == 0 and episodeNum != 0:
        #    print("Average return so far: ", returnSum/episodeNum)
#    print("Average return so far: ", returnSum/numTrainingEpisodes)
    
#    print(Q1)
#    print(Q2)

def evaluate(numEvaluationEpisodes):
    returnSum = 0.0
    Q=Q1+Q2
    for episodeNum in range(numEvaluationEpisodes):
        G = 0
        R,S = blackjack.sample(0, 1)
        if S==False:
            G = G + R
        
        while S != False:    #if state a!= terminal state
            if Q[S,0]>=Q[S,1]:
                A=0
            else:
                A=1
            R, S = blackjack.sample(S, A)
            G = G + R
                #print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G

    return returnSum/numEvaluationEpisodes


def policy(state):
    Q=Q1+Q2
    if Q[state,0]>Q[state,1]:
        return 0
    else:
        return 1
#part 2
#double-Q learning for test the randompolicy(alpha=0.001,eps=1) for 1000000 episodes.

#learn(0.001, 1, 1000000)
#blackjack.printPolicy(policy)
#value_evaluate=evaluate(1000000)
#print(value_evaluate)


#double-Q learning for test the eps=0.01 and alpha=0.001 for 1000000 episodes.
learn(0.001, 0.01, 1000000)
#blackjack.printPolicy(policy)
value_evaluate=evaluate(1000000)
#blackjack.printPolicyToFile(policy)
#print(value_evaluate)

#part 3


learn(0.001,0.85, 10000000)
#blackjack.printPolicy(policy)
value_evaluate=evaluate(10000000)
#blackjack.printPolicyToFile(policy)
#print(value_evaluate)


















