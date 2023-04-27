#dist = abs(x_origin - x) + abs(y_origin - y)
#prey = sorted(can_eat, key = lambda x: (x[2], x[0], x[1]))[0]
#거리계산을 이렇게 해버리면 원래의 위치에서 지나야할 칸을 고려하지 못함.

from collections import deque

N = int(input())
board = []
#각 좌표의 시간 저장
board_time = [[-1 for i in range(N)] for j in range(N)]

size = 2
eat_count = 0
result = 0

#상어의 현재 위치
x_origin = 0
y_origin = 0

max_xy = 20
min_x = max_xy
min_y = max_xy

min_dist = 401

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque([])

for x in range(N):
    a = list(map(int, input().split()))
    if 9 in a:
        x_origin = x
        y_origin = a.index(9)
        #아기상어의 초기 위치의 시간은 0.
        board_time[x_origin][y_origin] = 0
    board.append(a)

def init():
    global board_time, min_x, min_y, min_dist, max_xy
    board_time = [[-1 for i in range(N)] for j in range(N)]
    min_x = max_xy
    min_y = max_xy
    min_dist = 401

while True:
    queue.append((x_origin, y_origin))
    board_time[x_origin][y_origin] = 0
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
                
            board_time[x][y] = board_time[curr_pos[0]][curr_pos[1]] + 1
            
            #먹이가 있을 경우
            if board[x][y] != 0 and board[x][y] < size:
                #지금 거리 계산이 제대로 되지 않고 있음.
                #어차피 모든 간선이동은 코스트가 1이므로 이동시간을 거리로 칠 수 있다.
                #지금까지의 거리보다 더 짧은 거리의 먹이일 경우
                if min_dist > board_time[x][y]:
                    min_x = x
                    min_y = y
                    min_dist = board_time[x][y]
                #거리가 같을 경우, 즉 여러 마리의 먹이가 있을 경우 가장 위의 가장 왼쪽을 찾는다.
                elif min_dist == board_time[x][y]:
                    if min_x == x:
                        if min_y > y:
                            min_x = x
                            min_y = y
                    elif min_x > x:
                        min_x = x
                        min_y = y
            
            queue.append((x, y))
            
            
    #먹이를 찾은 경우
    if min_x != max_xy and min_y != max_xy:
        board[min_x][min_y] = 0
        result += board_time[min_x][min_y]
        eat_count += 1
        if eat_count == size:
            size += 1
            eat_count = 0
        #아기 상어 이동
        board[x_origin][y_origin] = 0
        x_origin = min_x
        y_origin = min_y
        init()
    else:
        print(result)
        break
