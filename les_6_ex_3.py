class Worker:

    def __init__(self, name, surname, position, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):
    def __init__(self, name, surname, position,bonus):
        super().__init__(name, surname, position, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income_wage + self._income_bonus

p = Position('Elena', 'Skalina', 'ECO', "wage" 100000,"bonus" 30000)
print(pos.get_full_name(), pos.get_total_income())
