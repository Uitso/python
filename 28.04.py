import random

class Student:
    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.hunger = 100
        self.progress = 0
        self.money = 500
        self.alive = True
    def to_study(self):
        print('Time to study')
        self.hunger -= 10
        self.progress += 0.12
        self.gladness -= 3
    def to_sleep(self):
        print("I will sleep")
        self.hunger -= 10
        self.gladness += 3
    def to_chill(self):
        print('Rest time')
        self.hunger += 30
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 40
    def to_job(self):
        print('Time to work')
        self.hunger -= 20
        self.progress -= 0.05
        self.gladness -= 5
        self.money += 150
    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression')
            self.alive = False
        elif self.progress > 5:
            print('Passed externally')
            self.alive = False
        elif self.hunger <= 0:
            print('Starving')
            self.alive = False
    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress, 2)}')
        print(f'Hunger = {self.hunger}')
        print(f'Money = {self.money}')

    def live(self, day):
        day = ' Day ' + str(day) + ' of ' + self.name + ' live '
        print(f'{day:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            if self.money < 40:
                nick.to_job()
            else:
                self.to_chill()
        self.end_of_day()
        self.is_alive()




nick = Student(name='Nick')

for day in range(366):
    if nick.hunger < 30 or nick.gladness < 10:
        nick.to_chill()
    if nick.progress < 0:
        nick.to_study()
    if nick.alive == False:
        break
    nick.live(day)



