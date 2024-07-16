def minion_game(string):
    length = len(string)
    vowels = "AEIOU"
    total_substrings = (length * (length + 1)) // 2
    kevin = sum(length - i for i in range(length) if string[i] in vowels)
    stuart = total_substrings - kevin
    if stuart == kevin:
        print("Draw")
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Kevin", kevin)
if __name__ == '__main__':
    s = input()
    minion_game(s)
