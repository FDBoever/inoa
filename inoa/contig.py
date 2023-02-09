#!/usr/bin/env python

class Contig:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

ctg = Contig('corey','shafer',5000)
print(ctg)


print(ctg.fullname())
print(Contig.fullname(ctg))
