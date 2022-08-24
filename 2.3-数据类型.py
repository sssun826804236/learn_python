"""
    主要三类数据类型：
    1.字符串类型     string
    2.整型          int
    3.浮点型        float
"""

# 使用type()语句查看数据类型
print(type("sun"),type(666),type(12.13))

# type()返回的结果可以储存
string_type = type("sun")
int_type = type(666)
float_type = type(12.13)
print(type(float_type))
# type()语句也可以查看变量的数据类型
name = "sun"
name_type = type(name)
print(name_type)


