def average(array):
    # your code goes here
    setCollection = set()


    for x in array:
         setCollection.add(x)

    sum = 0
    i = 0
    for val in setCollection:
        sum = sum + val
        i = i + 1

    total = sum/i

    return total

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)