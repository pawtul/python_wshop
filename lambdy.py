# -*- coding: utf-8 -*-
# lambdy

#definicja
g = lambda c=12: c

#alternatywnie
def g(c=12):
	return c

print g(14)


map(lambda x: x**2, [1,2,3,4,5])



#wywoływanie kilku funkcji w lambdaie
def f(x):
	print x


map(lambda x: f(x) or x**2, [1,2,3,4,5])


# TODO: dodac opis
def kw(x):
	return x**2

x = 1
if kw(x): # wiejdzie bo kw(x) <> 0
	print "weszlo"

#tożsame z:
x = 1
wynik = kw(x)
if wynik:
	print "weszlo"



#kwargs i args

