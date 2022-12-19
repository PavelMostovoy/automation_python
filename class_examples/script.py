class FirstClass :
    company = "Our Company"
    name = "default"
    password = "default"

    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    def first_method(self, separator):
        return self.__name + f"{separator}" +  self.__password



if __name__ == "__main__":
   # data = input("name,Password : ")
   data = ("admin,admin123")
   data = data.strip().split(",")

   user = FirstClass(data[0], data[1])
   user_1 = FirstClass(data[1],data[0])

   print(user.__name)

   print(f"{user.name=}, {user.password=}, {user.company=}")

   print(user.first_method("        "))
   print(user_1.first_method("________"))

   print(FirstClass.name)