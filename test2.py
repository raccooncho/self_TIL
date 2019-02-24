import sys
sys.stdin = open('input.txt' ,'r')

T = int(input())
for t in range(T):
    rounds = list(map(int, input().split()))
    bus = rounds[0]
    busstop = rounds[1:bus] + [0]

    cnt = 0
    roads = 0
    fuel = 0
    while roads < bus - 1:
        if bus - 1 - roads <= busstop[fuel] + fuel:
            cnt += 1
            roads = bus - fuel - 1
            fuel = 0
        else:
            fuel += 1



    print(f'#{t + 1} {cnt-1}')