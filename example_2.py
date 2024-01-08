#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    word = input("Введите слово: ")

    idx = len(word) // 2
    if len(word) % 2 == 1:
        #Длина слов нечетная
        r = word[:idx] + word [:idx+1:]
    else: 
        #Длина слов четная
        r = word[:idx-1] + word [:idx+1:]

    print(r)