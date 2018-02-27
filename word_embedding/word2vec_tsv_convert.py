import gensim

file_model="doc2vec.model"
file_text="converted_model"

model = gensim.models.doc2vec.Doc2Vec.load(file_model)
model.save_word2vec_format(file_text+".txt", binary=False)


f=open(file_text+".txt",'r')
g=open(file_text+'_tensors.txt','w')
h=open(file_text+'_tsv_metadata.txt','w')

f.readline()

for line in f:
    line=line.split()
    g.write(("\t".join(line[1:]))+"\n")
    h.write(line[0]+"\n")

f.close()
g.close()
h.close()
