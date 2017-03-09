#from pylab import *  # includes numpy
numTilings = 4
numTiles=81*4
posoffset=1.7/8
veloffset=0.14/8
    
def tilecode(position, velocity, tileIndices):
    # write your tilecoder here (5 lines or so)
    
    for i in range(0,numTilings):

        posindex = ((position+1.2) + i*(posoffset/numTilings)) // posoffset
        velindex = ((velocity+0.07) + i*(veloffset/numTilings)) // veloffset
        tile = (i*81) + (9*velindex) + posindex
        tileIndices[i] = int(tile)
    return tileIndices
    
    
def printTileCoderIndices(position, velocity):
    tileIndices = [-1] * numTilings
    tilecode(position, velocity, tileIndices)
    print('Tile indices for input (', position, ',', velocity,') are : ', tileIndices)

#def Qs (f):
#    Q=[0,0,0];
#    for action in range(3):
#        for index in f:
#            Q[action]+=theta[index+action*324]
#    return Q
#printTileCoderIndices(-1.2, -0.07)
#f=tilecode(-1.2,-0.07,[-1] * numTilings)
#theta = -0.01*rand(972)
#a=Qs(f)
#b=argmax(a)
#print(a)
#print(b)

#if __name__ == '__main__':
#    printTileCoderIndices(-1.2, -0.07)
#    printTileCoderIndices(-1.2, 0.07)
#    printTileCoderIndices(0.5, -0.07)
#    printTileCoderIndices(0.5, 0.07)
#    printTileCoderIndices(-0.35, 0.0)
#    printTileCoderIndices(0.0, 0.0)
