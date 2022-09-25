text = input()

def balanced(text):
    #your code goes here
    stack = [ ]
    optional = [ ]
    for x in text:
    
        if x == "(":
            stack.insert(0,x)
        elif x == ")":
            if len(stack) == 0:
                optional.append(x)
            else:
                stack.pop(0)
            
    print(len(stack) == 0 and len(optional) == 0)
    '''if (len(stack) == 0) and (len(optional) != 0):
        print("False")
    elif :
        print("False")'''
  
balanced(text)
