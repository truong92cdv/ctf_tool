import pprint


def getWordPattern(word):
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])
    return '.'.join(wordPattern)


def main():
    allPatterns = {}

    f = open('dictionary_french.txt')
    wordList = f.read().split('\n')
    f.close()

    for word in wordList:
        pattern = getWordPattern(word)
        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    f = open('wordPatterns_french.py', 'w')
    f.write('allPatterns = ')
    f.write(pprint.pformat(allPatterns))
    f.close()


if __name__ == '__main__':
    main()
