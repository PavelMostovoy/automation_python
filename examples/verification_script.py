from verifications.json_verification import JsonVerifications, Validation


instance_data = JsonVerifications(True)

class_data = JsonVerifications


print(instance_data.text)

instance_data.add_item()
instance_data.add_item()
instance_data.add_item()

instance_data.__counter_for_add = 123

instance_data.add_item()


print(instance_data.get_text())


obj = Validation(False)
obj.__counter_for_add = 123
obj.add_item()
print(obj.get_counter())
obj.add_item()
print(obj.image)
obj.image = 1234
print(obj.print_method())