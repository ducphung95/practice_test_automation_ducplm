i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# # for x in "banana":
# #   print(x)

# # fruits = ["apple", "banana", "cherry"]
# # for x in fruits:
# #   if x == "banana":
# #     break
# #   print(x)

# # for x in range(2, 30, 3):
# #     try:
# #         if x % 8 == 0:
# #             raise ValueError(f"Error at {x}")
# #         print(f"Value: {x}")
# #     except Exception as err:
# #         print(err)
# #         break
    
# # print("Continue program")


# # dict_a = {
# #     "a": 1,
# #     "b": 2,
# # }

# # # dict_a["c"]=3
# # dict_a.update({"c": 3}) 
# # print(dict_a)

# # key, value, value_2 = ("a", 1, "c")
# # print(key, value, value_2)
# # for item in dict_a.items():
# #     print(item[0], item[1])

# # day = 4
# # match day:
# #   case 1:
# #     print("Monday")
# #   case 2:
# #     print("Tuesday")
# #   case 3:
# #     print("Wednesday")
# #   case 4:
# #     print("Thursday")
# #   case 5:
# #     print("Friday")
# #   case 6:
# #     print("Saturday")
# #   case 7:
# #     print("Sunday")

# #Thu tu uu tien 'and' truoc moi den 'or'
# # print(bool(1 or 2 and 0))

# # my_set = {1, 2, 3, 4}
# # my_set.remove(1)
# # my_set.remove(7)
# # print(my_set)
# # my_set.add({4, 5, 6})
# # print(my_set)
# # print("Hello{name}".format(name='Bobby')) 

# # x = 2 and None
# # print(type(x))

# # print(4 / 2)

# '''Function'''

# # y = f(x)
# # def my_f(x, y, z, t=0, m=4):
# #     print(x, y, z, t)
# #     if x % 2 == 0:
# #         return x + y + z + m
# #     return x - y - z - t

# # d = my_f(4, 6, 7, m = 5, t = 3)
# # print(d)


# """Dynamic arrgument"""
# # args ~ [x, y, z] => *args ~ x, y, z
# # kwargs ~ {t: 0, m: 1} => **kwargs ~ t=0, m=1

# # def my_f(x, y, *args, m=15, **kwargs):
# #     print(x,  y, m)
# #     print(args[1]) # tuples
# #     print(kwargs['t']) # dict

# # d = my_f(2, 3, 4, 6, 7, m = 5, t = 3)

# """Lamda"""
# # def my_f(x, y, *args, m=15, **kwargs):
# #     x += 1
# #     if x > 10:
# #         return x + y
# #     else:
# #         total = my_f(x, y=m, *args, m=y, **kwargs)
# #         return total
    
# # d = (lambda x, y: my_f(x,y))(5,2)
# # print(d)

# # from copy import deepcopy

# # def my_func(my_dict, my_num):
# #     my_num += 1
# #     my_dict["added_key"] = my_num

# #     return my_dict, my_num

# # my_dict_initial = {"key": 1}
# # my_num_initial = 9

# # my_second_dict = deepcopy(my_dict_initial)

# # my_func(my_dict=my_dict_initial, my_num=my_num_initial)
# # print(my_dict_initial)
# # print(my_num_initial)

# # def my_func(a, b, c=1, d=2):
# #     print(a, b, c, d)
# #     return a+b+c+d

# # my_list = [1, 2]
# # my_dict = {"c:" 3, "d:" 4}

# # result = my_func(my_list)

# '''Class'''

# # class VietnamesePerson:



# #     skin_color = "white"

# #     hair_color = "black"

# #     eye_color = "brown"

# #     country = "VietNam"



# #     def __init__(self, name, age, skin_color, hair_color, eye_color, address=None, country=None):

# #         self.name = name

# #         self.age = age

# #         self.hair_color = hair_color

# #         self.eye_color = eye_color

# #         self.skin_color = skin_color

# #         self.address = address

       

# #         if country:

# #             self.country = country



# #     def speak(self):

# #         print("Hello, I am a person.")



# #     def run(self):

# #         print("I am running")

# #         self.speak()



# #     def hello(self, friend_name):

# #         print(f"Hello {friend_name}, I am {self.name} and I come from {self.country}.")

# #         # self.run()

# #     def summary(self):

# #         print(f"Name: {self.name}, Age: {self.age}")



# # manh = VietnamesePerson(name="Manh", age=22, skin_color="yellow", hair_color="black", eye_color="blue") # instance of VietnamesePerson class

# # vy = VietnamesePerson(name="Vy", age=20, skin_color="white", hair_color="brown", eye_color="black", country="USA")



# # print(Person.hair_color)

# # print(Person.age) --> error vi chua duoc khai bao o class Person

# # print("Manh's INFO:")

# # print("Hair color is " + manh.hair_color)

# # print(str(manh.age) + " years old")

# # print(vy.hair_color)

# # print(vy.age)

# # print(manh.country)

# # print(vy.country)



# # manh.hello("Vy")

# # manh.summary()

# from abc import ABC, abstractmethod

# class Person(ABC):
#     def __init__(self, name, age, gender, occupation, phone_num):
#         self.__name = name
#         self.__age = age
#         self.__gender = gender
#         self.__occupation = occupation
#         self.__phone_num = phone_num

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name
    
#     def set_age(self):
#         return self.__age

#     def set_age(self, age):
#         self.__age = age
    
#     def get_gender(self):
#         return self.__gender

#     def set_gender(self, gender):
#         self.__gender = gender
    
#     def get_occupation(self):
#         return self.__occupation

#     def set_occupation(self, occupation):
#         self.__occupation = occupation

#     def get_phone_num(self):
#         return self.__phone_num

#     def set_phone_num(self, phone_num):
#         self.__phone_num = phone_num

#     @abstractmethod
#     def work(self):
#         pass

#     @abstractmethod
#     def relax(self):
#         pass

#     def describe(self):
#         print(
#             f'''---Profile---
#         Name: {self.__name}
#         Age: {self.__age} years old
#         Gender: {self.__gender}
#         Occupation: {self.__occupation}
#         Marital status: {self.__phone_num}
#         '''
#         )

# class Teacher(Person):
#     def __init__(self, name, age, gender, occupation, phone_num, subject):
#         self.__subject = subject
#         super().__init__(name, age, gender, occupation, phone_num)

#     def get_subject(self):
#         return self.__subject

#     def set_subject(self, subject):
#         self.__subject = subject

#     def work(self):
#         print(f"Teacher {self.get_name()} is teaching {self.__subject}")

#     def relax(self):
#         print(f"Teacher {self.get_name()} is watching Faker's live stream")

# class Doctor(Person):
#     def __init__(self, name, age, gender, occupation, phone_num, specialization):
#         self.__specialization = specialization
#         super().__init__(name, age, gender, occupation, phone_num)

#     def get_specialization(self):
#         return self.__specialization

#     def set_specialization(self, specialization):
#         self.__specialization = specialization

#     def work(self):
#         print(f"Doctor {self.get_name()} is treating patients in the {self.__specialization} field")

#     def relax(self):
#         print(f"Doctor {self.get_name()} is watching the movie 'Doctor Strange in the multiverse of madness'")

# teacher = Teacher("Ba", 30, "Bisexual", "Teacher", "0910000001", "League of Legends")
# doctor = Doctor("Strange", 37, "Male", "Doctor", "0900000000", "Neuroanatomy")

# per_list = [teacher, doctor]
# for person in per_list:
#     person.describe()
#     person.work()
#     person.relax()

# def g(a = "aaa"):
#     return f"hi {a} from {b} !"
# print(g())

# for i in range(3):
#     while i < 2:
#         print(i)

# class A:
#     # x = 3
#     def __init__(self):
#         self.x = 1
# a = A()
# print(a.x)

# c

# b=B()
# b.show()
# a = A()
# print(a.value)

# y = (4, 5)
# x = [1, 2, 3]

# print(y + x)

# try:lass B(A):
#     def __init__(self):
#         super().__init__()
#         self.x += 1   
# b = B()        
# print(b.x) 
#     print(1 / 0)
# except ZeroDivisionError:
#     print("Error")