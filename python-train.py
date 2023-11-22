### Program ###
store_list = [1,2,"hello", 3.5]
print (store_list)

sample_dict = {"model": "ford", "brand": "abc", "year": 1984}
print("model is", sample_dict["model"])

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    if x == "banana":
        break


### lamba functions

func = lambda a:a+10
print(func(5))

add_num = lambda a,b,c : a + b + c
print(add_num(5,6,7))