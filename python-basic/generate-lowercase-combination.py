from itertools import product
from string import ascii_lowercase

characterLength = 6
fileName = "wordlistwithlength{}.txt".format(characterLength)
keywords = map("".join, product(ascii_lowercase, repeat=characterLength))

print(keywords)

with open(fileName, "w") as filehandle:
    for listitem in keywords:
        filehandle.write("%s\n" % listitem)

