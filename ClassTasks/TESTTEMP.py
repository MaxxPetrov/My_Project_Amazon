temp_string = [32,3423, "fdf", "sff", 32, "23r", "fdf"]
print(temp_string[3])

temp_set = set(temp_string)

print(temp_set)
sec_list = list(temp_set)
print(sec_list[3])

temp_tumple = (3,4.5,64)

temp_list = list(temp_tumple)
temp_list.append(12121)
print(tuple(temp_list))

d = dict()
dd = {["key1", 34, "key2", {"dfg": 324234}]:{23,423,434}, 123:{"fdf": "dfgf"}}
