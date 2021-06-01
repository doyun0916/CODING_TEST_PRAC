# 5. 더 맵게
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    counts = 0                      # 음식 섞은 횟수 count.
    while True:
        complete = True
        for food in scoville:        # 모든 음식의 스코빌지수가 k이상인지 확인
            if food < K:
                complete = False
                break
        if complete:
            break
        else:
            if len(scoville) == 1:   # 음식은 1개인데 스코빌지수가 k이하면, -1 return
                counts = -1
                break
            else:                     # 아니라면, 가장 맵지 않은 음식 2개 섞음.
                first = heapq.heappop(scoville)
                second = heapq.heappop(scoville)
                new = first + (second * 2)
                heapq.heappush(scoville, new)
                counts += 1
    answer = counts
    return answer

# heapq를 사용해, 가장 안 매운 음식의 지수, 두번째로 맵지 않은 음식의 지수 pop하여, 섞는 방법 이용.

# 오픈채팅방
def solution(record):
    result = []
    moves = []                                     # 기록 저장을 위한 list
    moves_ap = moves.append
    ids = dict()                                   # 각각의 id별 nickname 저장할 dict
    for rec in record:                             # 각각의 기록에 대해,
        now = list(rec.split())
        if len(now) == 3:                          # ENTER, CHANGE면, 
            move, user_id, nickname = now
            if move[0] == 'E':                 # ENTER
                moves_ap([user_id, '님이 들어왔습니다.'])
                ids[user_id] = nickname
            else:                              # CHANGE
                ids[user_id] = nickname
        else:                                       # LEAVE면,
            move, user_id = now
            moves_ap([user_id, '님이 나갔습니다.'])
            
    for i in range(len(moves)):                     # 각각의 기록에 대해, 최종 변경된 nickname을 적용하여 출력.
        message = ids[moves[i][0]] + moves[i][1]
        result.append(message)
    answer = result
    return answer

# ids = ['uid1234': 'Muzi', ...]                       <- change
# moves = [['uid1234', '님이 들어왔습니다.'], ...]        <- enter, leave
# 마지막에, 각각 id에 해당하는 최종 nickname을 moves에 적용하여 return.

# 문자열 압축
def solution(s):
    max_iter = len(s) // 2             # 최대로 자를수 있는 단위
    if max_iter == 0:                  # s가 한개만 주어졌을때 return 1
        return 1
    result = []
    for i in range(1, max_iter+1):     # 1개로 짜를때, 2개로 짜를떄, .....
        before = None
        counts = 1
        temp = []
        for j in range(0, len(s), i):
            now = s[j:j+i]
            if before == now:           # 전에 잘랐던 문자열과 현재 문자열이 같다면 count+1. 마지막 문자열이면, append.
                counts += 1
                if j+i == len(s):
                    temp.append(str(counts) + before)
            else:                       # 같지 않다면,
                if before is not None:
                    if counts == 1:     # 현재까지 쌓아온 문자열들이 같은게 전혀 없었다면, 그대로 append
                        temp.append(before)
                    else:               # 아니라면, 쌓아온 문자열만들 숫자 + 문자열 append
                        temp.append(str(counts) + before)
                    if len(before) != len(now) or j + i == len(s):  # 마지막 문자열이면, 추가로 append 후 종료.
                        temp.append(now)
                counts = 1       # count 초기화
                before = now     # 비교 기준 문자열 초기화.
        result.append(temp)
    min_val = int(1e9)
    for r in result:                      # 자른 단위별 길이 중 가장 작은 값 출력.
        temp = len("".join(r))
        min_val = min(min_val, temp)
    answer = min_val
    return answer

# a a b b a c c c -> 2a2ba3c -> 7
# aa bb ac cc -> aabbaccc -> 8
# aab bac cc -> aabbaccc -> 8
# ...

# 타겟 넘버
def dfs(numbers, step, added, target, result):    #(주어진 수들, 사용된 수들, 계산된 수, 목표, 타겟으로 만들어진 개수)
    if added == target and step == len(numbers):
        return result + 1
    elif step == len(numbers):
        return result
    else:
        result = dfs(numbers, step + 1, added + numbers[step], target, result)
        result = dfs(numbers, step + 1, added - numbers[step], target, result)
        return result

def solution(numbers, target):
    result = dfs(numbers, 0, 0, target, 0)
    answer = result
    return answer

# + -> + -> + -> +
# + -> + -> + -> -
# ...

# 수식 최대화
from itertools import permutations
def calculate(sign, a, b):
    if sign == '-':
        return a - b
    elif sign == '+':
        return a + b
    else:
        return a * b

def solution(expression):
    cal = ['-', '+', '*']
    cal_list = list(permutations(cal, 3))        # 3개의 연산자로 만들수 있는 6가지 경우의 수 계산.
    max_val = -int(1e9)
    exp = []
    now = 0
    for i in range(len(expression)):             # 숫자, 연산자 분리.
        if i == len(expression) - 1:             # iteration이 마지막이라면, 마지막 숫자 저장 후 종료.
            exp.append(expression[now:])
        if expression[i] in cal:                 # 연산자 등장시, 저장 및 앞쪽 숫자 저장.
            exp.append(expression[now:i])
            exp.append(expression[i])
            now = i+1
    for cal_steps in cal_list:                   # 각각 6가지 경우의 수에 대해,
        origin = exp
        for k in range(3):
            now = cal_steps[k]                   # 현재 연산자
            stack = []
            jump = False
            for i in range(len(origin)):         # (연산자, 숫자) origin에 대해,
                if jump:                         # 계산 된 숫자 스킵을 위해 jump 이용.
                    jump = False
                    continue
                if origin[i] == now:             # 현재 연산자 등장시,
                    a = int(stack.pop())
                    b = int(origin[i+1])
                    temp = calculate(now, a, b)  # 계산 후, 저장
                    stack.append(temp)
                    jump = True
                else:
                    stack.append(origin[i])      # 연산자가 아닐시, 그냥 저장.
            origin = stack                       # 다음 연산자 계산을 위해, 첫 우선순위 연산자를 통해 바뀐 수식 저장.
        max_val = max(max_val, abs(int(stack[0])))   # 최종 숫자의 abs 값 return.
    answer = max_val
    return answer


# 1. 6가지 경우의 수 설정. ['+', '-', '*'], ['-', '+', '*'] ...
# 2. 연산자, 숫자 분리. [100, '-', 200, '*', 300 ...]
# ['+', '-', '*'] -> '+' 먼저 2번 list가지고 진행. -> '-' 가지고 진행 ... -> 최종 값 절대값으로 return.
