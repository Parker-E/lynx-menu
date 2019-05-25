import sys
import os


class Menu(object):
    def __init__(self, *items, **kwargs):
        self.items = []
        self.title = kwargs.get('title', '')
        self.header = kwargs.get('header', '')
        for item in items:
            self.add(item)

    def add(self, *items):
        for item in items:
            self.items.append(item)
            if hasattr(item, 'subMenu'):
                self.addParentToChild(item.subMenu)

    def show(self):
        clear()
        if len(self.header):
            self.showHeader()
        if len(self.title):
            self.showTitle()
        for i, item in enumerate(self.items):
            print('[{}] {}'.format(i + 1, item.title))
        self.choice()

    def choice(self):
        while 1:
            try:
                choice = input('> ')
                if choice is 'q':
                    clear()
                    sys.exit()
                if choice is 'b':
                    if hasattr(self, 'parent'):
                        self.parent.show()
                    else:
                        self.show()
                        continue
                if not choice.isdigit():
                    raise ValueError
                item = self.items[int(choice) - 1]
                if hasattr(item, 'callback'):
                    item.callback()
                if hasattr(item, 'subMenu'):
                    item.subMenu.show()
                if not hasattr(item, 'subMenu') and not hasattr(item, 'callback'):
                    print('{} is an empty menu...'.format(item.title))
            except (ValueError, IndexError) as e:
                self.show()
                continue

    def addParentToChild(self, child):
        child.parent = self

    def showTitle(self):
        print(self.title)

    def showHeader(self):
        print(self.header)


class MenuItem(object):
    def __init__(self, title, subMenu=None, callback=None, tag=''):
        self.title = title
        if subMenu is not None:
            self.subMenu = subMenu
            if len(self.title):
                subMenu.title = self.title
        if callback is not None:
            self.callback = callback
        if tag:
            self.tag = tag


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
