class FirstClass :
    company = "Our Company"
    name = "default"
    password = "default"

    def first_method(self):
        return self.name + "  " +  self.password



if __name__ == "__main__":
   # data = input("name,Password : ")
   data = ("admin,admin123")
   data = data.strip().split(",")

   user = FirstClass()
   user_1 = FirstClass()
   user_1.name = data[0]
   # user.name = data[0]
   user.password = data[-1]

   # user.name = "new-name"

   print(f"{user.name=}, {user.password=}, {user.company=}")

   print(user.first_method())
   print(user_1.first_method())