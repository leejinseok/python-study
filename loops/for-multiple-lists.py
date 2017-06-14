list_a= [1,2,3]
list_b= [4,5,6]

for a,b in zip(list_a, list_b):
    if a>b:
        print a
    else:
        print b
