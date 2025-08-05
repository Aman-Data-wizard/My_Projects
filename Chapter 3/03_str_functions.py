name ="harry"

print(len(name))
print(name.endswith("rry"))

print(name.startswith("ha"))

count = name.count("r")
print(count)

print(name.capitalize())

index = name.find("y")
print(index)

#string replace (old word, new word)
str = "Rabiol"
replaced_string = str.replace("l","t")
print(replaced_string)