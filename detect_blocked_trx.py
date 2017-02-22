# -*- coding: utf-8 -*-
plik = open("printout1.txt") # otwiera plik do odczytu
#linie = plik.readlines() # wczytuje linijki i zwraca listę linijek


if 0:
	for wiersz in linie:
		if "BLO" in wiersz:
			blocked = True
			break
	else:
		blocked = False

if 0:
	blocked = False
	for wiersz in linie:
		if "BLO" in wiersz:
			blocked = True
			break

if 0:
	blocked = False
	for wiersz in plik:
		if "BLO" in wiersz:
			blocked = True
			break

if 1:
	blocked = "BLO" in plik.read()



print "TRX was blocked: {}".format(blocked)

