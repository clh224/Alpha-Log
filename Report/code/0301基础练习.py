# count=3 #定义数字等于3
# while count>0:#检测当数值大于0时，执行循环
#     print(f"倒计时：{count}")#f负责把无论是int str float 只要有{}全部强行转为与前面一致的语言
#     count=count-1
# print("发射")
#上面的内容主要学的是while和f的定义和应用
is_correct=False#这里先定义一开始用户就输错
while is_correct==False:#现在执行while
    u_input=input("请输入油价（元/升）:")#用户输入
    # replace('.', '', 1) 是为了处理小数，isdigit() 检查是否为数字
    if u_input.replace('.', '', 1).isdigit():#因为只有这样，我们才能既允许用户输入小数，又能挡住用户输入汉字 说白了就是骗这个isdigit
        price=float(u_input)#当与用户只输入数字时
        is_correct=True#通过
    else:print("错误：请输入纯数字（例如 7.5），不要带汉字或单位！")#否则继续问用户
print(f"录入成功！当前油价为：{price}")
#简单笔记 首先要知道while的判定这个函数和循环 然后知道可以主动查找用户错误
#用replace 见11行 old是旧的内容 new是变成新内容 count执行几次 然后isdigit用来判断是否为数
#如果不是那就到else 否则就成功
