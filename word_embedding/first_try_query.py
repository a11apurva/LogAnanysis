import gensim

model = gensim.models.doc2vec.Doc2Vec.load('doc2vec.model')


while(1):
    try:
        inp=input("Enter query: ")
        print (model.most_similar(inp))
    except Exception as e:
        pass




    
