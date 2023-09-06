
# 별 찍기. 
# 1009 분산처리
# 2563 색종이
arr = [[0] * 100 for _ in range(100)]
n = int(input())

for i in range(n):
    col,row = map(int,input().split())
    # 이 좌표는 배열 arr에서 1로 마킹할 시작점으로 사용된다.
    for j in range(col, col +10):
        for k in range (row, row+10):
            arr[j-1][k-1] = 1
            # 10*10크기의 부분 배열을 1로 마킹
            # col과 row가 1부터 시작하지만 배열의 인덱스는 0부터 시작
            # -1로 인덱스 조정
            
answer= 0
# answer에 포함된 1의 개수 저장 
for i in range(100):
    answer += sum(arr[i])
    # 2차원 배열 arr의 모든 요소의 합을 계산하여 answer에 더함. 

print(answer)
    



# 1475 방 번호
import math
n = input().strip()
num_dic = {str(i):0 for i in range(10)}
# 숫자를 문자열로 하나씩 쪼개서 받는다.
# 0-9까지 딕셔너리를 만들고 0으로 초기화. 

for i in n:
    if i not in ['6','9']:
        num_dic[i] +=1
    else:
        num_dic['6'] += 0.5
# for문으로 6이나 9가 아니면 해당 값에 1누적. 6이나 9이면 6에 0.5씩 넣는다.
 

for key,value in num_dic.items():
    num_dic[key] =  math.ceil(value)

num_dic = sorted(num_dic.values(),reverse=True)
print(num_dic[0])
# 그 다음에 다시 math.ceil을 사용하여 6.5의 값을 가진 6을 올림함.
# 내림차순으로 정렬해서 처음 인덱스만 출력





## 2503 숫자야구
from itertools import permutations
N = int(input())
# 사용자에게 정수 입력 받음, 

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))
# 가능한 3자리 숫자를 모두 만듦. 

for _ in range(N):
    n, s, b = map(int, input().split())
    # 사용자로부터 n과 해당 숫자의 스트라이크(s), 볼(b)를 입력받는다. 
    n = list(str(n))
    # n을 문자열로 변환 -> 각 자리 숫자를 요소로 갖는 리스트로 바꿈, 
    rmcnt = 0
    # 이후 수녕ㄹ에서 제거할 순서를 저장하는 변수 rmcnt
    for i in range(len(num)):
        # 리스트의 순열들에 대해 반복문 시작. 
        strike = ball = 0
        # 초기화 
        i -= rmcnt # num[0] 부터 시작
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
                # 스트라이크. 현재 순열 = 입력한 숫자의 자리 해당 여부 
            elif n[j] in num[i]:
                ball += 1
                # 숫자 자리는 다르고 입력한 숫자는 포함될 경우. 볼 증가. 
            
        if (strike != s) or (ball != b):
            num.remove(num[i])
            rmcnt += 1

print(len(num))
# 최종적으로 남아있는 가능한 세 자리 수의 개수를 출력. 
