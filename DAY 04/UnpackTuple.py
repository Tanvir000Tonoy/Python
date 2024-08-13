sex = ("male", "male", "female", "lasbian", "shemale")
(tanvir, shimul, *sinthia) = sex
print(f"Tanvir is {tanvir}, Shimul is {shimul}, Sinthia is {sinthia[0]}")

for s in sex:
    print(s)
print(sex.count("male"))

print(sex.index("lasbian"))