import gensim

file_model="word2vec_tsv_convert.py"
file_text="bigfile_converted_model"

model = gensim.models.doc2vec.Doc2Vec.load(file_model)
#model =gensim.models.Word2Vec.load_word2vec_format(file_model,binary=False)
#model=gensim.models.KeyedVectors.load_word2vec_format(file_model,binary=False)
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
