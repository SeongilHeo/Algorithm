# src: https://www.acmicpc.net/problem/14065
galon=1
L=3.785411784

mile=1
km=1609.344*0.001

fuel=float(input()) # mile/galone
eff=fuel*km/L
print("%.6f"%(100*1/eff))