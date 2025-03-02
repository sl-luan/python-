#!/usr/bin/python3
#使用while循环。实现操作登录
i=0
while i<3:
    a=input("请输入用户。")
    b=input("请输入密码。")
#初始化变量

    if a=="abc" and b=="123":
       print("登录成功")
       break
    else:
       print("登录失败。请重新登录。")    
       i=i+1
       print("已锁定")        