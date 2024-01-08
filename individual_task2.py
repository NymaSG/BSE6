#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_comma(s):
    start_comma = 0
    sentence =""
    first_comma = False
    for i in range(len(s)):
        if s[i] == ',':
            if first_comma == False:
                first_comma = True
                start_comma = i
            else:
                first_comma = False
                sentence += s[start_comma + 1:i] + ";"
                start_comma = 0
    if first_comma == True:
        sentence += s[start_comma + 1:-1]
        start_comma = 0

    return (sentence)

if __name__== "__main__":
    s_1 = "Он пришел домой, снял свою куртку, и сразу пошел в спальню."
    s_2 = "На столе лежала книга, она была открыта на последней странице."

    print (find_comma(s_1))
    print (find_comma(s_2))