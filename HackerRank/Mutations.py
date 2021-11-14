def mutate_string(string, position, character):
    s = list(string) #make list
    s[position] = character #convert the character
    return "".join(s)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)