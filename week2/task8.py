#works only on pypy3
import re
n = int(input())
for _ in range(n):
    try:
        s = input()
        p = re.compile(s)
        print("True")
    except re.error:
        print("False")