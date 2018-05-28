negatives=set()
for words in open("common_negative_words.txt","r"):
    negatives.add(words.strip())

to_keep=set()
for words in open("computer_terms.txt","r"):
    negatives.add(words.strip())

g=open("no-english-corpus.txt","w")
h=open("no-english-corpus-train.txt","w")
j=open("no-english-removed-words.txt","w")

def isCamel(s):
    return (s != s.lower() and s != s.upper())

removed=set()

count=0

for line in open("component_level_corpus_6_highest_acuracy/corpus_components_6.txt","r"):

    count+=1
    if count == 200:
        print "200"
    
    words=(line.strip()).split()
    label=words[0]
    words=words[1:]

    line=[]
    line2=[]
    
    set1=set()

    for i in range(len(words)):
        if ("_" in words[i]) or (words[i].lower() in to_keep) or (words[i] in to_keep):
            set1.add(i)
        if (words[i].lower() in negatives) or (words[i] in negatives):
            set1.add(i)
            if (i-1 >= 0) :
                set1.add(i-1)
            if (i+1<=(len(words)-1)):
                set1.add(i+1)
        if isCamel(words[i][1:]) :
            set1.add(i)
        
    for i in sorted(set1):
        line.append(words[i])
        
    for i in range(len(words)):
        if i not in set1 :
##            line2.append(words[i])
            removed.add(words[i])

    line=" ".join(line)    
    line = label+" "+line+"\n"
    g.write(line)

##    line2=" ".join(line2)    
##    j.write(line2+"\n")

    if line.strip() != label:
        h.write(line)

for word in sorted(removed):
    j.write(word+"\n")

g.close()
h.close()
j.close()
    
