import os, re, copy, pprint, wordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')


# Return Substitution Cipher with Mode 'ENCRYPT' or 'DECRYPT'
def substitution_cipher(message, MODE, key):
    
    translated = ''
    charsA = LETTERS
    charsB = key
    
    if MODE.upper() == 'DECRYPT':
        charsA, charsB = charsB, charsA

    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol

    return translated


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


def getBlankCipherletterMapping():
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
    'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P':
    [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [],
    'Y': [], 'Z': []}


def addLettersToMapping(letterMapping, cipherword, candidate):
    letterMapping = copy.deepcopy(letterMapping)
    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])
    return letterMapping


def intersectMappings(mapA, mapB):
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:
        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else:
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)
    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping):
    letterMapping = copy.deepcopy(letterMapping)
    loopAgain = True
    while loopAgain:
        loopAgain = False
        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])
                
        for cipherletter in LETTERS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        loopAgain = True
    return letterMapping


def crackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        newMap = getBlankCipherletterMapping()
        wordPattern = getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue
        for candidate in wordPatterns.allPatterns[wordPattern]:
            newMap = addLettersToMapping(newMap, cipherword, candidate)
        intersectedMap = intersectMappings(intersectedMap, newMap)
    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherLetterMapping(ciphertext, letterMapping):
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)
    print('\nKey: ' + key)
    return substitution_cipher(ciphertext, 'DECRYPT', key)
            

def main():
    message = """"""

    print('Hacking ...')
    letterMapping = crackSimpleSub(message)
    print('Mapping: ')
    pprint.pprint(letterMapping)
    print('\nOriginal ciphertext: ')
    print(message)
    crackedMessage = decryptWithCipherLetterMapping(message, letterMapping)
    print('\nCracked message: ')
    print(crackedMessage)


if __name__ == '__main__':
    main()
