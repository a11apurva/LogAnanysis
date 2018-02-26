import gensim

sources = ('time_stamp_removed.txt')
documents = gensim.models.doc2vec.TaggedLineDocument(sources)
model = gensim.models.doc2vec.Doc2Vec(dm=0, # DBOW
				size=400, 
				window=8, 
				min_count=5,  
				dbow_words = 1) # DBOW, simultaneously train word vectors with doc vectors

# build model
model.build_vocab(documents)
# train model
#model.train(documents)
model.train(documents, total_examples=model.corpus_count, epochs=model.iter)
# save
model.save('triage_time_stamp_removed')


model = gensim.models.doc2vec.Doc2Vec.load('triage_time_stamp_removed')

st = 'error' # must be in vocab

new_doc_vec = model.infer_vector(st)

print (model.docvecs.most_similar([new_doc_vec]))
