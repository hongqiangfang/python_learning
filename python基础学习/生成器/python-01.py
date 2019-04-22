

def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a
        # print(ret)
        a, b = b, a+b
        current_num += 1


# 如果在调用函数，发现函数有yield，此时是创建一个生成器对象
gen = create_num(10)
next(gen)
print(gen.send("57"))

