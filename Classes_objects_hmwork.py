class House:
    def __init__(self):
        self.numberOfFloors = 10

    def printFloor(self):
        for floor in range(self.numberOfFloors):
            print(f"Текущий этаж равен {floor}")

# Создаем экземпляр класса House
house = House()

# Вызываем метод printFloor
house.printFloor()
