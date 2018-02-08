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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

# def findspam():
#     spams = []
#     senders_call, anwsers_call, _ = makeset(calls)
#     _, _, numbers_text = makeset(texts)
#     for number in senders_call:
#         if number in anwsers_call or number in numbers_text:
#             pass
#         else:
#             spams.append(number)
#     return sorted(spams)
#
#
# def makeset(rowsformcsv):
#     senders = []
#     anwsers = []
#     for row in rowsformcsv:
#         senders.append(row[0])
#         anwsers.append(row[1])
#     return set(senders), set(anwsers), set(senders+anwsers)


# if __name__ == "__main__":
#     spams = findspam()
#     print("These numbers could be telemarketers:")
#     for number in spams:
#         print(number)

#生成器表达式学习过，但是忽略了set是可以运算的，自己实现一下咯
possible_list = [x[0] for x in calls]
impossible_list = [x[1] for x in calls] + sum([[x[0],x[1]] for x in texts],[])
#使用sum把二位数组转为一位数组，学到了，感谢
spams = sorted(set(possible_list) - set(impossible_list))

print('These numbers could be telemarketers:')
for spam in spams:
    print(spam)