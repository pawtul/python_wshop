"to jest nasz skrypt ktory faktycznie soc robi, a module ma tylko podefiniowane funkcje pomocnicze"

import module
#module.func1()
#module.X

import module as mod
#mod.func1()

from module import X
#X
from module import X as XX
#XX

X = 0
#nastepny import zastapi nam tego X
 
from module import *
# X to 24

