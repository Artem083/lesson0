class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f'{self.number_of_floors}-этажное строение {self.name} / отправимся на {new_floor}-й этаж')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'{new_floor}  - несуществующий этаж')
        else:
            for floor in range(new_floor):
                print(floor + 1)


edelweiss = House('ЖК Эдельвейс', 45)
kuntsevo = House('ЖК Кунцево', 25)

edelweiss.go_to(5)
kuntsevo.go_to(99)