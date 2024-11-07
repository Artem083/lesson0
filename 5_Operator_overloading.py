class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'{self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):   # 1.
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):   # 2.
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):   # 3.
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):  # 4.
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    # def go_to(self, new_floor):
    #     print(f'{self.number_of_floors}-этажное строение {self.name} / отправимся на {new_floor}-й этаж')
    #     if new_floor < 1 or new_floor > self.number_of_floors:
    #         print(f'{new_floor}  - несуществующий этаж')
    #     else:
    #         for floor in range(new_floor):
    #             print(floor + 1)


kuntsevo = House('ЖК Кунцево', 25)
edelweiss = House('ЖК Эдельвейс', 45)

# edelweiss.go_to(5)
# kuntsevo.go_to(99)

print(kuntsevo)
print(edelweiss)
print(kuntsevo == edelweiss)   #  1.
print(kuntsevo.__add__(20))    #  3.
print(kuntsevo == edelweiss)   #  3.
print(edelweiss.__iadd__(20))  #  4.
print(kuntsevo.__radd__(20))   #  4.
print(kuntsevo > edelweiss)    #  2.
print(kuntsevo >= edelweiss)   #  2.
print(kuntsevo < edelweiss)    #  2.
print(kuntsevo <= edelweiss)   #  2.
print(kuntsevo != edelweiss)   #  2.


# print(len(edelweiss))
# print(len(kuntsevo))