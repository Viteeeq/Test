class Kotik():
    name = ""
    age = 0
    weight = 0
    fluffiness_dgr = ""
    color = ""
    mood = 0
    hunger = 0
    sleep_time = 0
    def __init__(self, newName, age, weight, fluffiness_dgr, color, mood, hunger, sleep_time):
        self.name = newName
        self.animal_class = "Млекопитающее"
        self.age = age
        self.weight = weight
        self.fluffiness_dgr = fluffiness_dgr
        self.color = color
        self.mood = mood
        self.hunger = hunger
        self.sleep_time = sleep_time
        print("Родился новый кот!")
 
    def sharpen_your_claws(self):
        print("Котик как всегда точит свои когти об хозяйский диван, вот негодник.")

    def getAnimalClass(self):
        return self.animal_class

    def feed(self, food):
        if food >= 5:
            self.weight += 1
            print("Вы дали много мяса, кот теперь весит - ", self.weight)

    def purring_sad(self):
        if self.hunger <= 4:
            print(self.name, " истошно мяукнул! Кажется, ", self.name, " голоден!")

    def purring(self):
        if self.mood >=5:
            print(self.name, " мило мякнул:3")
 
    def sudden_tygydyk(self):
        if self.sleep_time >= 6:
            print(self.name, " сделал внезапный тыгыдык!!!")


print("Пример ввода: Имя, Возраст, Вес, Степень пушистости, Раскрас, Настроение(0-10), Степень голода(0-10), Время сна(0-12)")
k = input().split(", ")
myCat = Kotik(k[0], int(k[1]), int(k[2]), int(k[3]) ,k[4], int(k[5]), int(k[6]), int(k[7]))
print("Класс животных к которым этот кот принадлежит - ", myCat.getAnimalClass())
myCat.sudden_tygydyk()
myCat.purring_sad()
myCat.sharpen_your_claws()
print("Сколько кусочков мяска вы хотите дать котику?(0-10)")
myCat.feed(int(input()))
myCat.purring()
