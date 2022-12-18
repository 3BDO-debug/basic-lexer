from variables import *


def detect_keywords(text):
    arr = []
    for word in text:
        if word in lng_keywords:
            arr.append(word)
    return list(set(arr))


def detect_operators(text):
    arr = []
    for word in text:
        if word in lng_operators:
            arr.append(word)
    return list(set(arr))


def detect_delimiters(text):
    arr = []
    for word in text:
        if word in lng_delimiters:
            arr.append(word)
    return list(set(arr))


def detect_num(text):
    arr = []
    for word in text:
        try:
            a = int(word)
            arr.append(word)
        except:
            pass
    return list(set(arr))


def detect_identifiers(text):
    k = detect_keywords(text)
    o = detect_operators(text)
    d = detect_delimiters(text)
    n = detect_num(text)
    not_ident = k + o + d + n
    arr = []
    for word in text:
        if word not in not_ident:
            arr.append(word)
    return arr


def action_starter():
    with open("e1-example.txt") as t:
        text = t.read().split()
        return {
            "keywords": detect_keywords(text),
            "operators": detect_operators(text),
            "delimiters": detect_delimiters(text),
            "identifiers": detect_identifiers(text),
            "numbers": detect_num(text),
        }
