# src: https://www.acmicpc.net/problem/1157
string = input().lower()
A=[0]*26
for c in string:
    A[ord(c)-97]+=1
M=max(A)
if A.count(M)>1:
    print("?")
else:
    print(chr(A.index(M)+65))