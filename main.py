class Inventory:
    inventory = []
    panel = []
    select = []

    def replace(self, cell:int, value):
        cell %= 36
        value %= 65536

        self.inventory[cell].clear()
        self.inventory[cell].append(value)#65536

        print(self.inventory)

    def select_cell_panel(self, cell_panel, cell):
        cell_panel %= 9
        cell %= 36
        print(cell, cell_panel)

        self.panel[cell_panel] = self.inventory[cell]
        # return cell

    def select_cell():
        pass

    def __init__(self):
        self.inventory = [
            [],[],[],[],[],[],[],[],[],
            [],[],[],[],[],[],[],[],[],
            [],[],[],[],[],[],[],[],[],

            [],[],[],[],[],[],[],[],[]
        ]

        self.panel = [[] for x in range(9)]

        # панель в класическом режиме показывает на нижний ряд четвертый
        [[self.select_cell_panel(x, (3*9)+x)] for x in range(9)]
        # self.panel = [self.inventory[((3*9)+x)%36] for x in range(9)]

        # то что мы выбрали в руке
        self.select = self.panel[0]
    def clear(self):
        self.__init__()
    pass


tmp = Inventory()
tmp.replace(27, 4)
print(tmp.select, tmp.panel)
tmp.replace(27, 2)
print(tmp.select, tmp.panel)
