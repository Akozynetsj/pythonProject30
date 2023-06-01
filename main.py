class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print("Ім'я студента:", self.name)
        print("Вік студента:", self.age)
student1 = Student("HolyMoly", 20)
student1.get_info()
