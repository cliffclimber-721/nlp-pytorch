class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}가 짖습니다! 멍멍!")
    
    def eat(self):
        print(f"{self.name}의 밥 시간입니다! 멍멍!")
    
    def sanchek_prev():
        print(f"{name}아, 산책 가야지! 멍멍!")
        # self를 안해주면 보이는 def 와 같이 name이 defined 되지 않았다고 뜬다.
        # init을 해놨고 변수 설정을 위에 해뒀으니까 쟤를 고대로 가져다 쓰려면 self 쓰는거라고 이해하려고 한다.
        # 클래스 내에 있는 변수 접근할 때 쓴다!
    
    def sanchek(self):
        print(f"{self.name}아, 산책 가야지! 멍멍!")

# Dog 클래스의 인스턴스 생성
my_dog = Dog(name="레오", age=3)

# 메서드 호출
my_dog.bark()
my_dog.eat()
my_dog.sanchek()