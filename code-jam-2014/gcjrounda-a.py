#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shantam
#
# Created:     25/04/2014
# Copyright:   (c) Shantam 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
file_name = 'input.in'


class Power:
    def __init__(self,val):
        self.values = []
        d = list(val)
        self.values = map(int,d)
    def invert(self,bitnum):
        self.values[bitnum] = not self.values[bitnum]
    def GetVals(self):
        return self.values
    def Equal(self,pow):
        return self.values == pow.GetVals()


def Test(events):
    case = 1
    for e in events:
        outlets,devices = e

        case +=1


def GetInput(fn):
    f = open(fn)
    cases = int(f.readline())
    i = 0
    events = []
    while not(i ==cases):
        nout,space,numswitches = (f.readline()).partition(" ")
        nout = int(nout)
        numswitches = int(numswitches)
        soutlets = (f.readline()).split(" ")
        sdev = (f.readline()).split(" ")
        outlets = [Power(s) for s in soutlets]
        devices = [Power(s) for s in sdev]

        events.append((outlets,devices))
        i += 1
    return events


def main():
    Test(GetInput(file_name))


if __name__ == '__main__':
    main()
