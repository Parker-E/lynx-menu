from lynx import *


def foo():
    print('called foo')


if __name__ == '__main__':
    item1 = MenuItem('empty test 1')
    item2 = MenuItem('empty test 2')
    subMenu1 = Menu(item1, item2)
    item3 = MenuItem('sub menu', subMenu=subMenu1, callback=foo)
    testMenu = Menu(item1, item2, item3, title='Main Menu')
    testMenu.show()
