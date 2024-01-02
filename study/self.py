class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}가 짖습니다! 멍멍!")
    
    def eat(self):
        print(f"{self.name}의 밥 시간입니다! 멍멍!")

# Dog 클래스의 인스턴스 생성
my_dog = Dog(name="뽀삐", age=3)

# 메서드 호출
my_dog.bark()
my_dog.eat()