class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")
        

a = Person("홍길동", 20)
print(a.name, a.age)
a.info()
