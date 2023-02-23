with open("test_example.html", "rb") as f:
    data = f.read()

data = str(data)
parsed_data = data.split("<")
new_data = []
for element in parsed_data:
    new_data.append(element.strip(" >n\\r"))

new_list = []
for i, element in enumerate (new_data):
    if 'please use the code:' in element:
        new_list.append(element.split())
        print(i, element)



print(new_list)