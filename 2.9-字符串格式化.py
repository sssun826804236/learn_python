"""
    使用格式化字符串来完成拼接
"""

name = "sun"
school = "上海大学"
message = "我叫：%s，在%s上学" %(name,school)
print(message)

# 通过占位方式，完成数字和字符串拼接
class_num = 20
avg_salary = 16781.5
message = "Python大数据学科，北京%d期，平均工资：%.2f"%(class_num,avg_salary)
print(message)

name = "传智播客"
setup_year = 2006
stock_price = 19.99
message = "%s，成立于：%d年，今天的股价是：%.2f"%(name,setup_year,stock_price)
print(message)

"""
    使用辅助符号m.n来控制数据的宽度和精度
    m，控制宽度，要求是数字，很少使用
        例如：%5d 就表示把数字宽度控制在5位，例如11，设置为5d，就会变成：[空格][空格][空格]11
        
    .n，控制小数点精度，要求是数字，会对小数四舍五入
    
        如果有11.345设置为%7.2f的话，结果为：[空格][空格]11.35
"""

num1 = 11
num2 = 11.345
print('数字11宽度限制5，结果是：%5d'%num1)
print('数字11宽度限制1，结果是：%1d'%num1)# 该项目不变化，m比数字本身宽度小，
print('数字11.345宽度限制7，小数精度2，结果是：%7.2f'%num2)
print('数字11不限制宽度，小数精度2，结果是：%.2f'%num2)

"""
    快速字符串格式化的方式
"""

name = "传智播客"
setup_year = 2006
stock_price = 19.99
message = "%s，成立于：%d年，今天的股价是：%.2f"%(name,setup_year,stock_price)
# f:format
print(f"我是{name}，我成立于：{setup_year}年，我今天的股价是：{stock_price}")



