# 2019-2
import random, timeit
##
## 여기에 세 가지 정렬함수를 위한 코드를...
##
 
def quick_sort(A,first,last):
	global Qc, Qs
	if first >= last :
		return
	left, right = first+1, last
	pivot = A[first]
	while left<=right:
		while left <= last and A[left] < pivot:
			Qc += 1
			left += 1
		while right > first and A[right] >= pivot:
			Qc += 1
			right -= 1
		if left <= right:
			A[left], A[right] = A[right], A[left]
			Qs += 1
			left += 1
			right -= 1
	A[first],A[right] = A[right],A[first]
	Qs += 1
	quick_sort(A,first,right-1)
	quick_sort(A,right+1, last)
#-----------------------------------------------------------------------------------------------
def merge_sort(A,first,last):
	if first >= last:
		return
	m = (first+last)//2
	merge_sort(A, first, m)
	merge_sort(A,m+1,last)
	merge_two_sorted_list(A,first,last)
 
def merge_two_sorted_list(A,first,last):
	global Mc, Ms
	m=(first+last)//2
	B=[]
	i = first
	j =m+1
	while i <= m and j <= last:
		if A[i] < A[j]:
			Mc += 1
			B.append(A[i])
			i += 1
		else:
			B.append(A[j])
			j += 1
	for k in range(i,m+1):
		B.append(A[k])
	for k in range(j,last+1):
		B.append(A[k])
	A[first:last+1] = B[:]
#-----------------------------------------------------------------------------------------------
def heapify_down(C,k,n):#heap성질 만족하는 위치로 이동
	global Hs, Hc
	while 2*k+1 < n:#자식 노드가 있으면
		L,R = 2*k+1, 2*k+2#자식 노드의 인덱스
		if L < n and C[L] > C[k]: #왼쪽 자식이 더 클때
			Hc += 1
			m = L#왼쪽 자식 인덱스 저장
		else:#크거나 같을 때
			m = k#현재 위치 값
		if R < n and C[R] > C[m]:#오른쪽 자식이 나머지 둘보다 크다
			Hc += 1
			m = R#오른쪽 자식 인덱스 저장
		if m!= k:# 바꿔야 되면
			Hs += 1
			C[k],C[m] = C[m],C[k]#바꾸기
			k = m#인덱스 바꾸기
		else:#안바꿔도 되면
			break#탈출
				
def make_heap(C):
	n = len(C)#힙  크기
	for k in range(n-1,-1,-1):#마지막꺼부터 위치 찾아가기
		heapify_down(C,k,n)
	return C
			
def heap_sort(C):
	C=make_heap(C)
	n=len(C)
	for k in range(len(C)-1,-1,-1):
		C[0],C[k] = C[k],C[0]
		n=n-1
		heapify_down(C,0,n)
	
# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: 
			return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))