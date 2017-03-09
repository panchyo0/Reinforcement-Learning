import blackjack
from pylab import *



def run(numEvaluationEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEvaluationEpisodes):
        G = 0
        R,S = blackjack.sample(0,1)
        if S==False:
            G = G + R
    
        else:
            while S != False:    #if state a!= terminal state
                R, S = blackjack.sample(S, randint(0,2))
                G = G + R
        print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
    return returnSum/numEvaluationEpisodes

#value_run=run(2000)
#print(value_run)

