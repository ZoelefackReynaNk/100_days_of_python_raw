txt = input()
txtl = txt.split()
y = [ ]
for x in txtl:
    y.append(len(x))
d = 0
for i in range(len(y)):
    if y[i] == max(y):
        d = i
print(txtl[d])
