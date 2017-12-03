# __name__ = 'kitku'

if __name__ == '__main__':
    print('uruchomiono')

if __name__ == 'kitku':
    print('__name__ to kitku')

print __file__
modname = __file__[:-3]
if __name__ == modname:
    print "imported"
