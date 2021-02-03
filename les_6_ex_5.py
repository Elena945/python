class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки {self.title}'


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()