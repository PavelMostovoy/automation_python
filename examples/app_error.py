
while True:
    user_input = input("fill 1 or 0 : ")
    if user_input == "0":
        print("user fill '0' ")
        try:
            print(foo())
        except Exception as e:
            print(f"Something vent wrong with function with {e}")
        else:
            print("ELSE")

        finally:
            print("After function call ")

    elif user_input == "1":
        print("other")
    elif user_input == "def":
        def foo():
            value = int("234")
            print(f"second {value}")
            return "return"

    elif user_input == "def_1":
        def foo():
            1 / int(user_input)
            print("Third")

    elif user_input == "def_2":
        def foo():
            exit()
            print("Third")

    else:
        exit()
