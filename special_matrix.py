import math
t = int(input())
inp = 0

while inp < t:
    n = int(input())    
    line_list =[]
    med =math.ceil(n/2)
    step_col = 0
    step_row = 0 
    for j in range(n):
        line_list.append(str(input()))
    for i in range(len(line_list)):
        count = 0        
        for j in line_list[i]:
            count += 1
            if j == '*':       
               print (i+1, count)         
               if ( (i+1) < med) and (count < med):
                   step_row = med - (i+1)
                   step_col = med - count           
               elif ( (i+1) > med) and (count > med):
                   step_row = (i+1) - med
                   step_col = count - med     
               elif (count == med) and ((i+1) < med)  :                   
                   step_col = 0
                   step_row = med - (i+1)
               elif (count == med) and ((i+1) > med)  :  
                   step_col = 0
                   step_row = (i+1) - med  
               elif ((i+1) == med) and (count < med)  :
                   print ("in")
                   step_row = 0
                   step_col = med - count
               elif ((i+1) == med) and (count > med)  :  
                   step_row = 0
                   step_col = count - med 
               elif ((i+1) < med) and (count > med)  :
                   
                   step_row = med- (i+1)
                   step_col = count - med
               elif ((i+1) > med) and (count < med)  :  
                   step_row = (i+1) - med
                   step_col = med - count    
               else:
                   step_col = 0
                   step_row = 0     
             
    print (step_row + step_col)

    inp = inp + 1   

