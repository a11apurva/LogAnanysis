import os


count=0

files=os.listdir("filtered_xml")

product=dict()
component=dict()

for file_name in files:
    for line in open("filtered_xml//"+file_name):
        line=line.rstrip()
        if "<product>" in line:
            line=line.replace("<product>","")
            line=line.replace("</product>","")

            if line not in product:
                product[line] = 1
            else:
                product[line] += 1
        if "<component>" in line:
            line=line.replace("<component>","")
            line=line.replace("</component>","")

            if line not in component:
                component[line] = 1
            else:
                component[line] += 1

count=0
print "\nProducts :\n"
for key, value in sorted(product.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)
    count+=value
print count

count=0
print "\nProducts :\n"
for key, value in sorted(component.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)
    count+=value
print count
