# -*- coding: utf-8 -*-

#dekorator to funkcja która przyjmuje inną funkcje i zwraca nową funkcję

def dekorator(funkcja):
	def nowa_funkcja(*args, **kwargs):
		print args, kwargs
		return funkcja(*args, **kwargs)
	return nowa_funkcja

#dekorowanie
funkcja = dekorator(oryginalna_funkcja)

@dekorator
def oryginalna_funkcja(*args, **kwargs):
	pass

#powyższe skutkuje tym, że do zmiennej oryginalna_funkcja zostanie przypisany obiekt zwrócony przed dekorator (w tym przypadku będzie to nowa_funkcja)

def dekorator(funkcja):
	return 2

@dekorator
def f():
	pass

# ponieważ do zmiennej f bedzie przypisane to co zostało zwrócone przez dekorator, to w tym przypadku f beðzie miało wartosć 2

