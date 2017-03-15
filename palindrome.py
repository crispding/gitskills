#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
代码功能：
给你一个正整数n， 编程求所有这样的五位和六位十进制回文数，
满足各位数字之和等于n(5<=n<=54)。
按从小到大的顺序输出满足条件的整数。
"""


def pldr(min_digit, max_digit):

    """ 返回一个包含要求位数回文数的list """

    pal_clcts = []
    for num in range(10**(min_digit - 1), 10**max_digit):
        xstr = str(num)
        if xstr == xstr[::-1]:
            pal_clcts.append(num)
    return pal_clcts

def pldr_output(number):

    """ 在屏幕上打印出各位数字之和为要求数值的所有5至6位回文数 """

    pldr_use = pldr(5, 6)
    matched_num = 0
    for num in pldr_use:
        if sum(int(i) for i in str(num)) == number:
            print(num)
            matched_num += 1
    if matched_num == 0:
        print('无匹配项')

def func():

    """ 主函数 """

    num_request = int(input('n = '))
    pldr_output(num_request)


if __name__ == '__main__':
    func()
