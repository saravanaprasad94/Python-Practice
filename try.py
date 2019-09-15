n = int(input())
input_l = []
iter_l = []
inp = input().split(" ")
for j in inp:    
    iter_l.append(int(j))  
min_l = min(iter_l)
i = 0
count = 0 
while i < min_l:
    for j in range(len(iter_l)):
        iter_l[j] = iter_l[j] -1
        if iter_l[j] == 0:
            count += 1 
    i += 1
   
 
if count == len (iter_l):
    print ("YES")
else :
    print ("NO")           