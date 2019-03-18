def preprocess(input_str):
    import re
    from nltk.tokenize import sent_tokenize, word_tokenize
    import string
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize


    input_str = input_str.lower()
    input_str = re.sub(r'\d+', '', input_str)
    input_str = input_str.translate(str.maketrans("", "", string.punctuation))
    input_str = str(input_str.strip())
    input_str = word_tokenize(input_str)
    stop_words = set(stopwords.words('english'))
    input_str = [i for i in input_str if not i in stop_words]

    s = ""
    stemmer = PorterStemmer()
    for word in input_str:
        s += (stemmer.stem(word) + " ")
    return s


if __name__ == '__main__':
    d=[]
    with open("Largetext.txt", 'r') as myfile:
        Largetext = myfile.read()
        Largetext = preprocess(Largetext)
    d.append(Largetext)

    with open("text1.txt", 'r') as myfile:
        text1 = myfile.read()
        text1 = preprocess(text1)
    d.append(text1)

    with open("text2.txt", 'r') as myfile:
        text2 = myfile.read()
        text2 = preprocess(text2)
    d.append(text2)

    with open("text3.txt", 'r') as myfile:
        text3 = myfile.read()
        text3 = preprocess(text3)
    d.append(text3)

    for i in range(len(d)):
        print("AFTER PREPROCESSING : "+str(i+1))
        print(d[i])


