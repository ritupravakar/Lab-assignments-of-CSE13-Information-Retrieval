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

    def file(i):
        with open("doc" + str(i) + ".txt", 'r') as myfile:
            FILE = myfile.read()
            FILE_PREPROCESS = preprocess(FILE)
            return FILE_PREPROCESS

    document=[]
    for i in range(10):
        document.append({'id':str(i+1),'text':file(str(i+1)).split()})

    words=set()
    database1=dict()
    database2 = dict()

    for i in range(len(document)):
        for j in range(len(document[i]['text'])):
            words.add(document[i]['text'][j])
    words=list(words)

    for i in range(len(words)):
        database2=dict()
        for j in range(len(document)):
            if document[j]['text'].count(words[i]):
                database2[j]=document[j]['text'].count(words[i])
        database1[words[i]]=database2

    #database1 = {words : database2}
    #database2 = {document : count}
    query_count=int(input("Enter no of queries"))
    for i in range(query_count):
        print("\nEnter query")
        query=(input())
        try:
            d=list(database1[query].items())
            for i in range(len(d)):
                print(" Document : "+str(d[i][0])+" Count : "+str(d[i][1]))
        except KeyError:
            print('Value doesn\'t exist !')