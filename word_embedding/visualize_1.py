from sklearn.manifold import TSNE
import re
import matplotlib.pyplot as plt
import pandas as pd
import gensim

model = gensim.models.doc2vec.Doc2Vec.load('preprocessed')

vocab = list(model.wv.vocab)
X = model[vocab]

tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)

df = pd.DataFrame(X_tsne, index=vocab, columns=['x', 'y'])

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(1, 1, 1)

ax.scatter(df['x'], df['y'])

for word, pos in df.iterrows():
    ax.annotate(word, pos)


