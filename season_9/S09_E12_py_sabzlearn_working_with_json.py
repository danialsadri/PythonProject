from json import load, loads, dump, dumps
# ------------------------------------------------------------------------
# loads ==> json string to python type --> deserializers / pars
# load  ==> json file to python type
# dumps ==> python type to json string --> serializers
# dump  ==> python type to json file
# ------------------------------------------------------------------------


# ------------------ json string to python type----------------------------
# json_str = '{"name": "ali", "family": "sadri"}'
# python_type = loads(json_str)
#
# print(json_str, type(json_str))
# print(python_type, type(python_type))
# ------------------------------------------------------------------------


# ------------------ json file to python type ----------------------------
# with open(file='package.json', mode='rt') as json_file:
#     s = load(json_file)
# print(s, type(s))
# ------------------------------------------------------------------------


# ------------------ python type to json string ----------------------------
# dict_python = {'name': 'ali', 'family': 'akbari'}
# json_str = dumps(dict_python)
#
# print(dict_python, type(dict_python))
# print(json_str, type(json_str))
# ------------------------------------------------------------------------


# ------------------ python type to json file ----------------------------
# dict_python = {"name": "danial",
#                "lastname": "sadri",
#                "age": 17,
#                "marks": {"riazi": [12, 15, 18], 'fizik': [19, 20, 14]},
#                "lessons": ['honar', 'fizik']
#                }
#
# with open(file='package.json', mode='wt') as json_file:
#     dump(dict_python, json_file, indent=4, sort_keys=True, separators=(',', ':'))
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
#  چجوری همه اینارو با استفاده از متد dump بنویسم داخل فایل جیسونی

# name = "danial"
# age = 17
# marks = {"riazi": [12, 15, 18], 'fizik': [19, 20, 14]}
# lessons = ['honar', 'fizik']
# b = True
# family = 'mohammadi'
#
#
# dict_python = {"name": name, "age": age, "marks": marks, "lessons": lessons, "family": family, "b": b}
#
#
# with open(file='package.json', mode='wt') as json_file:
#     dump(dict_python, json_file, indent=4)
# ------------------------------------------------------------------------
#  چجوری همه اینارو از فایل جیسونی بخونم


# with open(file='package.json', mode='rt') as json_file:
#     p = load(json_file)
#
#
# name = p['name']
# age = p['age']
# marks = p['marks']
# lessons = p['lessons']
# family = p['family']
# b = p['b']
#
# print(f"{name}\n{age}\n{marks}\n{lessons}\n{family}\n{b}")
# ------------------------------------------------------------------------
