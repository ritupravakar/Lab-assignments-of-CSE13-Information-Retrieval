import re
from nltk.tokenize import sent_tokenize, word_tokenize
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

input_str = "Natural language processing (NLP) is a field " + \
            "of computer science, artificial intelligence " + \
            "and computational linguistics concerned with " + \
            "the interactions between computers and human " + \
            "(natural) languages, and, in particular, " + \
            "concerned with programming computers to " + \
            "fruitfully process large natural language " + \
            "corpora. Challenges in natural language " + \
            "processing frequently involve natural " + \
            "language understanding, natural language" + \
            "generation frequently from formal, machine" + \
            "-readable logical forms), connecting language " + \
            "and machine perception, managing human-" + \
            "computer dialog systems, or some combination " + \
            "thereof."
# case
input_str = input_str.lower()
# numbers
result = re.sub(r'\d+', '', input_str)
# punctuations
input_str = input_str.translate(str.maketrans("", "", string.punctuation))
# space
input_str = str(input_str.strip())

# tokenize
# input_str= sent_tokenize(input_str)
input_str = word_tokenize(input_str)

# stop words removal
stop_words = set(stopwords.words('english'))
input_str = [i for i in input_str if not i in stop_words]
#print(input_str)

#stemming

stemmer= PorterStemmer()
for word in input_str:
    print(stemmer.stem(word))