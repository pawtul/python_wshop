# -*- coding: utf-8 -*-

#old-style class
class A:
	pass


#new style class
class A(object):
	pass


#wszystkie atrybuty sa publiczne, private i protekted to tylko koncepcja
class A(object):
	def __init__(self):
		self.public = 0
		public = 2
		self._protected = 0
		self.__private = 0

	def wyprintuj(self):
		print self.public
		print self._protected
		print self.__private

#ale atrybuty z 2 podkreślnikami z przodu i co najwyżej jednym z tyłu są manglingowane (tzw. name mangling) - ale wewnątrz klasy używamy tego atrybutu normalnie
print dir(A())
# zamiast atrybutu __private mamy _A__private - jest to po to, żeby przypadkiem klasy pochodne nie odwoływały się do tego atrybutu wewnątrz swojego kodu

def connect_to(ip):
	pass


class BSC(object):
	def __init__(self, numer, adres_ip):
		self.numer = numer
		self.adres_ip = adres_ip
	def wypisz_numer(self):
		print self.numer

	def send_command(self, command):
		socket = connect_to(self.adres_ip)
		socket.send(command)
		

bsc110 = BSC(110, "lmbsc110c")
bsc110.numer
bsc110.wypisz_numer()
bsc110.send_command("PCORP:BLOCK=MISSRA;")

#domyślne wartości w metodach
#metoda __init__ inicjalizuje klase ale jej nie tworzy
In [77]: class BSC(object):
    ...:     def __init__(self, apz):
    ...:         self.apz = apz
    ...:     def upgrade_apz(self):
    ...:         self.apz = 55
    ...:         

In [78]: bsc110 = BSC(33)

In [79]: bsc110.apz
Out[79]: 33

In [80]: bsc110.upgrade_apz()

In [81]: bsc110.apz
Out[81]: 55

In [82]: class BSC(object):
    ...:     def __init__(self, apz=33):
    ...:         self.apz = apz
    ...:     def upgrade_apz(self):
    ...:         self.apz = 55
    ...:         

In [83]: 

In [83]: bsc110 = BSC()

In [84]: bsc110.apz
Out[84]: 33

In [85]: bsc110 = BSC(34)

In [86]: bsc110.apz
Out[86]: 34


#konstruktor __new__ tworzy klase, ktora potem bedzie inicjalizowana przez metodę __init__
In [105]: class ConverterCF(object):
     ...:     def __new__(cls, liczba):
     ...:         return 32*liczba + 8
     ...:     

In [106]: ConverterCF(12)
Out[106]: 392
	
#atrybuty sa przechowywane w atrybucie __dict__ obiektu będącego słownikiem

a = A()
print a.__dict__

#i można dodawac nowe atrybuty przez dict
a.__dict__["attr"] = 2
print a.attr

# do dict można wrzucać atrybuty, kßore normalnie wywołałyby błąd

a.__dict__["@2"] = 2
#a.@2 # będzie error
a.__dict__["@2"] # zwróci 2
print a.__dict__ # jest atrybut @2


#ponieważ __dict__ jest zmienialny (bo jest słownikiem) to ma pewnien naddatek, bo musi być przygotowany na dynamiczne dodawanie nowych atrybutów, co  wprzypadku tworzenia wielu instancji tej klasy moze byc kłopotliwe, dlatego można dodać atrybut __slots__ - wtedy klasa moze mieć tylko takie atrybuty jaki podane są w __slots__

class A(object):
	__slots__ = ('a', 'b', 'c')

a = A()
a.a = 12
a.b = 13
a.c = 14
a.d = 15 # error


#definiowanie metod
#metody zawsze przyjmują co najmniej 1 argument - self


#-operatory
In [26]: class BSC(object):
    ...:     def __add__(self, innybsc):
    ...:         print "lacze stpy"
    ...:     def __contains__(self, podsystem):
    ...:         if podsystem == "scxb":
    ...:             return True
    ...:     def __radd__(self, n):
    ...:         return self.__add__(n)
    ...:         
    ...:             

In [27]: bsc110 = BSC()

In [28]: 12 + bsc110
lacze stpy

In [29]: class BSC(object):
    ...:     def __add__(self, innybsc):
    ...:         print "lacze stpy"
    ...:     def __contains__(self, podsystem):
    ...:         if podsystem == "scxb":
    ...:             return True
    ...:     __radd__ = __add__


#kiedy operacja np __add__ zwróci NotImplemented to Python uruchamia odpowiednia metodę w drugiej klasie (np. __radd__ w tej drugiej klasie)



#rzutowanie na string

class A(object):
	def __repr__(self):
		"""
		Zwrocony string jest printowany po wpisaniu nazwy obiektu w konsoli i kliknieciu enter.
		kiedy nie ma metody __str__ to wywoływana jest metoda __repr__
		"""
		return ""
	def __str__(self):
		"""
		Zwracany string jest uzywany przy rzutowaniu na string (str(x)) lub przy printowaniu: print x
		"""
		return ""

# __format__ jest wywoływana kiedy formatujemy string:
# "{}".format(obiekt)
In [392]: class A(object):
     ...:     def __format__(self, fmt=None):
     ...:         print fmt
     ...:         if fmt == "24":
     ...:             raise Exception("24?! :O")
     ...:         return "A"


# __setitem__ pozwala przeciążyć przypisuwanie przypisywanie przy nawiasach kwadratochych

In [405]: class A(object):
     ...:     def __init__(self):
     ...:         self.itemy = {}
     ...:     def __setitem__(self, item, val):
     ...:         if val <=0:
     ...:             val = 1
     ...:         self.itemy[item] = val

In [406]: a = A()

In [407]: a[1] = -10

In [408]: a[2] = 12

In [409]: a.itemy
Out[409]: {1: 1, 2: 12}


# __delattr__, __setattr__, __getattr__, __getattribute__
In [21]: class A(object):
    ...:     def __delattr__(self, attr):
				 """
				 wywolywane kiedy del a.x
                 """
    ...:         print "delattr: {}".format(attr)
    ...:     def __getattr__(self, attr):
    ...:         print "getattr: {}".format(attr)
    ...:     def __setattr__(self, attr, val):
    ...:         print "setattr {}={}".format(attr, val)
    ...:         self.__dict__[attr] = val
    ...:         

In [22]: a = A()

In [23]: a.x
getattr: x

In [24]: a.x = 23
setattr x=23

In [25]: a.x
Out[25]: 23

In [26]: del a.x
delattr: x


# __hash__ - jak definiujemy __hash__ to musimy __eq__

In [59]: class A(object):
    ...:     def __hash__(self):
    ...:         return 2
    ...:     def __eq__(self, other):
    ...:         return True

In [63]: {A(), A()}
Out[63]: {<__main__.A at 0xb4be70ec>, <__main__.A at 0xb4be72ac>}


In [68]: class A(object):
    ...:     def __hash__(self):
    ...:         return 2
    ...:     def __eq__(self, other):
    ...:         return True
    ...:         
    ...:         
    ...:     

In [69]: {A(), A()}
Out[69]: {<__main__.A at 0xb4be5e8c>}



#iterowanie
In [95]: class Iterator(object):
    ...:     def __init__(self):
    ...:         self.index = 0
    ...:     def next(self):
				 """
				 Iterator musi mieć metodę next (__next__ w py3) ktora zwroci kolejny element, który bedzie uznawany za element wyjety z klasy A i wyrzucać StopIteration kiedy iteracja jest konczona - petla for sobie sama przechwyci StopIteration i zakonczy iterację
				 """
    ...:         self.index += 1
    ...:         if self.index > 5:
    ...:             raise StopIteration("Koniec")
    ...:         return 5
    ...:         

In [96]: class A(object):
    ...:     def __iter__(self):
				 """
				 Powinna zwracać iterator (obiekt majacy next/__next__)
				 """
    ...:         return Iterator()
    ...:     

In [97]: 

In [97]: for i in A():
    ...:     print i
    ...:     
5
5
5
5
5

In [98]: 



# atrybuty klas i instancji - atrybuty klas są wspóldzielone przez instancje
     ...:     x = 23
     ...:     y = []
     ...:     z = set()
     ...:     
# tworzy klasę majacą atrybuty instancji: x, y, z

a = A()
id(a.y) == id(A.y) # True

#przykład
In [158]: class BSC(object):
     ...:     log = []
     ...:     def __init__(self, log=None):
     ...:         if log is not None:
     ...:             self.log = log
     ...:     def send_command(self, command):
     ...:         self.log.append(command)
     ...:             

In [159]: 

In [159]: bsc110 = BSC()

In [160]: bsc210 = BSC([])

In [161]: bsc310 = BSC()
In [162]: bsc110.log == bsc110.log
Out[162]: True

In [163]: bsc110.log == bsc310.log == BSC.log
Out[163]: True

In [164]: bsc110.log == bsc210.log
Out[164]: True

In [165]: bsc110.log.append(3)

In [166]: bsc210.log
Out[166]: []

In [167]: A.log = []

In [168]: BSC.log = []

In [169]: bsc110.log
Out[169]: []

In [170]: bsc110.send_command("PCORP=...")

In [171]: BSC.log
Out[171]: ['PCORP=...']

In [172]: bsc310.log
Out[172]: ['PCORP=...']

In [173]: bsc110.log
Out[173]: ['PCORP=...']

In [174]: bsc210.log
Out[174]: []

In [175]: dir(bsc210)
Out[175]: 
['__class__',
 '__delattr__',
 '__dict__',
 '__doc__',
 '__format__',
 '__getattribute__',
 '__hash__',
 '__init__',
 '__module__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'log',
 'send_command']

In [176]: bsc210.__class__
Out[176]: __main__.BSC

In [177]: BSC
Out[177]: __main__.BSC

In [178]: bsc210.__class__()
Out[178]: <__main__.BSC at 0xb4bea2ac>

In [179]: bsc210.__class__
Out[179]: __main__.BSC

In [180]: bsc210.__class__.log
Out[180]: ['PCORP=...']

In [181]: BSC.log
Out[181]: ['PCORP=...']

In [182]: bsc210.__class__.log
Out[182]: ['PCORP=...']

In [183]: bsc210
Out[183]: <__main__.BSC at 0xb4bd570c>

In [184]: bsc210.log
Out[184]: []

In [185]: del bsc210.log

In [186]: bsc210
Out[186]: <__main__.BSC at 0xb4bd570c>

In [187]: bsc210.log
Out[187]: ['PCORP=...']

In [188]: id(bsc210.log) == id()BSC.log
  File "<ipython-input-188-93f44fd78bc6>", line 1
    id(bsc210.log) == id()BSC.log
                            ^
SyntaxError: invalid syntax


In [189]: id(bsc210.log) == id(BSC.log)_
  File "<ipython-input-189-cc2014066cbf>", line 1
    id(bsc210.log) == id(BSC.log)_
                                 ^
SyntaxError: invalid syntax


In [190]: id(bsc210.log) == id(BSC.log)
Out[190]: True

In [191]: del bsc210.log # nie można usuwać atrybutów klasy z poziomu instancji
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-191-7923d652fe24> in <module>()
----> 1 del bsc210.log

AttributeError: log

In [192]: bsc210.send_command("ASDASD")

In [193]: bsc210.log
Out[193]: ['PCORP=...', 'ASDASD']

In [194]: bsc110.log
Out[194]: ['PCORP=...', 'ASDASD']

In [195]: del bsc110.log
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-195-2411d02e60ff> in <module>()
----> 1 del bsc110.log

AttributeError: log

In [196]: del bsc210.log
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-196-7923d652fe24> in <module>()
----> 1 del bsc210.log

AttributeError: log

In [197]: 



#classmethods
In [209]: class BSC(object):
     ...:     log = []
     ...:     def __init__(self, log=None):
     ...:         if log is not None:
     ...:             self.log = log
     ...:     def send_command(self, command):
				  """
				  self to jest instancja - jest dostep do atrybutow instancji, tj. self to <__main__.BSC at 0xb4b6d12c>
				  """
     ...:         self.log.append(command)

     ...:     @classmethod
     ...:     def send_command_global(cls, command):
				  u"""
				  cls jest klasą jaka ma instancja a nie instancją, tj. BSC
				  """
     ...:         print cls
     ...:         cls.log.append(command)
     ...:             

In [210]: bsc110 = BSC([])

In [211]: bsc110.send_command("PCORP")

In [212]: BSC.log
Out[212]: []

In [213]: bsc110.log
Out[213]: ['PCORP']

In [214]: bsc110.send_command_global("PCORR")
<class '__main__.BSC'>

In [215]: bsc110.log
Out[215]: ['PCORP']

In [216]: BSC.log
Out[216]: ['PCORR']

In [217]: 


# deskryptory: implementują __set__, __get__, __delete__
#TODO: sprawdzic czy dobre sygnatury
In [243]: class Desc(object):
     ...:     def __get__(self, inst, owner):
     ...:         print "get"
     ...:     def __set__(self, inst, val):
     ...:         print "set"
     ...:     def __delete__(self):
     ...:         print "del"
     ...:         

In [244]: 

In [244]: class A(object):
     ...:     x = Desc()
     ...:     

In [245]: 

In [245]: a = A()

In [246]: a.x
get

In [247]: a.x = 23
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-247-b5decf1c1ad9> in <module>()
----> 1 a.x = 23

TypeError: __set__() takes exactly 4 arguments (3 given)

In [248]: del a.x
del

In [249]: class Integer(object):
     ...:     def __set__(self, inst, val):
     ...:         if no isinstance(val, int):
  File "<ipython-input-249-01eaf4cd3d58>", line 3
    if no isinstance(val, int):
                   ^
SyntaxError: invalid syntax


In [250]: class Integer(object):
     ...:     def __set__(self, inst, val):
     ...:         if not isinstance(val, int):
     ...:             raise ValueError("blablablabl")
     ...:         

In [251]: class A(object):
     ...:     x = Integer()
     ...:     

In [252]: a = A()

In [253]: a.x  ="asd"
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-253-5a61765b5276> in <module>()
----> 1 a.x  ="asd"

<ipython-input-250-308bb82fdce8> in __set__(self, inst, val)
      2     def __set__(self, inst, val):
      3         if not isinstance(val, int):
----> 4             raise ValueError("blablablabl")
      5 

ValueError: blablablabl

In [254]: a.x  = 23

In [255]:          


#property
In [255]: class A(object):
     ...:     @property
     ...:     def x(self):
     ...:         print "get"
     ...:     @x.setter
     ...:     def x(self, val):
     ...:         if not isinstance(val, int):
     ...:             raise ValueError("asdasd")
     ...:     @x.deleter
     ...:     def x(self):
     ...:         print "delete"
     ...:         

In [256]: dir(A)
Out[256]: 
['__class__',
 '__delattr__',
 '__dict__',
 '__doc__',
 '__format__',
 '__getattribute__',
 '__hash__',
 '__init__',
 '__module__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'x']

In [257]: a = A()

In [258]: dir(a)
Out[258]: 
['__class__',
 '__delattr__',
 '__dict__',
 '__doc__',
 '__format__',
 '__getattribute__',
 '__hash__',
 '__init__',
 '__module__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'x']

In [259]: a.x
get

In [260]: a.x = 23

In [261]: a.x = "23"
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-261-3a61e8c30140> in <module>()
----> 1 a.x = "23"

<ipython-input-255-88b69277579c> in x(self, val)
      6     def x(self, val):
      7         if not isinstance(val, int):
----> 8             raise ValueError("asdasd")
      9     @x.deleter
     10     def x(self):

ValueError: asdasd

In [262]: del a.x
delete

#inny przykłąd
In [272]: class BSC(object):
     ...:     @property
     ...:     def address(self):
     ...:         return self.__dict__["@address"] + ":4444"
				  #alternatywnie może być:
				  #return self._address + ":4444"

     ...:     @address.setter
     ...:     def address(self, val):
     ...:         self.__dict__["@address"] = val
				  #alternatywnie może być:
				  #self._address = val
     ...:     def __init__(self, address):
     ...:         self.address = address
     ...:         

In [273]: 

In [273]: bsc110 = BSC("lmbsc110c")


bsc110.address
"lmbsc110c:4444"

In [274]: dir(bsc110)
Out[274]: 
['@address',
 '__class__',
 '__delattr__',
 '__dict__',
 '__doc__',
 '__format__',
 '__getattribute__',
 '__hash__',
 '__init__',
 '__module__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'address']

In [275]: bsc110.@address
  File "<ipython-input-275-cdec2d638fa7>", line 1
    bsc110.@address
           ^
SyntaxError: invalid syntax


In [276]: bsc110.123address
  File "<ipython-input-276-4050068735a5>", line 1
    bsc110.123address
             ^
SyntaxError: invalid syntax


In [277]: 




#super
In [302]: class A(object):
     ...:     def f(self):
     ...:         print "A"
     ...:         

In [303]: class B(A):
     ...:     def f(self):
     ...:         print "B"
     ...:         #super(B, self).f()
     ...:         

In [304]: b = B()

In [305]: b.f()
B

In [306]: class B(A):
     ...:     def f(self):
     ...:         print "B"
     ...:         super(B, self).f()
     ...:         

In [307]: b = B()

In [308]: b.f()
B
A

In [309]: 


#przykąłd
In [310]: class A(object):
     ...:     def __init__(self):
     ...:         self.x = 23
     ...:         

In [311]: class B(A):
     ...:     def __init__(self):
     ...:         self.y = 24
     ...:         

In [312]: b = B()

In [313]: isinstance(b, A)
Out[313]: True

In [314]: b.x
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-314-4fa97807159e> in <module>()
----> 1 b.x

AttributeError: 'B' object has no attribute 'x'

In [315]: a = A()

In [316]: a.x
Out[316]: 23

In [317]:             


#kolejnosc wywolywnaia super
In [338]: class A(object):
     ...:     def __init__(self, arg):
     ...:         self.arg = arg + 23
     ...:         

In [339]: class B(A):
     ...:     def __init__(self, arg):
     ...:         self.arg = arg
     ...:         

In [340]: b = B("asd")

In [341]: b.arg
Out[341]: 'asd'

In [342]: class B(A):
     ...:     def __init__(self, arg):
     ...:         super(B, self).__init__(arg)
     ...:         self.arg = arg
     ...:         

In [343]: 

In [343]: b = B()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-343-7930f1635390> in <module>()
----> 1 b = B()

TypeError: __init__() takes exactly 2 arguments (1 given)

In [344]: b = B("asd")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-344-533e0f750aa7> in <module>()
----> 1 b = B("asd")

<ipython-input-342-a63049da48cc> in __init__(self, arg)
      1 class B(A):
      2     def __init__(self, arg):
----> 3         super(B, self).__init__(arg)
      4         self.arg = arg
      5 

<ipython-input-338-fe374c619ce3> in __init__(self, arg)
      1 class A(object):
      2     def __init__(self, arg):
----> 3         self.arg = arg + 23
      4 

TypeError: cannot concatenate 'str' and 'int' objects

In [345]: b = B(23)

In [346]: b.arg
Out[346]: 23

In [347]: class B(A):
     ...:     def __init__(self, arg):
     ...:         #super(B, self).__init__(arg)
     ...:         self.arg = arg
     ...:         super(B, self).__init__(arg)
     ...:         
     ...:         

In [348]: b = B(23)

In [349]: b.arg
Out[349]: 46



# mixiny
# Connectable to Mixin - klasa, kótra jest tylko po to, żeby dać kilka metod - oszczędzanie kodu
In [390]: class Connectable(object):
     ...:     def connect(self):
     ...:         print "connecting to: ", self.address
     ...:     def disconnect(self):
     ...:         print "disconnecting from: ", self.address
     ...:         

In [391]: class RemoteDevice(object):
     ...:     def __init__(self, addr):
     ...:         self.address = addr
     ...:         
     ...: 

In [392]: class BSC(Connectable, RemoteDevice):
     ...:     pass
     ...: 

In [393]: class TRC(Connectable, RemoteDevice):
     ...:     pass
     ...: 

In [394]: class MSC(Connectable, RemoteDevice):
     ...:     pass
     ...: 


