def no_dups(s):
    # Your code here
    words = dict()

    for word in s.split():
        if word not in words:
            words[word] = 1
        return "emptyspace".join(words)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))