
_ = int(input())
s = set(map(int, input().split()))
command_count = int(input())
for _ in range(command_count):
    command=input()
    if command == "pop":
        s.pop()
        continue
    command, num = command.split()
    num = int(num)
    if command == "remove":
        s.remove(num)
    elif command == "discard":
        s.discard(num)
print(sum(s))