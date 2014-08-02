#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shantam
#
# Created:     11/04/2014
# Copyright:   (c) Shantam 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class eve:
    def __init__(self,firstguess, firstboard,secondguess,secondboard):
        self.firstguess = firstguess
        self.firstboard = firstboard
        self.secondguess = secondguess
        self.secondboard = secondboard

filename = 'A-small-attempt2.in' #ENTER FILENAME HERE

def ParseInput(file):
#this parsese the input and returns an array of events

    events = [[]]

    file.readline()
    p=0
    i=0
    for lines in file:
        if p == 10:
            p = 0
            i = i +1

        if p == 0 and not(i==0):
            events.append([lines])
            if i == 0:
                 events[i].append(lines)
        else:
            events[i].append(lines)

        p = p+1

    print(events)
    return events

def RidN(events):
    i = 0
    j = 0
    for ar in events:
        j = 0
        for string in ar:
            if(string.find('\n')):
                d = len(events[i][j])
                events[i][j] = events[i][j][:d-1]
            j = j+1
        i = i+1
    return events

def BuildEvents(events):
    arr = []
    for a in events:
        fb  = []
        i = 1
        while i <= 4:
            fb.append(list(map(int, a[i].split(' '))))
            i = i+1
        sb = []
        i = 6
        while i <= 9:
            sb.append(list(map(int, a[i].split(' '))))
            i = i+1

        k = eve(int(a[0]),fb,int(a[5]),sb)
        arr.append(k) #CHECK HERE FOR PROBS< THE OBS MAY NOT BE CREATED CORR
    return arr

def Resolve(arr):
    case = 1
    f = open("ans.txt","w")
    for even in arr:
        possnums = even.firstboard[even.firstguess-1]
        print(even.firstguess-1)
        truenums = even.secondboard[even.secondguess-1]
        print(even.secondguess-1)
        num = 0
        ans = 0
        for i in possnums:
            stuff =(i in truenums)
            if stuff == True:
                ans = i
            num = num + stuff
        #print(num)

        if num ==1:
            f.write("Case #" + str(case)+ ": " + str(ans)+'\n')
        elif num == 0:
            f.write("Case #" + str(case)+ ": Volunteer cheated!\n")
        else:
            f.write("Case #" + str(case)+ ": Bad magician!\n")
        case = case +1

def main():
    inpfile = open(filename)
    events = RidN(ParseInput(inpfile))
    arr = BuildEvents(events)
    #print(events)
    Resolve(arr)
    #print(arr)

if __name__ == '__main__':
    main()
