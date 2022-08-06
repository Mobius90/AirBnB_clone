#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
m_model_json = my_model.to_dict()
print(m_model_json)
print("JSON of my_model:")
for k in m_model_json.ks():
    print("\t{}: ({}) - {}".format(k, type(m_model_json[k]), m_model_json[k]))
