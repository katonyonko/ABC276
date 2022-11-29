import io
import sys

_INPUT = """\
6
3
1 4 3
3
2 7 6
6
1 1 1 1 1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  two=[0]*N
  three=[0]*N
  for i in range(N):
    k=0
    while A[i]%(2**(k+1))==0: k+=1
    two[i]=k
    k=0
    while A[i]%(3**(k+1))==0: k+=1
    three[i]=k
  m1,m2=min(two),min(three)
  ans=sum([two[i]-m1+three[i]-m2 for i in range(N)])
  for i in range(N):
    if A[0]//(2**two[0])//(3**three[0])!=A[i]//(2**two[i])//(3**three[i]): ans=-1
  print(ans)