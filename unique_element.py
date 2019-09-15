a = [10, 20,10 ,30 ,40 ,40]

def norma_uniq(a):
    sea_list = a.copy()
    for j in a:   
        sea_list.remove(j)    
        if j not in sea_list:
            print (j)
    
     
def set_uniq(lists):
    set_list = set(lists)
    list_res = list(set_list)
    for i in list_res:
        print (i)

set_uniq(a)        