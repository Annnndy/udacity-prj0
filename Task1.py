"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""

# FMT_STR = "There are {0} different telephone numbers in the records."
#
# number_list = []
#
# if len(texts) > 0:
#     for row in texts:
#         number_list.append(row[0])
#         number_list.append(row[1])
# else:
#     print("No texts found")
#
# if len(calls) > 0:
#     for row in calls:
#         number_list.append(row[0])
#         number_list.append(row[1])
# else:
#     print("No calls found")
#
# number_set = set(number_list)
# count = len(number_set)
# print(FMT_STR.format(count))

#set之间的运算这个技巧真的是相见恨晚啊，python没有系统的去学，网上查了一下，这个都是很基础的交、并、补、差运算，汗颜啊。。。

texts_transposed = list(zip(*texts))
calls_transposed = list(zip(*calls))

print("There are {} different telephone numbers in the records.".format(
    len(set(texts_transposed[0]) | set(texts_transposed[1]) |
    set(calls_transposed[0]) | set(calls_transposed[1]))
))
