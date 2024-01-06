x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'}, # index 0
     {'first_name' : 'John', 'last_name' : 'Rosales'}    # index 1
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1. Update Values in Dictionaries and Lists
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"]="Bryant"
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0]="Andres"
print(sports_directory)

# Change the value 20 in z to 30
z[0]["y"]=30
print(z)

# 2. Iterate Through a List of Dictionaries
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
def iterateDictionary(some_list):
    for i in range(len(some_list)):
        print("first_name"+" - "+students[i]["first_name"]+", "+"last_name"+" - "+students[i]["last_name"])

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students) 

# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    print(some_list[key_name])
# Output of First_name
for i in range(len(students)):
    for each_key in students[i]:
         if each_key == "first_name":
             iterateDictionary2(each_key,students[i])
# Output of Last_name
for i in range(len(students)):
    for each_key in students[i]:
         if each_key == "last_name":
             iterateDictionary2(each_key,students[i])

# 4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for each_key in some_dict:
        print(" ")
        print(str(len(some_dict[each_key]))+" "+each_key)
        for i in range(len(some_dict[each_key])):
            print(some_dict[each_key][i])


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)