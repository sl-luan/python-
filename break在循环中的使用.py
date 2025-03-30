s=0# 储存循环次数
i=1#循环判断值
while i<11:
    s+=i
   # print(s, i)
    if s>20:
        print(i, "累加已经大于20。")
        break
    i=i+1    
    #用户登录系统
i=1    
while i<3:
    name=input("请输入用户名。")
    mima=input("请输入密码。")
    if name=="aaa" and mima=="123456":
        print("登录成功，请稍后。")
        break
    else:    
        if i<2:
            print("用户名登录不正确, 还剩: ", 2-i, "次机会")
            i=i+1
        else: 
            print("三次登录错误。")    
    
    