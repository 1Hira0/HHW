#Write a function in python which accepts a list of  marks of a student and return the minimun mark, maximum mark and the avergae marks. Use this same function to test

def _max(l):
    m = l[0]
    for i in l:
        if i > m:
            m = i
    return m

def _min(l):
    m = l[0]
    for i in l:
        if i < m:
            m = i
    return m

def _avg(l):
    return sum(l) / len(l)

def stats(l):
    return _max(l), _min(l), _avg(l)

print(stats([int(i) for i in input("Enter list of no.: ").split()]))