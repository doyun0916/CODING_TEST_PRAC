## Question 1 #########################
def solution(board, moves):
    bag = [-1]
    c = 1
    result = 0
    for i in moves:
        for p in range(len(board)):
            if board[p][i-1] != 0:
                if bag[c-1] == board[p][i-1]:
                    bag.remove(bag[c-1])
                    board[p][i-1] = 0
                    c -= 1
                    result += 2
                    break
                else:
                    bag.append(board[p][i-1])
                    board[p][i-1] = 0
                    c += 1
                    break
    answer = result
    return answer