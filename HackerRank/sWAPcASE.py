def swap_case(s):
    # string=list(s)
    # sentence = ""
    # for i in range(len(string)):
    #     if string[i].islower():
    #         sentence = sentence + string[i].upper()
    #     elif string[i].isupper():
    #         sentence = sentence + string[i].lower()
    #     else:
    #         sentence = sentence + string[i]
    sentence = [i.upper() if i.islower() == True else i.lower() for i in s] #list comprehension
    return "".join(sentence)
    return sentence

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)