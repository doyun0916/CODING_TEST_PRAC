# 1. 멀쩡한 사각형


# 2. 124 나라의 숫자.
def solution(n):
    num = ['4', '1', '2']            # 기본으로 표현할 수 있는 수들
    lis = []                         # 나머지들을 저장할 배열
    if n < 4:                        # 기본으로 표현가능한 수들은 바로 return
        return num[n % 3]
    before = n
    while True:
        quotient = before // 3         # 3으로 나눈 몫
        remainder = before % 3         # 3으로 나눈 나머지
        if remainder == 0:             # 나머지가 0이라면 몫 - 1의 자연수가 표현된 진법 사용.
            before = quotient - 1
        else:
            before = quotient          # 아니라면, 다음에 진행할 몫을 저장
        lis.append(remainder)          # 나머지 저장.
        if before < 4:                 # 다음에 진행할 몫이 4 이하면, 탈출. 진행할 필요가 없으니까.
            break
    now = num[before % 3]              # 현재 몫부터 변환.
    while lis:                         # now에 차례로 이어서 변환된 값을 덛붙인다.
        remainder = lis.pop()
        now = now + num[remainder % 3]
    return now
 
# # 규칙대로 계속 나누면서 필요한 애들만 계산.
# # 거꾸로 접근. 나머지가 0일 경우, 몫 - 1 의 값을 적용.


# 3. 짝지어 제거하기
def solution(s):
    stack = [s[0]]
    if len(s) % 2 != 0:            # 문자가 홀수개면 바로 return 0
        return 0
    for i in range(1, len(s)):      # 문자 크기만큼 스택에 저장.
        if not stack:
            stack.append(s[i])
            continue
        if stack[-1] == s[i]:      # 현재 문자와 전에 넣은 문자가 같다면, 둘다 삭제.
            stack.pop()
        else:
            stack.append(s[i])     # 아니면 계속 스택에 저장.
    if not stack:                  # 마지막에 스택이 비어있다면 성공.
        answer = 1
    else:                          # 아니면 실패.
        answer = 0
    return answer


# 4. 기능개발
def solution(progresses, speeds):
    deploy = []                                # 한번 배포할때마다 몇개씩 되었는지 저장할 배열
    deploy_turn = 0                            # 몇번째부터 배포해야하는지 가리킬 변수
    jobs = len(progresses)                     # 총 작업 수
    while deploy_turn < jobs:       # 모든 작업이 배포될때까지를 max iterations으로
        temp = deploy_turn
        counts = 0
        for i in range(jobs):                  # 매 루프마다 모든 작업에 각각의 1일치 진행도를 더해준다.
            progresses[i] += speeds[i]
        for i in range(temp, jobs):            # 작업들이 100을 넘었는지 확인하고, 넘었다면 count로 숫자를 새주며, 다음에 배포될 작업을 포인팅한다.
            if progresses[i] >= 100:
                deploy_turn = i + 1
                counts += 1
            else:                              # 넘지 않았다면, 다음날로 넘어간다.
                break
        if counts != 0:
            deploy.append(counts)
    answer = deploy
    return answer


# reference)
# 1. 멀쩡한 사각형
from math import gcd
def solution(w,h):
    iteration = gcd(w, h)                           # 최대공약수만큼의 블록이 직선상에 반복된다.
    unusable = iteration * ((w // iteration) + (h // iteration) - 1)         #각 블록당 사용 불가한 사각형 개수는 (가로 + 세로 - 1)개, 그러므로, 여기에 x 블록 개수 = 사용 불가 볼록
    answer = (w * h) - unusable
    return answer
