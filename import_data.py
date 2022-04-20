"""
    保存c++代码产生的数据 get_data_list()
    无限信号个数：get_row_num()
    归类好的3个列表：1. get_channel_list()
                   2. get_rssi_list()
                   3. get_available_channel()
    ------------------------------------------------------
    把下面的代码放到循环里
    做到每隔1秒循环一次-->GUI数据每秒刷新1次
"""
import os
import csv


class ImportData():
    # ============================（获取全部数据-放入list）=========================================
    def get_data_list():
        os.system('WIFIScan.exe')

        with open('out.csv', "r", encoding='utf-8') as f:    # open file
            data = [i for i in csv.reader(f, delimiter=',')]    # data_list[0]--就是第一行数据

        return data    # data为list类型
    # ===========================================================================================

    # ======================（获取数据条数）===========================
    def get_row_num(list):    # 传参为get_data_list()方法返回值
        num = len(list) - 1
        return num
    # ==============================================================

    # 归类 channel & rssi 列表
    # =====================================================================
    def get_channel_list(list, int):
        channel = []
        for index in range(int):
            channel.append(list[index][2])
        return channel

    def get_rssi_list(list, int):
        rssi = []
        for index in range(int):
            rssi.append(list[index][3])
        return rssi
    # =====================================================================

    # 获取实际1~13信道占用情况
    # =====================================================================
    def get_available_channel(list):
        available_channel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # int型列表，每个信道占用情况数据
        for i in list:
            t = int(i)
            # print(t)
            for j in range(14):
                if (t - 1) == j:
                    available_channel[t - 1] += 1
        available_channel.insert(0, 'number')
        return available_channel
    # =====================================================================

# data_list = ImportData.get_data_list()    # 获取数据
# row_num = ImportData.get_row_num(data_list)    # 获取数据个数
# channel = ImportData.get_channel_list(data_list, row_num)    # 获取channel列表
# rssi = ImportData.get_rssi_list(data_list, row_num)    # 获取rssi列表
# available_channel = ImportData.get_available_channel(channel)


# print(row_num)
# print(channel)
# print(rssi)
# print(available_channel)
