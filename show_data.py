import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
import import_data as imdata


# 获取数据
# =======================================================================
data_list = imdata.ImportData.get_data_list()    # 全部数据在一个list中
num_row = imdata.ImportData.get_row_num(data_list)    # 数据总数
rssi = imdata.ImportData.get_rssi_list(data_list, num_row)    # rssi
channel = imdata.ImportData.get_channel_list(data_list, num_row)    # 所有信道
available_channel = imdata.ImportData.get_available_channel(channel)    # 1~13信号占用情况

# 为data_list 添加第一列sequence 索引序列
# ---------------------------------------
for i in range(num_row):
    data_list[i].insert(0, i+1)
    # print(data_list[i])
# =======================================================================


# 创建主窗口                                                   tk -> start
# =======================================================================
win = tk.Tk()
win.title("WiFiScan")
# ------------------------------------------
# 获取屏幕宽高
screen_height = win.winfo_screenheight()
screen_width = win.winfo_screenwidth()
item02_width = int(screen_width/7)
item01_width = int(screen_width/14+0.5)
# ============================================================= tm -> end


# 创建3个frme                                                frame -> start
# =======================================================================
# frame1 信道占用情况显示 tree1
frame1 = tk.Frame(win)
frame1.place(x=0, y=0, width=screen_width, height=50)
# ----------------------------------------------------------
# frame2 WIFI具体信息显示 tree2
frame2 = tk.Frame(win)
frame2.place(x=0, y=49, width=screen_width+17, height=220)
# ---------***-frame2 纵向滚动条-*** ---------
scrollBar = tk.Scrollbar(frame2)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
# ----------------------------------------------------------
# frame3 RSSI信号强度 matplotlib图表显示
# *****************************************************
# *                   先空出来！                       **
# *****************************************************
# ========================================================== frame -> end


# 创建 treeview 组件                                                               treeview -> start
# ======================================================================================================================
# 设置 tree1 表头 (13+1 列)
tree1 = ttk.Treeview(frame1, columns=('Channel', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'),
                     show="headings")
# 设置 tree2 表头 (6+1) 列（隐藏纵向滚动条scrollBar）
tree2 = ttk.Treeview(frame2, columns=('序号', 'MAC地址', 'SSID', 'Channel', 'RSSI', '链路质量', 'BssType'),
                     show="headings", yscrollcommand=scrollBar.set)
# -----------------------------------------
# 表格显示(左对齐，纵向填充）
tree1.pack(side=tk.LEFT, fill=tk.Y)
tree2.pack(side=tk.LEFT, fill=tk.Y)
# -----------------------------------------columns
# 定义表头（列）
tree1["columns"] = ("Channel", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
tree2["columns"] = ("序号", "MAC地址", "SSID", "Channel", "RSSI", "链路质量", "BssType")
# -----------------------------------------tree1
# 创建tree1列 (13+1)，列还不显示
tree1.column("Channel", width=item01_width, anchor="center")    # 第一列设置居中显示
tree1.column("1", width=item01_width)
tree1.column("2", width=item01_width)
tree1.column("3", width=item01_width)
tree1.column("4", width=item01_width)
tree1.column("5", width=item01_width)
tree1.column("6", width=item01_width)
tree1.column("7", width=item01_width)
tree1.column("8", width=item01_width)
tree1.column("9", width=item01_width)
tree1.column("10", width=item01_width)
tree1.column("11", width=item01_width)
tree1.column("12", width=item01_width)
tree1.column("13", width=item01_width)
# 设置表头 显示文本
tree1.heading("Channel", text="Channel")
tree1.heading("1", text="1")
tree1.heading("2", text="2")
tree1.heading("3", text="3")
tree1.heading("4", text="4")
tree1.heading("5", text="5")
tree1.heading("6", text="6")
tree1.heading("7", text="7")
tree1.heading("8", text="8")
tree1.heading("9", text="9")
tree1.heading("10", text="10")
tree1.heading("11", text="11")
tree1.heading("12", text="12")
tree1.heading("13", text="13")
# -----------------------------------------tree2
# 创建 tree2 列 (6+1)，列还不显示
tree2.column("序号", width=item02_width)
tree2.column("MAC地址", width=item02_width)     # stretch=True---列宽度随窗体宽度变化而变化
tree2.column("SSID", width=item02_width)
tree2.column("Channel", width=item02_width)
tree2.column("RSSI", width=item02_width)
tree2.column("链路质量", width=item02_width)
tree2.column("BssType", width=item02_width)
# 设置表头 显示文本
tree2.heading("#1", text="seq")  # 这个行数序列可以再添加数据的时候自动生成吗？-----可以用索引吗？？
tree2.heading("#2", text="MAC")
tree2.heading("#3", text="SSID")
tree2.heading("#4", text="Channel")
tree2.heading("#5", text="RSSI")
tree2.heading("#6", text="LinQuality(1~100)")
tree2.heading("#7", text="BssType")
# -------------------------
# Treeview组件与垂直滚动条结合
scrollBar.config(command=tree2.yview)
# ============================================================================== treeview -> end =======================


# treeview 添加数据                                   insert_data -> start
# =======================================================================
# ---------- tree1 ---------
tree1.insert("", 0, text="line1", values=available_channel)
# ---------- tree2 ---------
for row in data_list:
    tree2.insert('', index="end", text="1", values=row)
# ==================================================================  end


win.mainloop()

