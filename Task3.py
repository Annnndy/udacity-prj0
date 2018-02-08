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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
import re

CITYS = {"BGL" : "(080)"}

def findanwsercode(callercode):
    anwsers = {}
    for row in calls:
        if row[0].startswith(callercode):
            code = matchedcode(row[1])
            if code in anwsers.keys():
                anwsers[code] += 1
            else:
                anwsers[code] = 1
    return anwsers


def matchedcode(numberstr):
    tel_match = re.match(r"^\(\d+\)", numberstr)
    cel_match = re.match(r"^[7-9].* *", numberstr)
    sel_match = re.match(r"^140", numberstr)
    if tel_match:
        return tel_match.group()
    elif cel_match:
        return cel_match.group()[0:4]
    elif sel_match:
        return "140"
    else:
        return "ERROR"


if __name__ == "__main__":
    code_total = findanwsercode(CITYS['BGL'])
    print("The numbers called by people in Bangalore have codes:")
    for code in sorted(code_total.keys()):
        if code != "ERROR":
            print(code)

    bgl_total = code_total[CITYS['BGL']]
    all_total = sum(code_total.values())
    rate = float(bgl_total) / all_total * 100
    print("{0:0.2f} percent of calls from fixed lines in Bangalore \
are calls to other fixed lines in Bangalore.".format(rate))
