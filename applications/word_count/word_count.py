from collections import Counter


def word_count(s):
    # Your code here
    # do something
    counting = dict()

    # splits the words that are coming in through 's' parameter.
    words = s.split()

    # for loop words and add a 1 if a specific word is found again.

    for word in words:
        if word in counting:
            counting[word] += 1
        else:
            # if the word only appears once then keep at '1'. if not repeat the loop.
            counting[word] = 1

    # returns counting which is = to dict().
    return counting


# TODO I need to lowercase the output.

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
