# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
# 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
# 1. N에서 1빼기
# 2. N을 K로 나누기

# EX) N=17 K=4이면 실행횟수는 3이됨. 17 -> 16 -> 4 -> 1

# 2<= N <=100000 , 2<=K<=100000
# 주어진 N은 항상 K보다 크거나 같다.

# 수행해야하는 횟수 최솟값을 출력

# TIP : 최대한 많이 나누기

n,k = map(int,input().split())
result = 0

while n > k:
    while n % k != 0:
        n-=1
        result+=1
    n//=k
    result+=1

while n>1:
    n-=1
    result+=1

print(result)
