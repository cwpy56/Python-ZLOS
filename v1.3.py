import math
import tkinter
import time
import random
import turtle
import os
def stone():
    w = "打平"
    e = "电脑赢"
    r = "你赢"
    for i in range(1000):
        import random
        print("石头1，剪刀2，布3")
        a = random.choice(("石头", "剪刀", "布"))
        b = input("请出拳")
        b = int(b)
        if (a == "石头"):
            if (b == 1):
                print(w)
                w = "打平\n"
                r2 = open("win.xinxi", "a")
                r2.write(w)
                r2.close()
            elif (b == 2):
                print(e)
                e = "电脑赢\n"
                p = open("win.xinxi", "a")
                p.write(e)
                p.close()

            elif (b == 3):
                print(r)
                r = "你赢\n"
                q2 = open("win.xinxi", "a")
                q2.write(r)
                q2.close()
            else:
                print("输入错误")
                return 0
        elif (a == "剪刀"):
            if (b == 1):
                print(r)
                r = "你赢\n"
                l2 = open("win.xinxi", "a")
                l2.write(r)
                l2.close()
            elif (b == 2):
                print(w)
                w = "打平\n"
                n2 = open("win.xinxi", "a")
                n2.write(w)
                n2.close()
            elif (b == 3):
                print(e)
                e = "电脑赢\n"
                g2 = open("win.xinxi", "a")
                g2.write(e)
                g2.close()
            else:
                print("输入错误")
                return 0
        elif (a == "布"):
            if (b == 1):
                print(e)
                e = "电脑赢\n"
                u2 = open("win.xinxi", "a")
                u2.write(e)
                u2.close()
            elif (b == 2):
                print(r)

                r = "你赢\n"
                q2 = open("win.xinxi", "a")
                q2.write(r)
                q2.close()
         
            elif (b == 3):
                print(w)
                w = "打平\n"
                y2 = open("win.xinxi", "a")
                y2.write(w)
                y2.close()
            else:
                print("输入错误")
                return 0
def write():
    q2 = open("信息.xinxi", "a")
    xinxi = input("加入信息")
    xin = xinxi +'\n'
    q2.write(xin)
    q2.close()
    print("写入成功")
def read():
    cho = input("请选择: 1.信息 2.石头剪刀布战绩")
    if cho == "1":
        w1 = open("信息.xinxi", "r")
        g = w1.read()
        w1.close()
        print(g)
        return 0
    elif cho == "2":
            try:
                r1 = open("win.xinxi", "r")
                q = r1.read()
                r1.close()
                print(q)
                return 0
            except:
                print("您未进行石头剪刀布游戏")
                return 0 
def jq():
    root = tkinter.Tk()
    root.resizable(width=False, height=False)
    '''hypeparameter'''
    # 是否按下了运算符
    IS_CALC = False
    # 存储数字
    STORAGE = []
    # 显示框最多显示多少个字符
    MAXSHOWLEN = 18
    # 当前显示的数字
    CurrentShow = tkinter.StringVar()
    CurrentShow.set('0')


    '''按下数字键(0-9)'''
    def pressNumber(number):
            global IS_CALC
            if IS_CALC:
                    CurrentShow.set('0')
                    IS_CALC = False
            if CurrentShow.get() == '0':
                    CurrentShow.set(number)
            else:
                    if len(CurrentShow.get()) < MAXSHOWLEN:
                            CurrentShow.set(CurrentShow.get() + number)


    '''按下小数点'''
    def pressDP():
            global IS_CALC
            if IS_CALC:
                    CurrentShow.set('0')
                    IS_CALC = False
            if len(CurrentShow.get().split('.')) == 1:
                    if len(CurrentShow.get()) < MAXSHOWLEN:
                            CurrentShow.set(CurrentShow.get() + '.')


    '''清零'''
    def clearAll():
            global STORAGE
            global IS_CALC
            STORAGE.clear()
            IS_CALC = False
            CurrentShow.set('0')


    '''清除当前显示框内所有数字'''
    def clearCurrent():
            CurrentShow.set('0')


    '''删除显示框内最后一个数字'''
    def delOne():
            global IS_CALC
            if IS_CALC:
                    CurrentShow.set('0')
                    IS_CALC = False
            if CurrentShow.get() != '0':
                    if len(CurrentShow.get()) > 1:
                            CurrentShow.set(CurrentShow.get()[:-1])
                    else:
                            CurrentShow.set('0')
                            
    '''计算答案修正'''
    def modifyResult(result):
            result = str(result)
            if len(result) > MAXSHOWLEN:
                    if len(result.split('.')[0]) > MAXSHOWLEN:
                            result = 'Overflow'
                    else:
                            # 直接舍去不考虑四舍五入问题
                            result = result[:MAXSHOWLEN]
            return result


    '''按下运算符'''
    def pressOperator(operator):
            global STORAGE
            global IS_CALC
            if operator == '+/-':
                    if CurrentShow.get().startswith('-'):
                            CurrentShow.set(CurrentShow.get()[1:])
                    else:
                            CurrentShow.set('-'+CurrentShow.get())
            elif operator == '1/x':
                    try:
                            result = 1 / float(CurrentShow.get())
                    except:
                            result = 'illegal operation'
                    result = modifyResult(result)
                    CurrentShow.set(result)
                    IS_CALC = True
            elif operator == 'sqrt':
                    try:
                            result = math.sqrt(float(CurrentShow.get()))
                    except:
                            result = 'illegal operation'
                    result = modifyResult(result)
                    CurrentShow.set(result)
                    IS_CALC = True
            elif operator == 'MC':
                    STORAGE.clear()
            elif operator == 'MR':
                    if IS_CALC:
                            CurrentShow.set('0')
                    STORAGE.append(CurrentShow.get())
                    expression = ''.join(STORAGE)
                    try:
                            result = eval(expression)
                    except:
                            result = 'illegal operation'
                    result = modifyResult(result)
                    CurrentShow.set(result)
                    IS_CALC = True
            elif operator == 'MS':
                    STORAGE.clear()
                    STORAGE.append(CurrentShow.get())
            elif operator == 'M+':
                    STORAGE.append(CurrentShow.get())
            elif operator == 'M-':
                    if CurrentShow.get().startswith('-'):
                            STORAGE.append(CurrentShow.get())
                    else:
                            STORAGE.append('-' + CurrentShow.get())
            elif operator in ['+', '-', '*', '/', '%']:
                    STORAGE.append(CurrentShow.get())
                    STORAGE.append(operator)
                    IS_CALC = True
            elif operator == '=':
                    if IS_CALC:
                            CurrentShow.set('0')
                    STORAGE.append(CurrentShow.get())
                    expression = ''.join(STORAGE)
                    try:
                            result = eval(expression)
                    # 除以0的情况
                    except:
                            result = 'illegal operation'
                    result = modifyResult(result)
                    CurrentShow.set(result)
                    STORAGE.clear()
                    IS_CALC = True


    '''Demo'''
    def Demo():
            root.minsize(320, 420)
            root.title('Calculator')
            # 布局
            # --文本框
            label = tkinter.Label(root, textvariable=CurrentShow, bg='black', anchor='e', bd=5, fg='white', font=('楷体', 20))
            label.place(x=20, y=50, width=280, height=50)
            # --第一行
            # ----Memory clear
            button1_1 = tkinter.Button(text='MC', bg='#666', bd=2, command=lambda:pressOperator('MC'))
            button1_1.place(x=20, y=110, width=50, height=35)
            # ----Memory read
            button1_2 = tkinter.Button(text='MR', bg='#666', bd=2, command=lambda:pressOperator('MR'))
            button1_2.place(x=77.5, y=110, width=50, height=35)
            # ----Memory save
            button1_3 = tkinter.Button(text='MS', bg='#666', bd=2, command=lambda:pressOperator('MS'))
            button1_3.place(x=135, y=110, width=50, height=35)
            # ----Memory +
            button1_4 = tkinter.Button(text='M+', bg='#666', bd=2, command=lambda:pressOperator('M+'))
            button1_4.place(x=192.5, y=110, width=50, height=35)
            # ----Memory -
            button1_5 = tkinter.Button(text='M-', bg='#666', bd=2, command=lambda:pressOperator('M-'))
            button1_5.place(x=250, y=110, width=50, height=35)
            # --第二行
            # ----删除单个数字
            button2_1 = tkinter.Button(text='del', bg='#666', bd=2, command=lambda:delOne())
            button2_1.place(x=20, y=155, width=50, height=35)
            # ----清除当前显示框内所有数字
            button2_2 = tkinter.Button(text='CE', bg='#666', bd=2, command=lambda:clearCurrent())
            button2_2.place(x=77.5, y=155, width=50, height=35)
            # ----清零(相当于重启)
            button2_3 = tkinter.Button(text='C', bg='#666', bd=2, command=lambda:clearAll())
            button2_3.place(x=135, y=155, width=50, height=35)
            # ----取反
            button2_4 = tkinter.Button(text='+/-', bg='#666', bd=2, command=lambda:pressOperator('+/-'))
            button2_4.place(x=192.5, y=155, width=50, height=35)
            # ----开根号
            button2_5 = tkinter.Button(text='sqrt', bg='#666', bd=2, command=lambda:pressOperator('sqrt'))
            button2_5.place(x=250, y=155, width=50, height=35)
            # --第三行
            # ----7
            button3_1 = tkinter.Button(text='7', bg='#bbbbbb', bd=2, command=lambda:pressNumber('7'))
            button3_1.place(x=20, y=200, width=50, height=35)
            # ----8
            button3_2 = tkinter.Button(text='8', bg='#bbbbbb', bd=2, command=lambda:pressNumber('8'))
            button3_2.place(x=77.5, y=200, width=50, height=35)
            # ----9
            button3_3 = tkinter.Button(text='9', bg='#bbbbbb', bd=2, command=lambda:pressNumber('9'))
            button3_3.place(x=135, y=200, width=50, height=35)
            # ----除
            button3_4 = tkinter.Button(text='/', bg='#708069', bd=2, command=lambda:pressOperator('/'))
            button3_4.place(x=192.5, y=200, width=50, height=35)
            # ----取余
            button3_5 = tkinter.Button(text='%', bg='#708069', bd=2, command=lambda:pressOperator('%'))
            button3_5.place(x=250, y=200, width=50, height=35)
            # --第四行
            # ----4
            button4_1 = tkinter.Button(text='4', bg='#bbbbbb', bd=2, command=lambda:pressNumber('4'))
            button4_1.place(x=20, y=245, width=50, height=35)
            # ----5
            button4_2 = tkinter.Button(text='5', bg='#bbbbbb', bd=2, command=lambda:pressNumber('5'))
            button4_2.place(x=77.5, y=245, width=50, height=35)
            # ----6
            button4_3 = tkinter.Button(text='6', bg='#bbbbbb', bd=2, command=lambda:pressNumber('6'))
            button4_3.place(x=135, y=245, width=50, height=35)
            # ----乘
            button4_4 = tkinter.Button(text='*', bg='#708069', bd=2, command=lambda:pressOperator('*'))
            button4_4.place(x=192.5, y=245, width=50, height=35)
            # ----取导数
            button4_5 = tkinter.Button(text='1/x', bg='#708069', bd=2, command=lambda:pressOperator('1/x'))
            button4_5.place(x=250, y=245, width=50, height=35)
            # --第五行
            # ----3
            button5_1 = tkinter.Button(text='3', bg='#bbbbbb', bd=2, command=lambda:pressNumber('3'))
            button5_1.place(x=20, y=290, width=50, height=35)
            # ----2
            button5_2 = tkinter.Button(text='2', bg='#bbbbbb', bd=2, command=lambda:pressNumber('2'))
            button5_2.place(x=77.5, y=290, width=50, height=35)
            # ----1
            button5_3 = tkinter.Button(text='1', bg='#bbbbbb', bd=2, command=lambda:pressNumber('1'))
            button5_3.place(x=135, y=290, width=50, height=35)
            # ----减
            button5_4 = tkinter.Button(text='-', bg='#708069', bd=2, command=lambda:pressOperator('-'))
            button5_4.place(x=192.5, y=290, width=50, height=35)
            # ----等于
            button5_5 = tkinter.Button(text='=', bg='#708069', bd=2, command=lambda:pressOperator('='))
            button5_5.place(x=250, y=290, width=50, height=80)
            # --第六行
            # ----0
            button6_1 = tkinter.Button(text='0', bg='#bbbbbb', bd=2, command=lambda:pressNumber('0'))
            button6_1.place(x=20, y=335, width=107.5, height=35)
            # ----小数点
            button6_2 = tkinter.Button(text='.', bg='#bbbbbb', bd=2, command=lambda:pressDP())
            button6_2.place(x=135, y=335, width=50, height=35)
            # ----加
            button6_3 = tkinter.Button(text='+', bg='#708069', bd=2, command=lambda:pressOperator('+'))
            button6_3.place(x=192.5, y=335, width=50, height=35)
            root.mainloop()


    if __name__ == '__main__':
            Demo()

def scsuiji():
    min1=int(input('请输入最小值:'))
    max1=int(input('请输入最大值:'))
    r1=random.randint(min1,max1)
    print(r1)
    time.sleep(2)
def csuiji():
    i=1
    s1=random.randint(0,100)
    cs1=int(input('请输入1~100中的一个数字:'))
    while s1!=cs1:
        if s1>cs1:
            print('你第'+str(i)+'次输入的数字小于随机数字')
            cs1=int(input('再试一次吧:'))
        else:
            print('你第'+str(i)+'次输入的数字大于随机数字')
            cs1=int(input('再试一次吧:'))
        i+=1
    print('恭喜你,你第'+str(i)+'次输入的数字与随机数字一样!')
    time.sleep(16)

def clock():
    while True:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        time.sleep(1)
        os.system('cls')
def ZLOSabout():
    print('\n++++++++++++++++++++++')
    print('       ===ZLOS===\n')
    print('by cwpy56 and acwpy Team\n')
    print(' Version : v1.3 Release\n')
    print('++++++++++++++++++++++\n')
    return 0
def start():            
        ZLOS=input('ZLOS 请选择: 1.计算器 2.随机数生成器(原创) 3.猜随机数(原创) 4.时钟 5.exit 6.写入信息 7.读取信息 8.石头剪刀布 9.About')
        global write
        global read
        if ZLOS == str(1):
                jq()
        elif ZLOS == str(2):
                scsuiji()
        elif ZLOS == str(3):
                csuiji()
        elif ZLOS == str(4):
                clock()
        elif ZLOS == str(5):
                exit()
        elif ZLOS == str(6):
                write()
        elif ZLOS == str(7):
                read()
        elif ZLOS == str(8):
                stone()
        elif ZLOS == str(9):
                ZLOSabout()
        else:
                return 0
while True:
        start()