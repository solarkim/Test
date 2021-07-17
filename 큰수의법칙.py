# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없음.
# M번 더해서 가장 큰수를 만드는데 같은 수를 K번 연속해서 더하면 안됨

# EX) [2,4,5,4,6] 배열에서 M=8, K=3
#     6+6+6+5+6+6+6+5 = 46

#  2 <= N <= 1000 , 1 <= M <= 10000 , 1 <= K <= 10000 의 자연수가 주어지며, 자연수는 공백
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 
# 단, 각각의 자연수는 1이상 10000이하의 수로 주어진다 
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

# N,M,K를 공백으로 구분하여 입력받기
n,m,k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort() # 입력받은 수 정렬
first=data[n-1] # 가장 큰 수
second=data[n-2] # 두 번째로 큰 수

result=0

while True:
    for i in range(k):
        if m==0:
            break
        result += first
        m-=1
    if m==0:
        break
    result+=second
    m-=1

print(result)