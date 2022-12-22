import random


class User:
    _domain_name = "example.com"
    __value_counter = []


    def __init__(self, name, pwd):
        self.__value_counter.append(name)
        self.__name = name
        self.__pwd = pwd

    def get_email(self):
        return f"{self.__name}@{self._domain_name}"

    @property
    def counter(self):
        return self.__value_counter

    @classmethod
    def reset_counter(cls):
        cls.__value_counter = []

    def reset_counter_instance(self):
        self.__value_counter = []

    @classmethod
    def chane_domaim(cls,new_domain):
        cls._domain_name = new_domain

    @staticmethod
    def _print():
        print("something")




    # def get_name(self):
    #     return self.__name
    #
    # def set_name(self, new_name):
    #     if "@" in new_name:
    #         return False
    #     else:
    #         self.__name = new_name
    #         return True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = f"{value} hhhh  "

    @property
    def pwd(self):
        return self.__pwd

    @pwd.setter
    def pwd(self, value):
        self.pwd = random.randint(1000,100000)





user = User("user", "qwerty")
user.__value_counter = [1,2,3,4,5,6,7,78,5]
user_1 = User("admin", "qwerty123")
print(user.pwd, user.name)

user.chane_domaim("temp.com")

print(user.counter)
print(user._domain_name)

user_1.reset_counter()
user_3 = User("s","d")

print(user.counter)
print(user_1.counter)
print(user.get_email())

user.print()

print(user_1.get_email())