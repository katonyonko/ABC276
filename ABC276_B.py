import io
import sys

_INPUT = """\
6
6 6
3 6
1 3
5 6
2 5
1 2
1 6
5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  ans=[[] for _ in range(N)]
  for i in range(M):
    A,B=map(lambda x: int(x)-1,input().split())
    ans[A].append(B+1)
    ans[B].append(A+1)
  for i in range(N):
    print(len(ans[i]), *sorted(ans[i]))