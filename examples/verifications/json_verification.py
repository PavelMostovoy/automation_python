class InitClass:
    pass


class JsonVerifications(InitClass):

    data = {"first": 1,
            "second": 2}

    user_credentials = {"user_1" :{"login": "password"},
                        "user_2": {"admin": 123}
                        }

    attempts = 5

    # counter_for_add = 0

    def __init__(self, value = False):
        self.text = "initial test"
        self.image = 123456
        self.__counter_for_add = 0
        if value:
            self.data = "ddddd"


    def add_item(self):
        self.__counter_for_add += 1
        self.text = "modified test"
        self.image = [1,2,3,4]


    def get_counter(self):
        return self.__counter_for_add


    def get_text(self):
        return self.text


class Validation(JsonVerifications):

    def __init__(self, value):
        super().__init__(value)
        self.additional_item = 12345
        self.counter_for_add = 0

    def print_method(self):
        print(self.data)

    def add_item(self):
        super().add_item()
        self.counter_for_add += 100
        self.text = "modified test  multy"

