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

filename = 'B-large.in' #ENTER FILENAME HERE

def SecToGetNhouses(numhouse,cookperf,costpf):
    n = 0
    sec = 0
    while not(n==numhouse):
        sec = sec + ((costpf*1.0)/(2+cookperf*n))
        n = n+1
    return sec
def SecToTarget(numhouse,cookpf,target):
    cps = 2.0 + numhouse*cookpf
    return target/cps
def NumFarms(cookpf,target,costpf):
    currfarm = 0
    morefarms = True
    while morefarms:
        currfarmsec = target/(2.0+currfarm*cookpf) #current farm sec to tgt
        newfarmsec = target/(2.0+(currfarm+1)*cookpf)+((costpf*1.0)/(2+cookpf*currfarm))

        if newfarmsec>currfarmsec:
            return currfarm
        currfarm = currfarm +1
def SecToWin(nhouse,cookpf,costpf,target):
    return SecToGetNhouses(nhouse,cookpf,costpf)+SecToTarget(nhouse,cookpf,target)

def ReadInput():
    f = open(filename)
    f.readline()
    inputarr = []
    for lines in f:
        inputarr.append(list(map(float, lines.split(' '))))
    return inputarr
def main():
    f = open("ans.txt","w")
    inp = ReadInput()
    case = 1
    for event in inp:
        cookpf = event[1]
        target = event[2]
        costpf = event[0]
        nf = NumFarms(cookpf,target,costpf)
        sec = SecToWin(nf,cookpf,costpf,target)
        f.write("Case #" + str(case)+ ": " + str(sec)+'\n')
        case = case +1

if __name__ == '__main__':
    main()
