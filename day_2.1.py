file = open("/usercode/files/books.txt", "r")

#your code goes here
bl = file.readlines()
code1 = [ ]
code2 = [ ]
code3 = [ ]
for text in bl:
    if text != ' ' and text != bl[len(bl)-1]:
        code1.append(len(text)-1)
        code2.append(text[0])
    elif text == bl[len(bl)-1]:
        code1.append(len(text))
        code2.append(text[0])
        
for i in range(len(code1)):
    d = code2[i] + str(code1[i])
    code3.append(d)
    
for code in code3:
    print(code)
    
file.close()
