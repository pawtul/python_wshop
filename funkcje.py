# -*- coding: utf-8 -*-
"""
Docstring modułu funkcje.py
"""

def f():
	print "Hello"

f()


# nazwy funkcji sie przykrywają a nie przeciążają 
def f(a, b, c):
	return a + b + c

print f(1, 2, 3)


# argumenty domyślne mają = i wartość
def f(a, b, c=4):
	return a + b + c

print f(1, 2) # równiznaczne print f(1, 2, 4)


#modyfikujemy oryginalny argument póki nie stworzymy nowego i nie przypiszemy do tej zmiennej
x = []

def f(x):
	x = x + [3] # tworzy nowy obiekt lokalny nie modyfikuje oryginału
f(x) # x = []

def f(x):
	x.append(3) # nie tworzymy nowego obiektu więc modyfikowany jest oryginalny przekazany do funkcji
f(x) # x = [3]

#
def append_3(lista=[]):
	lista.append(3) # w przypadku nie podania argumentu modyfikuje zmienna utworzoną w czasie definicji
	return  lista

#obejście powyższego:
def append_3(lista=None):
	if lista is None:
		lista = []
	lista.append(3)


#docstringi
def f():
	"""
	to jest nasz docstring
	"""

print f.__doc__
