# Below are the different data types we have in Python
#NUMERIC DATA TYPES; Integers (int), Floating(float) numbers and Complex numbers (complex)
#STRING; which is represented by "str"
#SEQUENCE; Here we have list, tuple, range
#MAPPING; dictionary(dict)
#BOOLEAN; (bool)
#SET and FROZEN SET

#INTEGER VALUES
#These are whole number values
num = 50
print(num, "is of a type", type(num))

#FLOAT VALUES
#These are values with decimal points/ floating points
num2 = 50.5
print(num2, "is of a type", type(num2)) #floats are decimal fractions

#COMPLEX NUMBERS
num6 = 1 + 2j
print(num6, "is of a type", type(num6))

#STRINGS
#values in quotes are treated as strings
name = "Soniah"
print(name, "is of a type", type(name))
num3 ="10000" #in this case 10000 will be treated as a string
print(num3, "is of a type", type(num3))

#TYPE CASTING
#The process of transforming a value from one data type to another
num4 = int(num3) #the computer will the store it as an interger
print(num4, "is of a type", type(num4))
num5 = float(num3) #the computer will the store it as an float
print(num5, "is of a type", type(num5))
#however, the name "Soniah" can not be converted into a float or an integer

#LIST
#these are variables that store more than one value
#A group of values accessed from one memory location, represented by square brackets []
#Other languages may call it an array
languages = ["Luganda", "Lusoga", "Lugwere", "Lugisu", "Lunyankole"]
languages2 = ["Python", "JavaScript", "C++", "PHP", "Jango"] #all these values will be accessed from the same memory location.
print(languages, "is of a type", type(languages))
#to print something from a list
#this can be done by indexing, so the first string in the list, 
# "Luganda" is in index 0 if we are moving from left to right (this is called 'positive indexing')
# "Luganda" is also in index -5 when moving from right to left(this is called 'negative indexing')
print(languages[0])
print(languages[-5])
print(languages2[3])

lang3 = [] #memory stores spaces for variables to be added
#you can have an empty list but you can't have an empty variable e.g. var2 =  (can't leave it blank, it will be an error)

my_stuff = ["lug","runyo","lugwere",["python","javascript","C"]]
print(my_stuff[3][1])
print(my_stuff[-1][-3])
print(my_stuff[3][0])
print(my_stuff[0])
my_stuff.append("spanish")
my_stuff.pop()
print(my_stuff)

#tuples. stores more amounts of data. uses indices to store data characterised by ()
#you can't add to tuples, they're read only and cannot be changed
cars=("ford","nissan","toyota","bmw","lexus")
print(cars[-1])

#dictionary data types are contained in mustache brackets {} eg.
persons={'name':'BiGi','age':20,'origin':'hoima'}
#use your own custom key to store data
print(persons["name"])

#sets like tuples are characterised by (). a set is an unordered collection of elements
fruits={'orange','apple','mangoes','orange','banana','pineapple'}
print(fruits)


