# author: dg1245
# e-mail: dg1245@qq.com
# start-date: 2023-11-11
# python-version: 3.12
# 协助：豆包 https://www.doubao.com/chat/

# 使用说明
# 先去亚马逊后台->Brands->Brand Analytics -> Search Analytics->
# ->Top Search Terms->Generate Report->Download Manager->下载csv
# 第21行代码填入wanted_word，运行代码即可
# result文件夹里会生成2个包含word_count和keyword_rank的csv文件

import os
import csv
from collections import Counter
import datetime
import sys
import time

# 填入一次，包含该词的关键词都会统计
wanted_word = "dogs"
wanted_word = wanted_word.lower()
print("[INPUT]", wanted_word)

start_time = time.time()

# 获得当前目录
current_directory = os.getcwd()
csv_file = ""

# 遍历当前目录下的文件
csv_file_count = 0
for file in os.listdir(current_directory):
    # 判断是否为需要的 CSV 文件
    if file.endswith('.csv') and "Top_Search_Terms" in os.path.basename(file):
        csv_file = file
        print("[IN]", csv_file)
        csv_file_count += 1

if csv_file_count == 0:
    print("未发现符合条件的csv文件")
    sys.exit()

if csv_file_count > 1:
    print("发现多个csv文件，请只保留所需的那个csv文件")
    sys.exit()

# 关键词和排名的列表
keyword_rank_list = []
wanted_keyword_rank_list = []

# 打开 CSV 文件
with open(csv_file, 'r', encoding='utf-8') as csvfile:
    # 读取 CSV 文件内容
    reader = csv.reader(csvfile)
    for row in reader:
        # keyword_list.append(row[1])
        keyword_rank_list.append([row[1], row[0]])

# print("keyword_rank_list", keyword_rank_list[0:100])

# keyword_rank_list的前两条信息不需要
for keyword in keyword_rank_list[2:]:
    if wanted_word in keyword[0]:
        # 已经按照rank排序
        wanted_keyword_rank_list.append(keyword)

# 包含wanted_word的关键词
wanted_keyword_list = []

for keyword in wanted_keyword_rank_list:
    if wanted_word in keyword[0]:
        wanted_keyword_list.append(keyword[0])

# 关键词列表转换为单词列表
wanted_keyword_word_list = []
for dk in wanted_keyword_list:
    wanted_keyword_word_list.extend(dk.split())

# 统计词频
word_counts = Counter(wanted_keyword_word_list)

# 获取出现次数最多的元素，并按照出现次数进行排序
most_common_word_counts = word_counts.most_common()
# 注意！
# word_counts是Counter, 里面是字典
# Counter({'dog': 25591, 'for': 10704, 'dogs': 8967,...})
# most_common_word_counts 是列表，里面是set
# [('dog', 25591), ('for', 10704), ('dogs', 8967),...]

# print("most_common_word_counts", most_common_word_counts)
# for word, count in word_counts.items():
#     print(f"{word}: {count}")

# 当前日期
t = datetime.datetime.today()
# windows系统的文件名不能包含":"
# 空格改为下划线，易看
t = str(t).replace(' ', '_').replace(":", "").split('.')[0]

output_wc_csv_file = wanted_word + "_word_count_" + t
result_csv_folder = "result"
output_wc_csv_file_path = result_csv_folder + "/" + output_wc_csv_file

# 判断是否创建result文件夹
if not os.path.exists('result'):
    # 创建 result 文件夹
    os.mkdir('result')
    print("[NOTE] create", result_csv_folder ,"folder")

# 把词频导出为csv
# word, counts
with open(output_wc_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    # 创建 CSV 写入器对象
    writer = csv.writer(csvfile)

    # 导出的csv未排序
    # for k,v in word_counts.items():
    #     writer.writerow([k, v])

    # 导出的csv已排序
    for wc in most_common_word_counts:
        writer.writerow(wc)
print("[OUT]", output_wc_csv_file_path)

# 把关键词和排名导出为csv
# keyword, rank
output_kr_csv_file = wanted_word + "_keyword_rank_" + t
result_csv_folder = "result"
output_kr_csv_file_path = result_csv_folder + "/" + output_kr_csv_file

with open(output_kr_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    # 创建 CSV 写入器对象
    writer = csv.writer(csvfile)
    # 导出的csv已排序
    for kr in wanted_keyword_rank_list:
        writer.writerow(kr)
print("[OUT]", output_kr_csv_file_path)

end_time = time.time()
# 计算运行时长（秒）
run_time = end_time - start_time
run_time = round(run_time, 2)
print("[SPEND]", str(run_time), "S")

print("-----DONE-----")
