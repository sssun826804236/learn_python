"""
    案例需求：定义一个数字（1~10，随机产生），通过3次判断来猜出来数字
    1.数字随机产生，范围1-10
    2.有三次机会猜数字，通过三层嵌套判断实现
    3.每次猜不中，会提示过大或者过小
"""
import random
num = random.randint(1,10)
# 第一次输入数字
gess_num = int(input("请输入你要猜测的数字："))

if gess_num == num:
    print("恭喜，第一次就猜中了！")
else:
    if gess_num > num :
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")

    # 第二次输入数字
    gess_num = int(input("请输入你要猜测的数字："))
    if gess_num == num:
        print("恭喜，第二次猜中了！")
    else:
        if gess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")

        # 第三次输入数字
        gess_num = int(input("请输入你要猜测的数字："))
        if gess_num == num:
            print("恭喜，第三次猜中了！")
        else:
            if gess_num > num:
                print("你猜测的数字大了")
                print("三次机会用完了，没有猜中")
            else:
                print("你猜测的数字小了")
                print("三次机会用完了，没有猜中")



