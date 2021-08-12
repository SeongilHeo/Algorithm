# src: https://www.acmicpc.net/problem/11466
h,w=map(int,input().split())
if h<w:
    h,w=w,h
R=[]
if w*3<=h:
    R.append(w)
if h/3<=w:
    R.append(h/3)
R.append(w/2)
print(max(R))