 src: https://www.acmicpc.net/problem/1992
N=int(input())
B=[list(input()) for _ in range(N)]
def check(r,c,size):
    if r>N or c>N:
        return
    pivot=B[r][c]
    for j in range(r,r+size):
        for i in range(c,c+size):
            if B[j][i] != pivot:
                return False
    return True

def solve(r,c,size):
    if check(r,c,size):
        return B[r][c]
    else:
        return "(%s%s%s%s)"%(
            solve(r,c,size//2),
            solve(r,c+size//2,size//2),
            solve(r+size//2,c,size//2),
            solve(r+size//2,c+size//2,size//2)
        )
print(solve(0,0,N))