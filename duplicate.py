
user_input  = input("enter the list space seperates ")

ls = user_input.split()

def dup(ls):
    s = set(ls)
    for i in s :
        if ls.count(i) > 1:
            print(i)

dup(ls)
