import io
import sys

_INPUT = """\
6
3
5 7 5
7
22 75 26 45 72 81 47
2
6 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  class BIT:
      def __init__(self, n):
          self._n = n
          self.data = [0] * n
      def add(self, p, x):
          assert 0 <= p < self._n
          p += 1
          while p <= self._n:
              self.data[p - 1] += x
              p += p & -p
      #合計にはrを含まない
      def sum(self, l, r):
          assert 0 <= l <= r <= self._n
          return self._sum(r) - self._sum(l)
      def _sum(self, r):
          s = 0
          while r > 0:
              s += self.data[r - 1]
              r -= r & -r
          return s

  mod=998244353
  N=int(input())
  A=list(map(int,input().split()))
  bit=BIT(2*10**5)
  bit2=BIT(2*10**5)
  ans=0
  for i in range(N):
    ans+=bit2.sum(0,A[i]-1)*A[i]*2+bit.sum(A[i]-1,2*10**5)*2+A[i]
    ans%=mod
    bit.add(A[i]-1,A[i])
    bit2.add(A[i]-1,1)
    print(ans*pow((i+1)**2,mod-2,mod)%mod)