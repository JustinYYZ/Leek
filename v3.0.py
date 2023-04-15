import tkinter
import keyboard
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import requests
import time
import matplotlib.pyplot as plt
# import pyqtgraph.widgets.MatplotlibWidget as mw
import numpy as np
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.pyplot import MultipleLocator
import matplotlib.ticker as ticker
from matplotlib.backend_bases import key_press_handler
from PIL import ImageTk, Image
import random
import os
import ctypes

tk = Tk()
tk.title("欢迎使用 我的云钢厂——老韭民的期货量化交易分析软件 v3.0")
tk.geometry("1400x600")
fontStyle = tkFont.Font(size=40)

try:  # >= win 8.1
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:  # win 8.0 or less
    ctypes.windll.user32.SetProcessDPIAware()
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)

up_frame = Frame(tk, width=200, height=400, highlightthickness=1, bd=3)
down_frame = Frame(tk, width=200, height=400, highlightthickness=1, bd=3)
up_frame.grid(row=0, column=0, padx=5, pady=4)
# down_frame.pack(padx=5, pady=5)
down_frame.grid(row=0, column=1, pady=6)

#  输入框1
now_nub10 = Label(up_frame, text="1、请输入螺纹钢期货交易年月：    RB")
now_nub10.grid(row=1, column=1, sticky="W")
now_bok11 = Spinbox(
    up_frame, values=[i for i in range(23, 100)], width=5, wrap=True)
now_bok11.grid(row=1, column=2, sticky="W")
now_bok12 = Spinbox(
    up_frame, values=[i for i in range(1, 13)], width=5, wrap=True)
now_bok12.grid(row=1, column=3, sticky="W")
#  输入框2
now_nub20 = Label(up_frame, text="2、请输入铁矿石期货交易年月：       I")
now_nub20.grid(row=2, column=1, sticky="W")
now_bok21 = Spinbox(
    up_frame, values=[i for i in range(23, 100)], width=5, wrap=True)
now_bok21.grid(row=2, column=2, sticky="W")
now_bok22 = Spinbox(
    up_frame, values=[i for i in range(1, 13)], width=5, wrap=True)
now_bok22.grid(row=2, column=3, sticky="W")
#  输入框3
now_nub30 = Label(up_frame, text="3、请输入 焦  炭 期货交易年月：      J")
now_nub30.grid(row=3, column=1, sticky="W")
now_bok31 = Spinbox(
    up_frame, values=[i for i in range(23, 100)], width=5, wrap=True)
now_bok31.grid(row=3, column=2, sticky="W")
now_bok32 = Spinbox(
    up_frame, values=[i for i in range(1, 13)], width=5, wrap=True)
now_bok32.grid(row=3, column=3, sticky="W")
#  输入框4
now_nub40 = Label(up_frame, text="4、请输入废钢价格（单位：元/吨）：")
now_nub40.grid(row=4, column=1, sticky="W")
now_bok41 = Spinbox(
    up_frame, values=[i for i in range(3000, 9999)], width=5, wrap=True)
now_bok41.grid(row=4, column=2, sticky="W")
#  输入框5
now_nub50 = Label(up_frame, text="5、请输入轧钢成本：")
now_nub50.grid(row=5, column=1, sticky="W")
now_bok51 = Spinbox(
    up_frame, values=[i for i in range(0, 9999)], width=5, wrap=True)
now_bok51.grid(row=5, column=2, sticky="W")
#  输出结果
Output_results = Label(up_frame, text="输出结果：")
Output_results.grid(row=8, column=1, sticky="NW")
# result_data_Text = Text(up_frame, width=50, height=20)  # 处理结果展示
# result_data_Text.grid(row=10, column=0, rowspan=15, columnspan=10)


def get_price(name):  # 获取数据
    headers = {'referer': 'http://finance.sina.com.cn'}
    resp = requests.get('http://hq.sinajs.cn/list=nf_' +
                        name, headers=headers, timeout=6)  # 请求网页+a[i6]
    content1 = resp.text
    l = list(content1.split(','))
    return l[8]


def get_time():  # 获取时间
    r = time.time()
    timeArray = time.localtime(r)
    otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
    print('当前时间：', end='')
    print(otherStyleTime)
    return otherStyleTime


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
now_time = get_time()
dd = ''
for i in now_time[0:10]:
    if i == '/':
        dd = dd + '-'
    else:
        dd = dd + i
if os.path.exists('C:/Leek/') == False:
    os.mkdir('C:/Leek/')
if os.path.exists('C:/Leek/' + dd + '.txt') == False:
    fp = open('C:/Leek/' + dd + '.txt', 'w')
    fp.close()
# f = open('C:/Leek/' + dd + '.txt', 'r', encoding = 'utf-8')
# f1 = f.readlines()
# f1.append('RB' + str(now_bok1.get()) + ', I' + str(now_bok2.get()) + ', J' + str(now_bok3.get()) + '\n')
# f2 = ''
# for i in f1:
#     f2 = f2 + i
# f3 = open('C:/Leek/' + dd + '.txt','w', encoding = 'utf-8', errors = 'ignore')
# f3.write(f2)
# f3.close()
# f.close()


def value():
    li = ['RB' + str(now_bok11.get()) + str(now_bok12.get()).zfill(2), 'I' + str(now_bok21.get()) +
          str(now_bok22.get()).zfill(2), 'J' + str(now_bok31.get()) + str(now_bok32.get()).zfill(2)]
    # print(li)
    # li = ['RB2310', 'I2309', 'J2309']
    # print(li, get_price('J2310'))
    fg = now_bok41.get()
    fg = float(fg)
    zzcb = now_bok51.get()
    zzcb = float(zzcb)
    while True:
        # if keyboard.is_pressed('esc'):
        #     break
        jg = list(map(lambda x: float(get_price(x)), li))
        now_time = get_time()
        s = ''
        s = s + '当前时间：' + now_time + '\n'
        s = s + '螺纹钢价格：' + str(jg[0]) + '\n' + ' 铁矿石价格：' + \
            str(jg[1]) + '\n' + ' 焦炭价格：' + str(jg[2]) + '\n'
        st = (jg[1] * 1.55 + jg[2] * 0.45) / 0.9  # 生铁
        cg = (0.96 * st + 0.15 * fg) / 0.82  # 粗钢
        lljg = round(cg + zzcb, 2)  # 理论价格
        s = s + '螺纹钢理论成本：' + str(lljg) + '\n' + '操作空间：' + \
            str(round(jg[0] - lljg, 2)) + '\n'
        f = open('C:/Leek/' + dd + '.txt', 'r', encoding='utf-8')
        s1 = f.readlines()
        s1.append('RB' + str(now_bok11.get()) + str(now_bok12.get()).zfill(2) + ', I' + str(now_bok21.get()) +
                  str(now_bok22.get()).zfill(2) + ', J' + str(now_bok31.get()) + str(now_bok32.get()).zfill(2) + '\n')
        s1.append(now_time + ', ' + str(jg[0]) + ', ' +
                  str(jg[1]) + ', ' + str(jg[2]) + ', ' + str(lljg) + '\n')
        s2 = ''
        for i in s1:
            s2 = s2 + i
        s3 = open('C:/Leek/' + dd + '.txt', 'w',
                  encoding='utf-8', errors='ignore')
        s3.write(s2)
        s3.close()
        f.close()
        # tt = now_time + ', ' + str(jg[0]) + ', ' + str(jg[1]) + ', ' +  str(jg[2]) + ', ' + str(lljg) + '\n'
        # print(tt)
        ttk.Style().configure('TLabel', width=70, font=('Courier', 15))
        result_data_Text = Label(up_frame, text="%s" % (s), font=fontStyle)
        # result_data_Text = tkFont.Font(size = 10, weight = tkFont.BOLD)
        result_data_Text.grid(row=10, column=0, rowspan=15, columnspan=10)
        t.append(now_time)
        m1.append(jg[0])
        m2.append(lljg)
        if len(t) >= 200:
            del (t[0])
            del (m1[0])
            del (m2[0])
        # plt.clf()
        # plt.plot(t, m1, '-b', label='螺纹钢期货实时价')
        global plot1
        plot1.clear()
        plot1.plot(t, m1, '-b', label='螺纹钢期货实时价')
        # print(t, m1)
        # 实时.set_data(t, m1)
        # plt.plot(t, m2, '-r', label='螺纹钢冶炼成本价')
        plot1.plot(t, m2, '-r', label='螺纹钢冶炼成本价')
        # 成本.set_data(t, m2)
        # print(t, m2)
        # plt.title('螺纹钢实时价格折线图', fontsize=15)
        plot1.set_title('螺纹钢实时价格折线图', fontsize=15)
        # plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(20))
        fig.gca().xaxis.set_major_locator(ticker.MultipleLocator(3))
        # plt.legend(fontsize=15)
        plot1.legend(fontsize=15)
        # plt.xticks(rotation=30, fontsize=15)
        # plot1.set_xticklabels(plot1.get_xticks(), rotation=30, fontsize=15)
        # plt.yticks(fontsize=15)
        # plot1.set_yticks(fontsize=15)
        canvas.draw()
        # plt.show()
        # time.sleep(3)
        canvas.start_event_loop(3)
        # plt
        # break


plt.ion()  # 开启interactive mode 成功的关键函数
plt.rcParams['toolbar'] = 'None'
# fig = plt.figure()#figsize=(0,0))\
fig = Figure(figsize=(5, 4), dpi=100)
plot1 = fig.add_subplot()
# fig.canvas.manager.window.overrideredirect(1)
# a_plt = mw.MatplotlibWidget() # 设置工具栏不可见 a_plt.toolbar.setVisible(False)
# fig.canvas.manager.window.showMinimized(1)
# 把fig放进root
canvas = FigureCanvasTkAgg(fig, master=down_frame)
# 绘图
canvas.draw()
# plt图形导航工具条
toolbar = NavigationToolbar2Tk(canvas, down_frame, pack_toolbar=False)
toolbar.update()
# 显示plt图形导航工具条
canvas.get_tk_widget().pack()
# canvas._tkcanvas.pack()  # side=tkinter.TOP,fill=tkinter.BOTH,expand=1)
# plt.close(fig)
t = []
m1 = []
m2 = []
plot1.tick_params(axis='x', labelrotation=30)
# 实时, = plot1.plot(['2023/04/02 12:59:06'], [114514], '-b', label='螺纹钢期货实时价')
# 成本, = plot1.plot(['2023/04/02 12:59:07'], [191981], '-r', label='螺纹钢冶炼成本价')
# def my_quit():
#     print('my_quit')
# exit()
Submission = Button(up_frame, text="提交", fg="blue",
                    bd=2, width=10, command=value)
Submission.grid(row=6, column=2, sticky="NW")
# b = Button(up_frame, text = '退出', command = tk.quit)
Exit = Button(up_frame, text='退出', fg = 'blue', width = 20, height = 2, command=tk.destroy)
Exit.grid(row=100, column=1, rowspan=15, columnspan=10)
tk.mainloop()
