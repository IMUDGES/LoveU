#-*- coding:utf-8 -*-
import string, random


def rand(n):
    s = random.sample(['1','2','3','4','5','6','7','8','9','0'], n)
    q = ''
    for i in s:
        q = q + i
    return q

