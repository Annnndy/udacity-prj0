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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# FMT_TEXT_STR = "First record of texts, {0} texts {1} at time {2}"
# FMT_CALL_STR = "Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds"
#
# if len(texts) > 0:
#     first_text_record = texts[0]
#     print(FMT_TEXT_STR.format(first_text_record[0],
#                               first_text_record[1],
#                               first_text_record[2]))
# else:
#     print("no records found")


if len(calls) > 0:
    last_call_record = calls[-1]
    incoming_number = last_call_record[0]
    answering_number = last_call_record[1]
    action_time = last_call_record[2]
    during_time = last_call_record[3]
    print(FMT_CALL_STR.format(incoming_number, answering_number, action_time, during_time))
else:
    print("no records found")
