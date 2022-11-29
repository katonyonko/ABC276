import io
import sys

_INPUT = """\
6
4 4
....
#.#.
.S..
.##.
2 2
S.
.#
5 7
.#...#.
..#.#..
...S...
..#.#..
.#...#.
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #BFS
  from collections import deque
  def bfs(G,s):
    inf=10**20
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D

  H,W=map(int,input().split())
  C=[input() for _ in range(H)]
  G=[[] for _ in range(H*W)]
  ans='No'
  for i in range(H):
    for j in range(W):
      if C[i][j]=='#': continue
      elif C[i][j]=='S':
        si,sj=i,j
        continue
      for k,l in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0<=k<H and 0<=l<W and C[k][l]=='.': G[i*W+j].append(k*W+l)
  for i,j in [(si-1,sj),(si+1,sj),(si,sj-1),(si,sj+1)]:
    if 0<=i<H and 0<=j<W and C[i][j]=='.':
      D=bfs(G,i*W+j)
      for k,l in [(si-1,sj),(si+1,sj),(si,sj-1),(si,sj+1)]:
        if 0<=k<H and 0<=l<W and (i!=k or j!=l) and D[k*W+l]<10**20:
          ans='Yes'
  print(ans)