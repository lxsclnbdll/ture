# 凯撒密码计算器
def jiami():  # 加密区域

    wenben_1 = input("请输入明文：")
    wenben_2 = wenben_1.lower()
    miwen = list(wenben_2)
    key = int(input("请输入偏移量："))
    a = 0
    while a < len(wenben_2):#保证有文字才输出
        if ord(wenben_2[a]) < 123 - key:
            miwen[a] = chr(ord(wenben_2[a]) + key)
        else:
            miwen[a] = chr(ord(wenben_2[a]) + key - 26)
        a += 1
    print("加密结果为：" + "".join(miwen))


def jiemi():  # 解密区域
    wenben_3 = input("请输入密文;")
    key_1 = int(input("请输入偏移量："))
    wenben_4 = wenben_3.lower()
    mingwen = list(wenben_4)
    b = 0
    while b < len(wenben_4) :
        if ord(wenben_4[b]) >= key_1 + 97 :
            mingwen[b] = chr(ord(wenben_4[b]) - key_1)
        else:
            mingwen[b] = chr(ord(wenben_4[b]) - key_1 + 26)
        b += 1
    print("解密结果为：" + "".join(mingwen))

#读取文件区域
def wenjian():
    while True:
        print(u"1.加密")
        print(u"2.解密")
        print(u"3.结束")
        xuanze_1 = int(input("请输入所选模式:"))
        wjm = input("请输入文件地址：")
        with open(wjm) as file_1:
            file_2 = file_1.read()

        if xuanze_1 == 1:
            file_3 = file_2.lower()
            miwen_1 = list(file_3)
            key_3 = int(input("请输入偏移量："))
            a = 0
            while a < len(file_3):  # 保证有文字才输出
                if ord(file_3[a]) < 123 - key_3:
                    miwen_1[a] = chr(ord(file_3[a]) + key_3)
                else:
                    miwen_1[a] = chr(ord(file_3[a]) + key_3 - 26)
                a += 1
            print("加密结果为：" + "".join(miwen_1))
        elif xuanze_1 == 2:
            key_4 = int(input("请输入偏移量："))
            file_4 = file_2.lower()
            mingwen_1 = list(file_4)
            b = 0
            while b < len(file_4):
                if ord(file_4[b]) >= key_4 + 97:
                    mingwen_1[b] = chr(ord(file_4[b]) - key_4)
                else:
                    mingwen_1[b] = chr(ord(file_4[b]) - key_4 + 26)
                b += 1
            print("解密结果为：" + "".join(mingwen_1))
        elif xuanze_1 == 3 :
            break
        else:
            print("您的输入有误")




# 选择模式（加密/解密/读取文件）区域
while True:
    print("模式:")
    print(u"1.加密")
    print(u"2.解密")
    print(u"3.读取文件")
    xuanze = int(input("请输入所选模式："))
    if xuanze == 1:

        jiami()
    elif xuanze == 2 :

        jiemi()
    elif xuanze == 3 :
        wenjian()
    else:
        print("输入有误")

