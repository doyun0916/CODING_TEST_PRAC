# [1차] 뉴스 클러스터링
# 자카드 거리 = 교집합 / 공집합
# 모두 공집합일때는 자카드 거리 = 1
# a, b 있으면, a b 교집합 원소들 각각 a,b에서 빼고, 남은것들 + '교집합' 하면, 합집합 나옴.
# 대소문자 무시하고 같은 원소로 취급.
import math
def split(string):
    str_re = []
    for a, b in zip(string, string[1:]):
        if not a.isalpha() or not b.isalpha():
            continue
        else:
            str_re.append(a+b)
    return str_re


def solution(str1, str2):
    str1_re = split(str1)
    str2_re = split(str2)
    str1_len, str2_len = len(str1_re), len(str2_re)
    str2_bi = [False] * str2_len
    common = 0
    for i in range(str1_len):
        for j in range(str2_len):
            if not str2_bi[j]:
                if str1_re[i].upper() == str2_re[j].upper():
                    common += 1
                    str2_bi[j] = True
                    break
    intersect = common
    union = len(str1_re) + len(str2_re) - common
    if union == 0:
        answer = 1 * 65536
    else:
        answer = math.floor((intersect / union) * 65536)
    return answer
  
  # 튜플
  def solution(s):
    s = s[1:-1]
    s_n = []
    start = None
    temp = []
    sub = []
    for lis in s:
        if lis == '{':
            start = True
            continue
        if start:
            if lis == ',':
                sub_str = "".join(sub)
                temp.append(int(sub_str))
                sub = []
            elif lis == '}':
                sub_str = "".join(sub)
                temp.append(int(sub_str))
                s_n.append(temp)
                temp, sub = [], []
                start = False
            else:
                sub.append(lis)
    len_check = [(len(s_n[i]), i) for i in range(len(s_n))]        # 길이, 번째.
    len_check.sort()
    result = []
    for k in len_check:
        for j in s_n[k[1]]:
            if j not in result:
                result.append(j)
    answer = result
    return answer

#개수가 1인 놈부터 차례대로 탐색 시작! 그 순서대로 1개씩 더해질때마다 순서 상관없이 그 값 append.

# 전화번호 목록
def solution(phone_book):
    phone_book.sort()
    answer = True
    counts = len(phone_book)
    for i in range(counts-1):
        mid_check = False
        for j in range(i+1, counts):
            print(phone_book[j], phone_book[i])
            if phone_book[j].find(phone_book[i]) >= 0:
                    mid_check = True
                    break
        if mid_check:
            answer = False
            break
    return answer
  
  # 메뉴 리뉴얼
  from itertools import combinations
from collections import Counter
def solution(orders, course):
    result = []
    for num in course:
        result_sub = []
        for order in orders:
            iters = list(combinations(order, num))
            for ite in iters:
                ite = list(ite)
                ite.sort()
                ite = tuple(ite)
                if ite in result_sub:
                    continue
                temp = []
                for i in range(len(orders)):
                    stop = False
                    for alp in ite:
                        if alp not in orders[i]:
                            stop = True
                            break
                    if not stop:
                        temp.append(ite)
                result_sub = result_sub + temp
        result_sub = Counter(result_sub).most_common()
        if result_sub:
            max_val = result_sub[0][1]
        else:
            continue
        if max_val == 1:
            continue
        for result_s in result_sub:
            if result_s[1] == max_val:
                result.append("".join(result_s[0]))
    result.sort()
    answer = result
    return answer
  
  # 예상 대진표
  def solution(n,a,b):
    lis = [i for i in range(1, n+1)]
    counts = 0
    stop = False
    while True:
        if stop:
            break
        temp = []
        for i in range(0, len(lis)-1, 2):
            check1 = lis[i]
            check2 = lis[i+1]
            if (check1 == a or check1 == b) and (check2 == a or check2 == b):
                stop = True
                break
            if check1 == a or check1 == b:
                temp.append(check1)
            elif check2 == a or check2 == b:
                temp.append(check2)
            else:
                temp.append(check1)
        lis = temp
        counts += 1
    answer = counts
    return answer
  
  # 프린터
  def solution(priorities, location):
    priority = [(i, priorities[i]) for i in range(len(priorities))]
    iters = 0
    while True:
        current_max = priority.index(max(priority, key=lambda x: x[1]))
        pre = priority[:current_max]
        post = priority[current_max+1:]
        iters += 1
        if priority[current_max][0] == location:
            break
        else:
            priority = post + pre
    answer = iters
    return answer
