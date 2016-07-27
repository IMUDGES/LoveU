import string, random


def rand(n):
    s = random.sample(['1','2','3','4','5','6','7','8','9','0'], n)
    s = s[0] + s[1] + s[2] + s[3] + s[4] + s[5]
    return s
#调用方法，生成n位随机数
# rand(6)

