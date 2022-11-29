import io
import sys

_INPUT = """\
6
3
3 1 2
10
9 8 6 5 10 3 1 2 4 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  P=list(map(int,input().split()))
  now=10**100
  for i in reversed(range(N)):
    if P[i]>now:
      t=i
      now=P[i]
      break
    now=min(now,P[i])
  k=max([P[i] for i in range(t,N) if P[i]<now])
  print(*P[:t],k,*sorted([P[i] for i in range(t,N) if P[i]!=k],reverse=True))