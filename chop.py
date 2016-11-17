f = open("nodes.csv", 'r');
s = "";
for l in f :
  c1 = l.find(',');
  c2 = l.find(',', c1+1);
  if(c2 != -1) :
    s += l[:c2] + '\n';
    print(l);
print(s);
f.close();
fs = open("nodesC.csv", 'w');
fs.write(s);
fs.close();
  