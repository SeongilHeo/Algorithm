# src: https://www.acmicpc.net/problem/1864
D={'-': 0, '\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while True:
    a=input()
    if "#"==a:
        break
    r=0
    for i,c in enumerate(a[::-1]):
        r+=D[c]*8**i
    print(r)