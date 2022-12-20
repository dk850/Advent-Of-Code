from string import ascii_lowercase
from collections import deque


def getnns(x: int, y: int) -> list:
    return [ i for i in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] \
        if i[0] >= 0 and i[0] <= xm and i[1] >= 0 and i[1] <= ym \
            if topo.get(i) - topo.get((x, y)) < 2 ]

h = lambda v: list('S'+ascii_lowercase+'E').index(v) \
    if v in 'S'+ascii_lowercase+'E' else None

itxt = [list(r) for r in open("input", mode='r').read().splitlines()]
topo = {(x,y):h(v) for y, r in enumerate(itxt) for x, v in enumerate(r)}
xm, ym = len(itxt[0]) -1, len(itxt) -1

s = [c for c, v in topo.items() if v == 0][0]
e = [c for c, v in topo.items() if v == 27][-1]
qp, qv = deque([(0,s[0],s[1])]), deque([(0,s[0],s[1])])

while qp:
    ns, nx, ny = qp.popleft()
    
    if (nx, ny) == e: break
    if (nx, ny) in qv: continue
    qv.append((nx, ny))
    
    for nnx, nny in getnns(nx, ny):
        qp.append((ns+1, nnx, nny))
print(min([ns for ns, nx, ny in qp]))
