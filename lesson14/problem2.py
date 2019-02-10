class Car:
    def __init__(self,model,make,speed):
        self.__model = model
        self.__make = make
        self.__speed = speed


    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

def main():

    my_car = Car

    model=input('Enter model of car:')
    make=input('Enter make of car: ')
    speed=0


    my_car=Car(model,make,speed) # the object or instance of a class


    for count in range(5):
        my_car.accelerate()
        print('Current speed: ', my_car.get_speed() )

    for count in range(5):
        my_car.brake()
        print('Curent speed: ', my_car.get_speed())

main()
