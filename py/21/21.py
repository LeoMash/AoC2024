import sys
from collections import defaultdict, deque
import heapq

f = '21.in'
# f = '21_test.in'

D = open(f).read().split('\n')
F = list(D)
# print(F)

NUM_S = "789\n456\n123\nX0A".split('\n')
NUM = defaultdict(lambda: 'X')
NUM_POS = {}
for y, ln in enumerate(NUM_S):
    for x, c in enumerate(ln):
        NUM[x, y] = c
        NUM_POS[c] = x, y

DIR_S = "X^A\n<v>\n".split('\n')
DIR = defaultdict(lambda: 'X')
DIR_POS = {}
for y, l in enumerate(DIR_S):
    for x, c in enumerate(l):
        DIR[x, y] = c
        DIR_POS[c] = x, y

DIR4 = {
    (0, 1): 'v',
    (1, 0): '>',
    (0, -1): '^',
    (-1, 0): '<',
}


def get_neighbours(s):
    for dx, dy in DIR4.keys():
        nx, ny = s[0] + dx, s[1] + dy
        yield nx, ny


def get_valid_neighbours(s, m):
    for n in get_neighbours(s):
        if m[n] != 'X':
            yield n


def dijkstra(m, start):
    cost = defaultdict(lambda: 1e10)
    cost[start] = 0
    prev = {}
    q = [(0, start)]

    while q:
        cur_cost, cur = heapq.heappop(q)
        if cur_cost > cost[cur]:
            continue
        assert cur_cost == cost[cur]

        for nbr in get_valid_neighbours(cur, m):
            ncost = cur_cost + 1
            if ncost < cost[nbr]:
                cost[nbr] = ncost
                prev[nbr] = [cur]
                heapq.heappush(q, (ncost, nbr))
            elif ncost == cost[nbr]:
                prev[nbr].append(cur)

    return dict(cost), prev


NUM_COSTS = {
    start: dijkstra(NUM, start) for start in list(NUM)
}
DIR_COSTS = {
    start: dijkstra(DIR, start) for start in list(DIR)
}

# NUM_ROBOT_LAYERS = 2
NUM_ROBOT_LAYERS = 25
LAYERS = [(NUM_COSTS, NUM_POS)] + [(DIR_COSTS, DIR_POS)] * NUM_ROBOT_LAYERS


def get_paths(m, src, tgt):
    if tgt == src:
        return [""]
    x, y = tgt
    m_paths = m[src][1]

    res = []
    prevs = m_paths[tgt]
    for prev in prevs:
        prev_x, prev_y = prev
        dx, dy = x - prev_x, y - prev_y
        move = DIR4[(dx, dy)]
        paths = get_paths(m, src, prev)
        for p in paths:
            res.append(p + move)

    return res


CACHE = {}
def go(i, csrc, ctgt):
    if i == len(LAYERS):
        return 1
        # return ctgt
    if (i, csrc, ctgt) in CACHE:
        return CACHE[(i, csrc, ctgt)]
    cost, m = LAYERS[i]
    src, tgt = m[csrc], m[ctgt]
    # min_path = ''
    min_path_len = 0
    for path in get_paths(cost, src, tgt):
        pos = 'A'
        # enc_path = ''
        enc_path_len = 0
        for c in path + 'A':
            # enc_path += go(i + 1, pos, c)
            enc_path_len += go(i + 1, pos, c)
            pos = c

        # if not min_path or len(enc_path) < len(min_path):
        #     min_path = enc_path
        if not min_path_len or enc_path_len < min_path_len:
            min_path_len = enc_path_len

    CACHE[(i, csrc, ctgt)] = min_path_len
    # return min_path
    return min_path_len


res = 0
for code in F:
    print('*', code)
    val = int(code[:-1])

    pos = 'A'
    # min_path = ''
    min_path_len = 0
    for c in code:
        # min_path += go(0, pos, c)
        min_path_len += go(0, pos, c)
        pos = c
    # print('->', min_path)
    # min_path_len = len(min_path)
    print('len = ', min_path_len)
    res += (min_path_len * val)

print('CACHE:', len(CACHE))

print(res)
