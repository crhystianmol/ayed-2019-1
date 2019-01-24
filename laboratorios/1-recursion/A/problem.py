from sys import stdin
def partition(x,low,high): 
    i = ( low-1 )        
    pivot = int(x[high])    
  
    for j in range(low , high):
     
        if   int(x[j]) <= pivot:              
            i = i+1 
            x[i],x[j] = x[j],x[i]   
    x[i+1],x[high] = x[high],x[i+1] 
    return i+1  


def quickSort(x,low,high): 
    if low < high:         
        pi = partition(x,low,high) 
  
       
        quickSort(x, low, pi-1) 
        quickSort(x, pi+1, high)
x=stdin.readline().strip().split()
quickSort(x,0,len(x)-1) 
print("Resultado:",int(x[-1])*int(x[-2]))
