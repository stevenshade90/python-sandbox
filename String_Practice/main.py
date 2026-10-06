
my_string = "--@--@--@--@"

new_string = my_string.replace("@", "X", 2)
print(new_string)

name = "Steve"

as_list = list(name)

as_list[0] = ""
del as_list[0]
del as_list[0]
print(as_list)

female_name = "xa".join(as_list)
print(female_name.title())

x = "aaa,.bbb,.ccc".split(",.")
print(x)


line = "justarandomlineofwords"
y = line.find("random")
print(y)

print(line.find("random") == 5)


print("Here is my attempt at replacing using Formatting expression %s, and here is a number %d" % (line, len(line)))
print("Here is another formatting method {}".format(line))
print(f"And finally f strings {line}")

line2 = "Here is another line, and formatting placed to be used later %s"
print(line2 % "and here is the later value")

print("{0:100} = {1:^100}".format(line, line))