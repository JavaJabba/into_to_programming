#Lab 6 Map/Lambda/List

programming_languages = ('php', 'java', 'python', 'c++', 'c')

# programming_languages = list(map(lambda x:(x.upper()), programming_languages))

# programming_languages = [i.upper() for i in programming_languages]


# for i in programming_languages:
#     i = i.upper()

# print(programming_languages)

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
fruitWithA = [i for i in fruit if fruit[0]=="A"]

print(fruitWithA)