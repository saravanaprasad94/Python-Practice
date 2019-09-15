input = [3, 1, 4, 6, 5]

def my_triplet(input):
    squared_list = []
    for i in input:
        squared_list.append(i * i)
    print (squared_list)    
    res_list = []
    for i in range(len(squared_list) -1):   
        for j in range(len(squared_list) -1):
            if (squared_list[i] + squared_list[j+1]) in squared_list:            
                res_list.append(squared_list[i] ** .5)
                res_list.append(squared_list[j+1] ** .5)
                res_list.append((squared_list[i] + squared_list[j+1]) ** .5)
                break
        else:
            continue 
        break   
    print (res_list)            
    
def sort_triplet(input):
    squared_list = []
    for i in input:
        squared_list.append(i * i)
    squared_list.sort()    
    print (squared_list)  
    for i in range(len(input)-1, 1, -1):
        j =0
        k = i-1
        while j < k:
            if squared_list[j]+squared_list[k] == squared_list[i]:
                return (True)
                break
            else:
                if squared_list[j]+squared_list[k] < squared_list[i]:
                    j +=1 
                else:
                    k -= 1
    return (False)                    


# my_triplet(input)
# print (sort_triplet(input))

def isTriplet(ar, n): 
    j = 0
      
    for i in range(n - 2): 
        for k in range(j + 1, n): 
            print (k)
            for j in range(i + 1, n - 1): 
                print (j)
                # Calculate square of array elements 
                x = ar[i]*ar[i] 
                y = ar[j]*ar[j] 
                z = ar[k]*ar[k]  
                if (x == y + z or y == x + z or z == x + y): 
                    return 1

isTriplet(input, len(input))                    