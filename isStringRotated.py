'''
clockwise rotation- skilllync, ncskillly- print 1
anticlockwise rotation- skilllync, illlyncsk- print 1
else print 0
'''


def isRotated(s1, s2):
    if len(s1) != len(s2):
        print(0)
        return
    if len(s1) < 2:
        print(0)
        return
    lenstr = len(s2)
    clockwise_rotated_str = ""
    anticlockwise_rotated_str = ""
    clockwise_rotated_str = s2[2:] + s2[0:2]
    anticlockwise_rotated_str = (s2[lenstr - 2:] + s2[0:lenstr - 2])
    print(int(clockwise_rotated_str == s1 or anticlockwise_rotated_str == s1))
    return


str1 = "skilllync"
str2 = "illlyncse"
isRotated(str1, str2)
