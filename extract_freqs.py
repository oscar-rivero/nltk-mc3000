from nltk.corpus import cess_esp, stopwords
from nltk import FreqDist

corpus = [word.lower() for word in cess_esp.words() if word not in stopwords.words("spanish") and word.isalpha()]

fdist = FreqDist(corpus)
mc3000 = fdist.most_common(3000)

finaltxt  = ("\n").join([str(a)+"   "+str(b) for (a,b) in mc3000])

with open("mc3000.txt", "w") as f:
    f.write(finaltxt)