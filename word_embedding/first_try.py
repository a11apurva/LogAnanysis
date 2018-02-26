import gensim
from gensim.models.deprecated.doc2vec import LabeledSentence
#LabeledSentence=gensim.models.doc2vec.LabeledSentence
from gensim.models.doc2vec import TaggedDocument

from os import listdir
from os.path import isfile, join

docLabels = []
docLabels = [f for f in listdir("training") if f.endswith('.txt')]

data = []
for doc in docLabels:
    f=open('training//'+doc,'r')
    data.append(f.read())
    f.close()


class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
       self.labels_list = labels_list
       self.doc_list = doc_list
    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
            yield LabeledSentence(words=doc.split(),labels=[self.labels_list[idx]])

class DocIterator(object):
    def __init__(self, doc_list, labels_list):
       self.labels_list = labels_list
       self.doc_list = doc_list
    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
            yield LabeledSentence(words=doc.split(),tags=[self.labels_list[idx]])



#it=LabeledLineSentence(data,docLabels)

#it = DocIt.DocIterator(data, docLabels)

it = DocIterator(data, docLabels)

##model = gensim.models.Doc2Vec(size=300, window=10, min_count=5, workers=11,alpha=0.025, min_alpha=0.025) # use fixed learning rate
##model.build_vocab(it)
##for epoch in range(10):
##    #model.train(it,total_examples=model.corpus_count,epochs=model.epochs)
##    #model.total_examples=model.corpus_count
##    #model.epochs=model.epochs
##    model.alpha -= 0.002 # decrease the learning rate
##    model.min_alpha = model.alpha # fix the learning rate, no deca
##    model.train(it)

model = gensim.models.Doc2Vec(alpha=0.025, min_alpha=0.025)  # use fixed learning rate
model.build_vocab(it)
for epoch in range(10):
    #model.train(it)
    model.train(it, total_examples=model.corpus_count, epochs=model.iter)
    model.alpha -= 0.002  # decrease the learning rate
    model.min_alpha = model.alpha
    #model.train(it, total_examples=self.corpus_count, epochs=self.iter)

#model.train(it, total_examples=self.corpus_count, epochs=self.iter)


model.save("doc2vec.model")

#print model.most_similar("documentFileNameInYourDataFolder")





    
