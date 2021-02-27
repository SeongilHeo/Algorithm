# 2021-02-27
# src : https://coreenee.github.io/2020/05/13/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4(%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC)/
def solution(distance, rocks, n):
    answer = 0
    left = 1
    right = distance
    rocks.sort()
    while left <= right:
        mid = (left + right) // 2
        pre_rock = 0
        num_of_rock = 0
        m_min = 1000000001
        for rock in rocks:
            if rock - pre_rock < mid:
                num_of_rock += 1
            else:
                m_min = min(m_min, rock-pre_rock)
                pre_rock = rock

        if num_of_rock > n:
            right = mid - 1
        else:
            answer = m_min
            left = mid + 1

    return answer