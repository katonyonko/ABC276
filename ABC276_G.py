import io
import sys

_INPUT = """\
6
3 4
276 10000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,M=map(int,input().split())
  F=[1]
  k=N+M
  for i in range(k):
    F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(k):
    I.append(I[-1]*(k-i)%mod)
  I=I[::-1]
  ans=0
  for i in range(5):
    if i==0 or i==4: t=1
    elif i==1 or i==3: t=2
    else: t=3
    for k in range(N):
      if (M-k-2*(N-1-k)-i)%3!=0 or M-k-2*(N-1-k)-i<0: continue
      ans=(ans+t*F[N-1]*I[k]*I[N-1-k]%mod*F[(M-k-2*(N-1-k)-i)//3+N]*I[N]*I[(M-k-2*(N-1-k)-i)//3]%mod)%mod
  print(ans)