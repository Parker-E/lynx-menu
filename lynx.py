import sys


class Menu(object):
    def __init__(self, *items, **kwargs):
        self.items = []
        for item in items:
            self.add(item)

    def add(self, item):
        self.items.append(item)
        if hasattr(item, 'subMenu'):
            self.addParentToChild(item.subMenu)

    def show(self):
        for i, item in enumerate(self.items):
            print('[{}] {}'.format(i + 1, item.title))
        self.choice()

    def choice(self):
        while 1:
            try:
                choice = input('> ')
                if choice is 'q':
                    sys.exit()
                if choice is 'b':
                    self.parent.show()
                item = self.items[int(choice) - 1]
                if hasattr(item, 'callback'):
                    item.callback()
                if hasattr(item, 'subMenu'):
                    item.subMenu.show()
            except (ValueError, IndexError) as e:
                    print('Invalid menu item. Try using the options listed')
                    continue

    def addParentToChild(self, child):
        child.parent = self
        pass


class MenuItem(object):
    def __init__(self, title, subMenu=None, callback=None):
        self.title = title
        if subMenu is not None:
            self.subMenu = subMenu
        if callback is not None:
            self.callback = callback
