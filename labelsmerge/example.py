l1= [
                [
                    309.3784249256302,
                    1883.8265226240803
                ],
                [
                    295.6004383904807,
                    1930.1706591514014
                ],
                [
                    298.105526851417,
                    1930.1706591514014
                ],
                [
                    314.38860184750274,
                    1886.3316110850167
                ]
            ]
import math
def GetLineLength(l):
    length=0
    num=len(l1)
    for n in range(num):
        if n < num-1:
            p1=l[n]
            p2=l[n+1]
            c_length = math.pow((p1[0]-p2[0]),2) + math.pow((p1[1]-p2[1]),2)
            length += math.sqrt(c_length)
        elif n == num-1:
            p1=l[0]
            p2=l[n]
            c_length = math.pow((p1[0]-p2[0]),2) + math.pow((p1[1]-p2[1]),2)
            length += math.sqrt(c_length)
    return round(length,1)


print GetLineLength(l1)
