import sys
sys.stdin = open('input.txt' ,'r')

T = int(input())
for t in range(T):
    rounds = int(input())
    num_set = []
    for r in range(rounds):
        dum = list(map(int, input().split()))
        num_set += [dum]
    roads = len(num_set) * 2 - 2
    row = len(num_set)
    min_roads = 0
    for i in range(1 << roads):
        if str(bin(i)).count('1') == (roads >> 1):
            if str(bin((1 << roads) - 1 - i)).count('1') == (roads >> 1):
                x = 0
                y = 0
                deft = num_set[y][x]
                road_sum = deft
                cntx = 0
                cnty = 0
                bp = 0
                for j in range(roads):
                    if i & (1 << j):
                        if cntx < len(num_set) - 1:
                            x += 1
                            cntx += 1
                    else:
                        if cnty < len(num_set) - 1:
                            y += 1
                            cnty += 1
                    deft = num_set[y][x]
                    road_sum += deft
                if min_roads == 0:
                    min_roads = road_sum
                elif road_sum < min_roads:
                    min_roads = road_sum
    print(f'#{t + 1} {min_roads}')