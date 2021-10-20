from itertools import permutations
def allPer(string):
    permlist=permutations(string)
    for i in permlist:
        k=int("".join(i))
        if k%d==0:
            t.append(k)
    return t
        

if __name__ == "__main__": 
    num,d=map(int,input().split())
    num=str(num)
    t=[]
    num=list(num)
    num.sort()
    least_multiple=-1
    allPer(num)
    t=[int(i) for i in t ]
  
    for i in t:
        if i%d==0:
            least_multiple=i
            break
    print(least_multiple)