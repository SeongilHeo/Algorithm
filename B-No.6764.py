# src: https://www.acmicpc.net/problem/6764
L=list(int(input()) for _ in range(4))
if len(set(L))==1:
    print("Fish At Constant Depth")
elif len(set(L))!=4:
    print("No Fish")
elif L==sorted(L):
    print("Fish Rising")
elif L==sorted(L,reverse=True):
    print("Fish Diving")
else:
    print("No Fish")
