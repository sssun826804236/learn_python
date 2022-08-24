"""
    if语句判断
"""
age = 30
if age>= 18 :
    print("你已经成年了")
    print("即将步入大学生活")
print("时间过得真快啊")

"""
if else 语句
"""
age = int(input("请输入你的年龄："))
if age>= 18 :
    print("您已成年，需要买票10元。")
else:
    print("您未成年，可以免费游玩")

"""
    if elif else 语句
"""
# height = int(input("请输入你的身高(cm)："))
# vip_level = int(input("请输入你的VIP等级(1-5)："))
# day = int(input("请告诉我今天几号："))
# if height<120:
#     print("身高小于120cm，可以免费")
# elif vip_level>3:
#     print("VIP级别大于3，可以免费")
# elif day ==1:
#     print("今天是1号免费日，可以免费")
# else:
#     print("需要买票10元")
# print("祝您游玩愉快")

"""
    可以把input放入判断中
"""
if int(input("请输入你的身高(cm)："))<120:
    print("身高小于120cm，可以免费")
elif int(input("请输入你的VIP等级(1-5)："))>3:
    print("VIP级别大于3，可以免费")
elif int(input("请告诉我今天几号：")) ==1:
    print("今天是1号免费日，可以免费")
else:
    print("需要买票10元")
print("祝您游玩愉快")