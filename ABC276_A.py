import io
import sys

_INPUT = """\
6
abcdaxayz
bcbbbz
aaaaa
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  ans=-1
  for i in range(len(S)):
    if S[i]=='a': ans=i+1
  print(ans)