"""
    数据类型之间，在特定场景下，可以相互转换，如字符串转数字，或者数字转字符串
"""

# 三个语句
# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str),num_str)

float_str = str(11.345)
print(type(float_str),float_str)
# 将字符串转换成数字
num1 = int("11")
print(type(num1),num1)

num2 = float("11.345")
print(type(num2),num2)

# num3 = int("sun")# 这个不可以转换

# 整数转浮点数
float_num = float(11)
print(type(float_num),float_num)

# 浮点数转整数
int_num = int(12.925)# 只是去掉小数点后边的数字，不会四舍五入
print(type(int_num),int_num)