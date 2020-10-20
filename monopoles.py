import sys
import numpy
print(sys.argv)

'''
class graph(object):
    def __init__(self,mono,room):
        self.mono = mono
        self.room = room


def arrage(self, monolist,roomlist):
 
    def ISOK(number,room):
        for i in range(len(hall[]))
            if number - room[i] in room:
                return 0
        return 1;

    def dfs(room, number):
        # end 
        if ISOK(numer, hall[room]) == 1:
            hall[room].append(number)
        # triverse all other room
        for i in range(room, len(roomlist)):
            dfs(i+1,number)
           

   #initial answer
    answer = [len(roomlist)];# answer contains a list of list,   
    hall = [len(roomlist)]; 
    
        
    # creating rooms 
    #using inde
    for i in range(len(list)):
        answer[i] = []
        hall[i] = []



    dfs(0,monolist[0])
    return answer;

def main():
    #int mono = argv[1]
    #int room = argv[2]
    mono = 5
    room = 2
    monolist = []
    roomlist = []
    # initial roomlist monopole list
    for x in range(5):
        monolist.append(x+1)   
    for j in range(room):
        roomlist.append(x)
    print("mono: ",monolist,"\n")
    print("room: ",roomlist)

    unvisited = monolist
    visited = []








if __name__=="__main__":
    main()
    



'''
##demo
'''
def IsOk(number,roomlist):
    for i in range(len(roomlist)):
        if number - room[i] in roomlist:
            return 0
    return 1
'''

def IsOk(number,array):
    for i in range(len(array)):
        if (number - array[i] in array ) :
            if number - array[i] == array[i]:
                return 1
           
            return 0
    return 1

def dfs(room, number,roomlist):
    # end 
    print("room#: ", room, " number: ",number)
    print ("in FUnc roonlist ", room, " is ",roomlist)
    x = IsOk(number,roomlist[room])
    print("x value :", x);
    if x == 1:
        roomlist[room].append(number)
        print("insert one at ", room," with #",number)
       
        unvisited[number-1] = 1
        print("unvisit : ", unvisited)
        return 0
        # triverse all other room
    
    #for i in range(room, len(roomlist)-1):
        #print(" i : ",i)
        #dfs(i+1,number,roomlist)
    if room+1 < len(roomlist):
        dfs(room+1,number,roomlist)       


mono = 8

room = 2

monolist=[]
roomlist=[]

# initial roomlist monopole list
for x in range(mono):
    monolist.append(x+1)   
for x in range(room):
    roomlist.append([])
print("labels we have: ",monolist)
unvisited = [0]*mono
print("initial roomlist", roomlist)
for i in range(len(monolist)):
    print(" monolist index : ", i)
    print(" mololist[i] = ", monolist[i])
    if unvisited[i]!=1 :
        print("calling func")
        dfs(0,monolist[i],roomlist)
print(roomlist)
result = 0 ;
sumall = sum(monolist)
for i in range(len(roomlist)):
    result=result +sum(roomlist[i])
print("sum :", sumall, "result: ", result)
if sumall!= result :
    print("EEND GAME")




