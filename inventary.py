class Inventory:
    # инвентарь:
    inventory = []

    # 9 указателей на слоты интвентаря:
    panel = []

    # указатель на слот панели, который сейчас в руке:
    select = []

    def replace(self, cell:int, value):
        """
            Вставка id-Обьекта в слот инвентаря
        """
        # слот:
        cell %= 36

        # содержимое для слота:
        value %= 65536

        # очищаем содержимое слота:
        self.inventory[cell].clear()

        # вставляем в слот свое содержимое:
        self.inventory[cell].append(value)

    def select_cell_panel(self, cell_panel, cell):
        # ячейка панели:
        cell_panel %= 9

        # слот:
        cell %= 36

        # привязка выбранного слота к ячейке:
        self.panel[cell_panel] = self.inventory[cell]


    def select_cell(self, cell_panel:int):
        # ячейка панели:
        cell_panel %= 9

        # то что мы выбрали в руке
        self.select = self.panel[cell_panel]

    def __init__(self):
        self.inventory = [
            [ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ],
            [ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ],
            [ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ],

            [ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ]
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
print(tmp.select)
print(tmp.panel)
tmp.replace(27, 2)
print(tmp.select)
print(tmp.panel)
