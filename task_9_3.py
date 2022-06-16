class Worker:
    name = None
    surname = None
    position = None
    bonus = None
    wage = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return self.name + self.surname
    def get_total_income(self):
        self.__income = {'wage': self.wage, 'bonus': self.bonus}
        return self.__income
buh = Position('Viktor ', 'Kuznetsov', 'CEO', 1500, 400)
print(buh.get_full_name(), buh.get_total_income())
