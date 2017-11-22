Pseudo projekt, w którym komponenty (pkg1, pkg2) mają podobną strukturę - część drzewa katalogowego się pokrywa


Struktura projektu w katalogu python_wshop/examples/dodatkowe/manipulacja_path
.
├── __init__.py
├── main.py
├── pkg1
│   ├── __init__.py
│   ├── jakisplik.py
│   ├── parsers
│   │   ├── dt.py
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── pkg2
│   ├── exceptions
│   │   └── __init__.py
│   ├── __init__.py
│   ├── parsers
│   │   ├── __init__.py
│   │   └── printouts.py
│   └── utils
│       └── __init__.py
└── readme.txt


widać, że pokrywają się moduły parsers (może wymagać tego jakaś biblioteka,
która sugeruje się strukturą katalogów albo coś).

Następnie, radośnie,w pliku main.py wstawiamy pakiet pkg2 do ścieżki - komu by się chciało
za kazdym razem pisać pkg2.parsers zamiast parsers itp.
Ale potrzebujemy jeszcze zaimportować plik "jakisplik",
bo ktos tam zaimplementował dużo przydatnych dla nas funkcji

Zawartosć pliku main.py
===================================================================
# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, './pkg2/')  # dodajemy, żeby importować bezpośrednio parsers a potem parsery printoutów

from pkg1 import jakisplik
from parsers import printouts # chcemy zaimportować moduł do parsowania różnych
                              # printoutów z pkg2, który przecież dodaliśmy do ścieżki
                              # czyli generalnie zdaje nam się, że będzie działało
===================================================================

i po uruchomieniu tego mamy problem!!!
$python main.py

Traceback (most recent call last):
  File "main.py", line 7, in <module>
    from parsers import printouts # chcemy zaimportować moduł do parsowania różnych
ImportError: cannot import name printouts


Niestety python nie znajduje modułu printouts - a przecież ten moduł jest w pkg2 - który
wcześniej dodalismy do ścieżki - w pakiecie parsers - czyli powinno działać.
I teraz trzeba poszukiwać blędu - przez wiele długich godzin,
nawet nie bardzo wiadomo jak sie za to zabrać.

dopiero przypadkiem, żmudnie debugując z pozoru prosty plik (main.py ma raptem 4 linijki...),
ktoś sprawdził sys.path przy wykonywaniu pliku main.py i zobaczył
(tak sys.path wyglada dopiero po zaimportowaniu modułu jakisplik, przedtem wszystko
wygląda jak powinno - a to dodatkowa trudność):

['./pkg1/', './pkg2/', ...]

i wtedy było jasne, że ktoś radośnie poszedł na skróty - tak samo jak my - i zmodyfikował
ścieżkę dodając pakiet pkg1 do sys.path - nie spodziewał się wtedy, że ktoś dopisze potem
kolejny pakiet (pkg2 powstał później i autor pkg1 nie mógł przewidzieć, że
będzie jeszcze jeden, albo po prostu chciał iść na skróty i być "sprytnym")

Zawartosć pliku jakisplik.py
===================================================================
import sys

sys.path.insert(0, './pkg1/')  # tworca tego pakietu chce sobie "ulatwic zycie"

from parsers import dt
# dalszy kod
===================================================================

i python przeszukiwał pkg1/parsers pod kątem pliku printouts, ale nie znalazł tam takiego pliku.

Dlatego modyfikowanie sys.path jest złym pomysłem, zwłaszcza w złożonych projektach

