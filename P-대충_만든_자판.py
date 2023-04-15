# src: https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    D=dict()
    for keys in keymap:
        for i,key in enumerate(keys):
            temp=D.get(key)
            if temp:
                D[key]=min(temp, i+1)
            else:
                D[key]=i+1
    answer = []
    for target in targets:
        ans=0
        for t in target:
            if D.get(t):
                ans+=D[t]
            else:
                ans=-1
                break
        answer.append(ans)
    return answer