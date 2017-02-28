#pobieranie inputu od użytkownika:
odp = input("podaj tekst ") # - złą funkcja wykona nam kod
odp = raw_input("podaj tekst ") # miła funkcja która zapisuje odpowiedź jako string

#stdin, stdout, stderr
import sys
sys.stdin # wyglada jak plik
sys.stdout # jw
sys.stderr # jw

#przechwytywanie z ekranu
In [94]: class OutHandler(object):
    ...:     def __init__(self):
				 #metoda init - kazda instancja handlera ma swój własny log - atrybut (commands)
    ...:         self.commands = []
    ...:     def write(self, command):
				#self jest informacją, do której instancji odnosi wię wywołanie tej metody - pod to self wstawimy instancje, dla której wywołujemy metodę
#In [121]: handler = OutHandler() - robienie instancji
#In [122]: handler2 = OutHandler()
#In [123]: handler.write("asd") - tutaj jest wuwołane z 2 zmiennymi, pierwsza (self) to handler  i druda (command) to "asd"
#In [124]: handler2.write("zxc")

				 # metoda, która przyjmuje string jaki był wypisany na ekran i zapisuje sobie ten string do logu
    ...:         self.commands.append(command)
    ...:     def flush(self):
    ...:         pass
    ...:     

In [95]: old_stdout = sys.stdout # zapisujemy sobie stary stdout na zaś

In [96]: handler = OutHandler()

In [97]: sys.stdout = handler  # przypisujemy nasz handler jako stdout - teraz zamiast printowania na ekran będzie szło do naszej klasy (przez metodę write)
In [98]: print "PCORP" # "printujemy", ale tak naprawdę idzie to do naszej klasy (przez metodę write)
In [99]: print "SYREI"
In [100]: print "SYBUP"
In [101]: x = "PCORP" in handler.commands
In [102]: sys.stdout = old_stdout

In [103]: x
Out[103]: True

In [104]: handler.commands
Out[104]: 
[u'\n', # u oznacza unicode
 '',
 'PCORP',
 '\n',
 u'\n',
 '',
 'SYREI',
 '\n',
 u'\n',
 '',
 'SYBUP',
 '\n',
 u'\n',
 '',
 u'\n',
 '']

In [105]: 



#otwieranie plików
open(name[, mode[, buffering]])
#name - nazwa/ścieżka do pliku
#mode - co będziemy robic an pliku: r-odczytywać (domyśkne), w-zapis z nadpisaniem poprzendiego pliku (jak był), a - dopisuje do pliku, b-przyrostek do plików binarnych np rb itp


