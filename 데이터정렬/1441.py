'''
버블 정렬
n = int(input())
data = list()

for i in range(n) :
	data.append(int(input()))
'''
import sys
n = int(sys.stdin.readline().rstrip())
data = list()
for i in range(n) :
	data.append(int(sys.stdin.readline().rstrip()))

for i in range(1,n) :
	for j in range(n-i) :
		if data[j] > data[j+1] :
			temp = data[j]
			data[j] = data[j+1]
			data[j+1] = temp

for d in data :
	print(d)

#print(data)
#print(" ".join(map(str,data)))

'''
파이썬 시간초과 이슈로 아래와 같이 제출
import sys
n = int(sys.stdin.readline().rstrip())
data = list()
for _ in range(n) :
	data.append(int(sys.stdin.readline().rstrip()))
data.sort()

for d in data :
	print(d)

'''