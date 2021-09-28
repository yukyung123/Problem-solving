## 수 정렬하기 3
# ====문제 
#숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# ====입력 
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 
# 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
# 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
# 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

#----풀이 
#입력값이 10000개 까지 주어질 수 있으니 10000개 만큼의 리스트를 만들어 놓는다.
# 인덱스는 0부터 세므로, 길이가 10001인 리스트를 만든다.

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)