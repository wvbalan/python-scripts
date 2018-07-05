with open('source') as f:
    lines = f.read().splitlines()
print lines

with open('destination') as d:
    dlines = d.read().splitlines()
print dlines

# "ip access-list 100 extended permit ip" + "lines" + "dlines"

#c=map(lambda x,y : x+y,lines,dlines)

c=["ip access-list 100 extended permit ip " + x + " " +  y for x in lines for y in dlines]
print c
output = open("acl.txt", "w")
for item in c:
   output.write("%s\n" % item)
