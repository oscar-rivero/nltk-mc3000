from nltk.corpus import stopwords

raw = open("5000_lemas.txt", "r")
read = raw.read()

lines = read.split("\n")

tuples = [line.split("\t") for line in lines]

words = [line[0] for line in tuples if line[0] not in stopwords.words("spanish") and line[0].isalpha()]

mc3000 = words[1:3001]
txt = "\n".join(mc3000)


with open("mc3000-CORPES.txt", "w") as f:
     f.write(txt)