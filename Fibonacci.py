num = int(input())


def fibonacci(n):
	
    if n<=1:
        return 0;
    else:
        a, b = 0, 1     
        for i in range(n):
            print(a)
            a, b = b, b + a

fibonacci(num)
