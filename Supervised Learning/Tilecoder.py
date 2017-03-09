numTilings = 8

    
def tilecode(in1, in2, tileIndices):
    # write your tilecoder here (5 lines or so)
    
    for i in range(0,numTilings):

        col = (in1 + i*(0.6/numTilings)) // 0.6
        row = (in2 + i*(0.6/numTilings)) // 0.6
        tile = (i*121) + (11*col) + row
        tileIndices[i] = int(tile)
    return tileIndices
    
    
def printTileCoderIndices(in1, in2):
    tileIndices = [-1] * numTilings
    tilecode(in1, in2, tileIndices)
    print('Tile indices for input (', in1, ',', in2,') are : ', tileIndices)

#printTileCoderIndices(0.1, 0.1)
#printTileCoderIndices(4.0, 2.0)
#printTileCoderIndices(5.99, 5.99)
#printTileCoderIndices(4.0, 2.1)
    
