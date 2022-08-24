"""
    布尔类型字面量：
    True    表示真     本质为 1
    False   表示假     本质为 0

    布尔类型可以用计算得到，使用比较运算得到的结果就是布尔类型
"""
bool_1 = True
bool_2 = False

print(f'bool_1变量的内容是：{bool_1}，类型是：{type(bool_1)}')
print(f'bool_2变量的内容是：{bool_2}，类型是：{type(bool_2)}')

"""
    6类比较运算符：
    ==      判断是否相等
    !=      判断是否不相等
    >       判断左侧是否大于右侧
    <       判断左侧是否小于右侧
    >=      判断左侧是否大于等于右侧
    <=      判断左侧是否小于等于右侧
"""
result = 10>5
print(f'10>5的结果是：{result}')


num1 = 10
num2 = 10
print(f'10 == 10 的结果是：{num1 == num2}')

num1 = 10
num2 = 15
print(f'10 == 15 的结果是：{num1 == num2}')

name1 = "sun"
name2 = "Sun"
print(f'sun == Sun 的结果是：{name1 == name2}')

num1 = 5
num2 = 5.2
num2 = int(num2)
print(f'num1 == num2 的结果是：{num1 == num2}')