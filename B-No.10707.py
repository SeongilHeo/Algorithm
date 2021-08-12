# src: https://www.acmicpc.net/problem/10707
X,Yb,Ym,Yp,P=[int(input()) for _ in range(5)]
print(min(X*P,Yb+(P-Ym)*Yp if P>Ym else Yb))