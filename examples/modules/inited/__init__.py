import collections

print("__init__.py")

def _private():
    print('_private w __init__.py')
    return 'zwrocone przez _private'

x = 55

class A:
    pass

