#https://www.acmicpc.net/problem/16236

'''
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
'''

#일단 먹을 수 있는 물고기를 찾고, 있다면 그때 시간을 더해야 할 듯

from collections import deque

N = int(input())
board = []
#각 좌표의 시간 저장
board_time = [[-1 for i in range(N)] for j in range(N)]
size = 2
eat_count = 0
can_eat = []
result = 0
min_dist = 401


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque([])

for x in range(N):
    a = list(map(int, input().split()))
    if 9 in a:
        queue.append((x, a.index(9)))
        #아기상어의 초기 위치의 시간은 0. 
        board_time[x][a.index(9)] = 0
    board.append(a)

while True:
    while queue:
        curr_pos = queue.popleft()
        for i in range(4):
            x = curr_pos[0] + dx[i]
            y = curr_pos[1] + dy[i]

            #맵 벗어난 경우
            if x < 0 or x >= N or y < 0 or y >= N:
                continue

            #상어보다 큰 물고기
            if board[x][y] > size:
                continue

            #이미 방문했다면 넘어간다.
            if board_time[x][y] != -1:
                continue

            #먹이가 있을 경우
            if board[x][y] != 0:
                dist = (abs(curr_pos[0] - x), abs(curr_pos[1] - y))
                can_eat.append((x, y, dist))

            queue.append((x, y))
            board_time[x][y] = board_time[curr_pos[0]][curr_pos[1]] + 1
    
    if len(can_eat) == 0:
        print(result)
        break
        
    else:
        result += board_time[]
        

