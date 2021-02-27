# 2021-02-27
def solution(begin, target, words):
    answer=0
    bfs = [begin]
    if target not in words:
        return 0
    while words:
        for l_text in bfs:
            temp=[]
            for word in words:
                if True if sum([0 if a==b else 1 for a,b in zip(l_text,word)]) == 1 else False:
                    temp.append(word)
                    words.remove(word)
        answer+=1
        if target in temp:
            return answer
        else:
            bfs = temp
    return 0