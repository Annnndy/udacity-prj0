"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
import time
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""


class DicNumberTime:

    def __init__(self, year=2016, month=1, day=1):
        self.FMT_TIME = "%d-%m-%Y %X"
        self.dic_number_time = {}
        self.year = year
        self.month = month
        self.day = day
        self.generatedic()

    def generatedic(self):
        """
        生成一个字典
        """
        if len(calls) > 0:
            for row in calls:
                row_year, row_month, _ = self.parsetime(row[2])
                if row_month == self.month and row_year == self.year:
                    self.updatedic(key=row[0], value=row[3])
                    self.updatedic(key=row[1], value=row[3])
        return None

    def maxtimecalled(self):
        datas = self.sortdict()
        return datas[-1]

    def mintimecalled(self):
        datas = self.sortdict()
        return datas[0]

    def parsetime(self, time_str):
        """
        :param time_str:
        :return: year, month, day
        """
        dt = time.strptime(time_str, self.FMT_TIME)
        return dt.tm_year, dt.tm_mon, dt.tm_mday

    def sortdict(self):
        """
        :return: Type:list, 返回一个按字典value排序的列表
        """
        sorted_dic_list = sorted(self.dic_number_time.items(), key=lambda item: item[1])
        return sorted_dic_list

    def updatedic(self, key, value):
        value = int(value)
        if key in self.dic_number_time.keys():
            self.dic_number_time[key] += value
        else:
            self.dic_number_time[key] = value
        return None


if '__main__' == __name__:
    FMT_STR = "{0} spent the longest time,\
    {1} seconds, on the phone during September 2016"
    dmt = DicNumberTime(year=2016, month=9)
    maxtimecalled = dmt.maxtimecalled()
    print(FMT_STR.format(maxtimecalled[0], maxtimecalled[1]))