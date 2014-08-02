#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shantam
#
# Created:     12/04/2014
# Copyright:   (c) Shantam 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

filename = 'input.in' #ENTER FILENAME HERE

def PlayDecWar(kblocks,nblocks):
    count = len(kblocks)
    kpoints,npoints = 0,0
    while not(count ==0):
        if max(nblocks) < max(kblocks):
            nblocks.remove(min(nblocks))
            kblocks.remove(max(kblocks))
            kpoints = kpoints +1
        else:
            nblocks.remove(max(nblocks))
            kblocks.remove(min(kblocks))
            npoints= npoints +1
        count = count -1
    return kpoints,npoints

def PlayNormWar(kblocks,nblocks):
    kblocks.reverse()
    nblocks.reverse()
    print(kblocks,nblocks)
    kpoints,npoints = 0,0

    for nb in nblocks:
        if(nb>max(kblocks)):
            kblocks.remove(min(kblocks))
            npoints = npoints +1
        else:
            kblocks.remove(max(kblocks))
            kpoints = kpoints + 1

    return kpoints,npoints#CHECK ME IF ERROR

def ReadInput():
    f = open(filename)
    f.readline()
    inputarr = []
    count = 1
    new = True

    for lines in f:

        if count %2 ==1:
            count = count +1
            new = True
            continue
        if new:
            inputarr.append(list(map(float, lines.split(' '))))
        else:
            new = False
            inputarr[len(inputarr)-1].append(list(map(float, lines.split(' '))))
        count = count +1


    return inputarr

def main():
    f = open("ans.txt","w")
    inp = ReadInput()
    print(inp)
    return
    kblocks,nblocks = GetBlocks

    kblocks.sort()
    nblocks.sort()
    kcbl = kblocks.copy()
    knorm,nnorm = PlayNormWar(kblocks,nblocks)
    kdec,ndec = PlayDecWar(kcbl,nblocks)

    print(ndec,nnorm)

if __name__ == '__main__':
    main()
