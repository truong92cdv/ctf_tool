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
    message = """azthxvyb nlxl sb kzdx jqvh - bdgbysydyszt_asunlxb_vxl_bzqovgql_gmuvmlvjas
-------------------------------------------------------------------------------
avqq cl sbncvlq. bzcl klvxb vhz-tlolx cstw nzm qzth uxlasblqk-nvosth qsyyql zx tz cztlk st ck udxbl, vtw tzynsth uvxysadqvx yz stylxlby cl zt bnzxl, s ynzdhny s mzdqw bvsq vgzdy v qsyyql vtw bll ynl mvylxk uvxy zj ynl mzxqw. sy sb v mvk s nvol zj wxsosth zjj ynl buqllt vtw xlhdqvysth ynl asxadqvyszt. mnltlolx s jstw ckblqj hxzmsth hxsc vgzdy ynl czdyn; mnltlolx sy sb v wvcu, wxsffqk tzolcglx st ck bzdq; mnltlolx s jstw ckblqj stozqdtyvxsqk uvdbsth gljzxl azjjst mvxlnzdblb, vtw gxsthsth du ynl xlvx zj lolxk jdtlxvq s clly; vtw lbulasvqqk mnltlolx ck nkuzb hly bdan vt duulx nvtw zj cl, ynvy sy xledsxlb v byxzth czxvq uxstasuql yz uxlolty cl jxzc wlqsglxvylqk byluusth styz ynl byxlly, vtw clynzwsavqqk ptzapsth ulzuql'b nvyb zjj-ynlt, s vaazdty sy nshn yscl yz hly yz blv vb bzzt vb s avt. ynsb sb ck bdgbysydyl jzx usbyzq vtw gvqq. msyn v unsqzbzunsavq jqzdxsbn avyz ynxzmb nscblqj duzt nsb bmzxw; s edslyqk yvpl yz ynl bnsu. ynlxl sb tzynsth bdxuxsbsth st ynsb. sj ynlk gdy ptlm sy, vqczby vqq clt st ynlsx wlhxll, bzcl yscl zx zynlx, anlxsbn olxk tlvxqk ynl bvcl jllqsthb yzmvxwb ynl zalvt msyn cl.

ynlxl tzm sb kzdx stbdqvx asyk zj ynl cvtnvyyzlb, glqylw xzdtw gk mnvxolb vb stwsvt sbqlb gk azxvq xlljb-azcclxal bdxxzdtwb sy msyn nlx bdxj. xshny vtw qljy, ynl byxllyb yvpl kzd mvylxmvxw. syb liyxlcl wzmtyzmt sb ynl gvyylxk, mnlxl ynvy tzgql czql sb mvbnlw gk mvolb, vtw azzqlw gk gxllflb, mnsan v jlm nzdxb uxloszdb mlxl zdy zj bshny zj qvtw. qzzp vy ynl axzmwb zj mvylx-hvflxb ynlxl.

asxadcvcgdqvyl ynl asyk zj v wxlvck bvggvyn vjylxtzzt. hz jxzc azxqlvxb nzzp yz azltyslb bqsu, vtw jxzc ynltal, gk mnsylnvqq, tzxynmvxw. mnvy wz kzd bll?-uzbylw qspl bsqlty bltystlqb vqq vxzdtw ynl yzmt, byvtw ynzdbvtwb duzt ynzdbvtwb zj czxyvq clt jsilw st zalvt xlolxslb. bzcl qlvtsth vhvstby ynl busqlb; bzcl blvylw duzt ynl uslx-nlvwb; bzcl qzzpsth zolx ynl gdqmvxpb zj bnsub jxzc anstv; bzcl nshn vqzjy st ynl xshhsth, vb sj byxsosth yz hly v bysqq glyylx blvmvxw ullu. gdy ynlbl vxl vqq qvtwbclt; zj mllp wvkb ulty du st qvyn vtw uqvbylx-yslw yz azdtylxb, tvsqlw yz gltanlb, aqstanlw yz wlbpb. nzm ynlt sb ynsb? vxl ynl hxllt jslqwb hztl? mnvy wz ynlk nlxl?

gdy qzzp! nlxl azcl czxl axzmwb, uvasth byxvshny jzx ynl mvylx, vtw bllcsthqk gzdtw jzx v wsol. byxvthl! tzynsth msqq aztylty ynlc gdy ynl liyxlclby qscsy zj ynl qvtw; qzsylxsth dtwlx ynl bnvwk qll zj kztwlx mvxlnzdblb msqq tzy bdjjsal. tz. ynlk cdby hly rdby vb tshn ynl mvylx vb ynlk uzbbsgqk avt msynzdy jvqqsth st. vtw ynlxl ynlk byvtw-csqlb zj ynlc-qlvhdlb. stqvtwlxb vqq, ynlk azcl jxzc qvtlb vtw vqqlkb, byxllyb vtw voltdlb-tzxyn, lvby, bzdyn, vtw mlby. kly nlxl ynlk vqq dtsyl. ylqq cl, wzlb ynl cvhtlysa osxydl zj ynl tllwqlb zj ynl azcuvbblb zj vqq ynzbl bnsub vyyxvay ynlc ynsynlx?"""

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

# https://www.guballa.de/substitution-solver
# https://www.guballa.de/vigenere-solver
# https://cryptii.com/