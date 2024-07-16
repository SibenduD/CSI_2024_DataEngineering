import textwrap
def merge_the_tools(st, k):
    # your code goes here
    t=textwrap.wrap(st, k)
    for i in t:
        l=[]
        for j in i:
            if j not in l:
                l.append(j)
        print(''.join(l))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)