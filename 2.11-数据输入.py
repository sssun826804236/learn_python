"""
    使用input()语句来进行输入
"""
# print('告诉我你是谁')
name = input("请告诉我你是谁：")
print(f'我知道了，你是：{name}')

# 输入数字类型
num = input("请输入银行卡密码：")
# 可以发现，input中输入的东西为str类型，如果需要int类型，需要转换
num = int(num)
print(f"你的银行卡密码的类型是：{type(num)}")


