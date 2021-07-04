# src: https://www.acmicpc.net/problem/2941
part=["c=","c-","dz=",'d-','lj','nj',"s=",'z=']
target=list(input())
result=0
i=0
while i<len(target):
    if len(target)>=i+3 and "".join(target[i:i+3]) in part:
        i+=3
        
    elif len(target)>=i+2 and "".join(target[i:i+2]) in part:
        i+=2

    else:
        i+=1
    result+=1

print(result)