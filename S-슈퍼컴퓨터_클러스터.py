# src: https://softeer.ai/practice/info.do?idx=1&eid=1204&sw_prbl_sbms_sn=143890

import sys
input = sys.stdin.readline
N, B = map(int,input().split())
A=list(map(int, input().split()))
def solve(s,e,B):
    M = (s+e)//2
    if s>e:
        return M
    need = [x-M for x in A if x-M <0]
    if sum(map(lambda x:x**2,need)) <= B:
        return solve(M+1,e,B)
    else:
        return solve(s,M-1,B)
print(int(solve(min(A),B**(1/2)+max(A),B)))
