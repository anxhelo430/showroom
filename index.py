print("Hello, World!")
#  komente te shkurtra
'''
komente te gjatë
'''

emriPerson = "John" # string
nr1 = 2 # int
nr2 = 2.2 # float
emriPerson, nr1, nr2 = "John", 2, 2.2
a = b=c =2
print(nr1)
# numrat komplkes: 1+2i
verte = True # boolean
# Lista
list = [1,3,4,"a","test"]
# dictionary
dict = {
      "key1": "value",
}
#tuple
tuple = (1,4,2,"a")

print("test"+str(1))
print(f"test{1}")
print(f"test{nr1}")
nr_1 = "2"
nr_2 = "3"
print(nr_1+nr_2)
print(int(nr_1)+int(nr_2))


# merrInfo = input("Vendos emrin tuaj: ")
# print(f"Pershendetje {merrInfo}.")


# # merrinfo = input("Vendos mbiemrin tuaj: ")
# # print(f"Pershendetje {merrinfo}.")
# # merrinfo = input("Vendos emrin dhe mbiemrin tuaj   : ") 
# # print(f"Pershendetje {merrinfo}.")

var1 = 'Hello, World!'
var2 = "Python Programming"
print(var1)
print(var2[0]) #P
print(var2[3]) #h
print(var2[3:9]) #hon Pr 
print(var2[3:]) #hon Programming
print(var2[:10]) #Python Pro
print("Python\nProgramming")
print("Python\tProgramming")
print("Python\"Programming\"")
print("Python\rProgramming")
# lista
list3=["a", "b", 1, 2, True, "c", "d"]
print(list3)
print(list3[2]) # 1
print(list3[2:5]) # [1, 2, True]
print(list3[2:]) # [1, 2, True, 'c', 'd']
print(list3[:5]) # ['a', 'b', 1, 2, True]
print(list3[-1]) #['d']
list3[2] = 11
print(list3)  
del list3[1]
print(list3)
list3.remove(True)
print(list3)
list3.append("test shto")
print(list3)
print(len(list3)) #6
print(2 in list3)  #true


list4 = ["a", "b", 1, 2, True, "c", "d"]
print(list4)
list5 = ["e", "f", 3, 4, False, "g", "h"]
print(list5)
print(list4 + list5) 
print(len(list4 + list5)) #14

# tuple
tuple1 = ("a", "b", 1, 2, True, "c", "d")
print(tuple1)
print(tuple1[2]) # 1
# tuple1[2] = 11 # error, tuples are immutable
# print(tuple1)
# Dictionary
dict1 = {
    "info1": "test",
    "info2": "new test"
}
print(dict1)
print(dict1["info1"])
print(dict1["info2"])
