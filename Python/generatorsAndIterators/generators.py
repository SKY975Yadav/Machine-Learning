def my_generator() :
    for i in range(10000):
        yield i+i

gen = my_generator();
for j in gen :
    print(j)