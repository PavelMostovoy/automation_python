class FirstClass() :
    company = "Our Company"
    name = "default"
    password = "default"

    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    def method_1(self):
        self.first_method(self.name)


    @classmethod
    def first_method(cls, separator):
        return cls.name + f"{separator}" + cls.password



if __name__ == "__main__":
   # data = input("name,Password : ")
   data = ("admin,admin123")
   data = data.strip().split(",")

   user = FirstClass(data[0], data[1])
   user_1 = FirstClass(data[1],data[0])

   # print(user.__name)

   print(f"{user.name=}, {user.password=}, {user.company=}")
   user.method_1()
   print(user.first_method("        "))
   print(user_1.first_method("________"))

   print(FirstClass.name)