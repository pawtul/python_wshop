# -*- coding: utf-8 -*-


def trefna_funkcja(arg):
	...
	if cepa_zepusta:
		raise CPError(":(")
	if apega_zepusta:
		raise APGError(":(")
	#tu będzie bład CPError albo APGError
	return

try:
	trefna_funkcja("lmbsc110c")
except:
	print ":( cos nie dziala"


#wersja rozszerzona
try:
	trefna_funkcja("lmbsc110c")
	print "sukces"
except CPError, e:
	print ":( cos nie dziala w CP"
except APGError, e:
	print ":( APGa zepsuta"
except:
	print "zlapie wszystkie pozostale bledy"
else:
	print "wejdzie tutaj, jak zaden wyjatek nie bedzie wyrzucony"
finally:
	print "zawsze sie wykonalo"


#w skrócie:
try:
	#wrażliwy kod
except:
	#obsługa wyjątku
else:
	#obsługa braku wyjatku
finally:
	#to co sie wykona zawsze
