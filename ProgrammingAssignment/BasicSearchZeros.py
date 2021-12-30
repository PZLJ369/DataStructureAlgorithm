# This code is not the actual Assignment (this is only used for TESTING PURPOSE)
# This code is used to test the efficiency of the part 2 code (P2ChallengeAlgorithm.py)

# JI ZHUOLIN (202016N) IT2005
SEQ = [100, 305060, 60070080, 9009000900, 300300700800, 1004450005600000]
Z = 18
numbZero = []
# exist:     5(4),7(3),8(4),9(2),10(1),11(2),12(0),13(1),15(2),17(3),18(4)
# not exist: 6(5),14(5),16(5)


def CountZero():
    for numb in SEQ:
        strNumb = str(numb)
        sepNumb = list(strNumb)  # separate number, e.g.: 100 to ["1","0","0"]
        n = 0  # n: count the number of zero in each number
        for i in range(len(sepNumb)):
            while sepNumb[i] == '0':
                n += 1
                break
        numbZero.append(n)


def BasicSearchZero(zeroList, Z):
    CountZero()
    low = 0
    high = len(zeroList) - 1
    p = 0

    while low < high:
        if zeroList[low] + zeroList[high] == Z:
            X = SEQ[low]
            Y = SEQ[high]
            print('X:', X, 'Y:', Y)
            return True
        elif zeroList[low] + zeroList[high] < Z:
            low += 1
        elif zeroList[low] + zeroList[high] > Z:
            high -= 1
        p += 1
        print("pass:",p)
    else:
        print('X: Not Found, Y: Not Found')

    return False


BasicSearchZero(numbZero, Z)

