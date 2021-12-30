# Name: JI ZHUOLIN
# AdminNO: 202016N
# Group: IT2153_05
# Part 2 - Challenge Question on Algorithm

SEQ = [100, 305060, 60070080, 9009000900, 300300700800, 1004450005600000]
Z = 6
numbZero = []  # [2, 3, 5, 7, 8, 10]
# ---- Advance Search Result ---- [number of passes] -- current py file
# exist:     5(0),7(0),8(1),9(2),10(1),11(1),12(0),13(0),15(0),17(1),18(3)
# not exist: 6(3),14(5),16(5)
# ---- Basic Search Result ---- [number of passes] -- BasicSearchZeros.py
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


def AdvSearchZero(zeroList, Z):
    CountZero()

    low = 0
    high = len(zeroList) - 1
    p = 0

    # Set range 5 to 18, if out of range do not search print('not found') directly
    if zeroList[low] + zeroList[low + 1] > Z or zeroList[high - 1] + zeroList[high] < Z:
        print('X: Not Found, Y: Not Found')

    # if within range
    else:
        while low < high:  # no repeat of numbers e.g. 6 -> 305060 & 305060
            if Z > zeroList[high]:  # zeroList[high] as the dividing line
                # search -> get larger number first then find smaller one.
                newZ = Z - zeroList[high]  # find smaller number
                mid = (low+high)//2
                if newZ == zeroList[mid]:
                    X = SEQ[mid]
                    Y = SEQ[high]
                    print('X:', X, 'Y:', Y)
                    return True
                elif newZ < zeroList[mid]:
                    for i in range(mid):
                        if newZ == zeroList[i]:
                            X = SEQ[i]
                            Y = SEQ[high]
                            print('X:', X, 'Y:', Y)
                            return True
                    else:
                        high -= 1

                elif newZ > zeroList[mid]:
                    low += 1
                else:
                    print('X: Not Found, Y: Not Found')
            # Z <= zeroList[len(zeroList)-1] , if Z smaller than 10 use another search
            else:  # search -> get smaller number first then find larger one.
                high -= 1  # if Z < zeroList[high] reduce high by 1

                newZ = Z - zeroList[low]  # find larger number
                mid = (low+high)//2
                if newZ == zeroList[mid]:
                    X = SEQ[low]
                    Y = SEQ[mid]
                    print('X:', X, 'Y:', Y)
                    return True
                elif newZ < zeroList[mid]:
                    for i in range(mid):
                        if newZ == zeroList[i]:
                            X = SEQ[low]
                            Y = SEQ[i]
                            print('X:', X, 'Y:', Y)
                            return True
                    else:
                        high -= 1

                elif newZ > zeroList[mid]:
                    low += 1
                else:
                    print('X: Not Found, Y: Not Found')

            p += 1
            print('pass:',p)
        else:
            print('X: Not Found, Y: Not Found')

    return False


AdvSearchZero(numbZero, Z)
