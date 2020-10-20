import sys



def main():

    def IsOk(number,array):
        for i in range(len(array)):
            if (number - array[i] in array ) :
                if number - array[i] == array[i]:
                    return 1
            
                return 0
        return 1

    def dfs(room, number,roomlist):
        # end 
        #print("room#: ", room, " number: ",number)
        #print ("in FUnc roonlist ", room, " is ",roomlist)
        x = IsOk(number,roomlist[room])
        #print("x value :", x);
        if x == 1:
            roomlist[room].append(number)
            #print("insert one at ", room," with #",number)
        
            unvisited[number-1] = 1
            #print("unvisit : ", unvisited)
            return 0
            # triverse all other room
        
        #for i in range(room, len(roomlist)-1):
            #print(" i : ",i)
            #dfs(i+1,number,roomlist)
        if room+1 < len(roomlist):
            dfs(room+1,number,roomlist)       

  

    file_name, arg1, arg2= sys.argv
    mono = int (arg1)
    room = int (arg2)
    #print("mono :", type(mono))
    #print("room :", room)
    
    #mono = 5
    #room = 2
    monolist=[]
    roomlist=[]

    # initial roomlist monopole list
    for x in range(mono):
        monolist.append(x+1)   
    for x in range(room):
        roomlist.append([])
    #print("labels we have: ",monolist)
    unvisited = [0]*mono
    #print("initial roomlist", roomlist)
    for i in range(len(monolist)):
        #print(" monolist index : ", i)
        #print(" mololist[i] = ", monolist[i])
        if unvisited[i]!=1 :
           
            dfs(0,monolist[i],roomlist)
    
    result = 0 ;
    sumall = sum(monolist)
    for i in range(len(roomlist)):
        result=result +sum(roomlist[i])
    #print("sum :", sumall, "result: ", result)
    if sumall!= result :
        print("unsat")
        return 0
    else: 
        print(roomlist)
        return 1
if __name__=="__main__":
    main()

