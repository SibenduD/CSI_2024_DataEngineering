def print_rangoli(s):
    # your code goes here
    ab='abcdefghijklmnopqrstuvwxyz'
    mid=((n+(n-1))*2)-1
    rev=[]
    for i in range(s):
        r=''
        k=''
        for j in range(i+1):
            if j==i:
                r+=ab[s-1-j]
                top=r+k[::-1]
                t=top.center(mid,"-")
                rev.append(t)
                print(t)
            else:
                r+=ab[s-1-j]+"-"
                k=r
    for i in range(s-1):
        print(rev[s-2-i])
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)