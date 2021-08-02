# src: https://www.acmicpc.net/problem/1259
def check(txt):
    for i in range(len(txt)//2):
        if txt[i]!=txt[-i-1]:
            return False
    return True
while True:
    txt=input()
    if txt=='0':
        break
    print("yes" if check(txt) else "no")