from sys import stdin
def busqueda (x,low,high,lista):   

    if int(lista[low])== x or int(lista[high])==x :
        if int(lista[low])== x:
            return low
        else:
            return high
    elif low==high and int(lista[low])!= x and int(lista[high])!=x:
        return -1
    else:
        mid = ((high+low)+1)//2
        if int(lista[mid])>=x:           
            
            return busqueda (x,low,mid,lista)
        else:
            
            return busqueda (x,mid,high,lista)
x=int(stdin.readline())
lista=stdin.readline().strip().split()
n=len(lista)-1
print( busqueda (x,0,n,lista))
