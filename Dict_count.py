text = input()
def add_dic(txt):
    dict = {}
    for i in txt:
      dict[i] = txt.count(i)
    print(dict)
add_dic(text)
