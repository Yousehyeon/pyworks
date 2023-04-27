# Dog 클래스
class Dog:
    kind = "스피츠"
    def __init__(self, name):
        self.name = name # 인스턴스 변수

dog1 = Dog("토리")
print(dog1.name)
print(Dog.kind)

dog2 = Dog("토리2세")
print(dog2.name)
#print(dog2.kind)
print(Dog.kind)