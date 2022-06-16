class Stationery:
    art_title = 'title'
    def draw(self, title):
        print('запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('рисование ручкой')
class Pencil(Stationery):
    def draw(self):
        print('рисование карандашом')
class Handle(Stationery):
    def draw(self):
        print('рисование маркером')
my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
