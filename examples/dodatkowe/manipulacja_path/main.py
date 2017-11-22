# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, './pkg2/')  # dodajemy, żeby importować bezpośrednio parsers a potem parsery printoutóœ

from pkg1 import jakisplik
from parsers import printouts # chcemy zaimportować moduł do parsowania różnych
                              # printoutów z pkg2, który przecież dodaliśmy do ścieżki
                              # czyli generalnie zdaje nam się, że będzie działało

