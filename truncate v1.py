# author: dg1245
# e-mail: dg1245@qq.com
# start-date: 2023-11-12
# python-version: 3.12
# 协助：豆包 https://www.doubao.com/chat/

# 使用说明
# 先去亚马逊后台->Brands->Brand Analytics -> Search Analytics->
# ->Top Search Terms->Generate Report->Download Manager->下载csv
# 第40行代码填入wanted_lines，运行代码即可
# 当前文件夹里会生成1个包含Top_Search_Terms和wanted_lines的csv文件

import os
import csv
import sys
import time


def truncate_csv(csv_path, new_csv_path, wanted_lines):
    # 读取 CSV 文件
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # 写入新的 CSV 文件
        with open(new_csv_path, 'w', newline='', encoding='utf-8') as new_csvfile:
            writer = csv.writer(new_csvfile)

            # 写入前 wanted_lines 行，注意，原始csv前2行非数据内容也保留
            for i, row in enumerate(reader):
                if i < wanted_lines + 2:
                    writer.writerow(row)


# 修改该数值
wanted_lines = 10000

# 若wanted_lines数值大于0,就导出包含前wanted_lines行数的新csv
if wanted_lines > 0:
    print("[INPUT]", wanted_lines, "lines")
else:
    print("[NOTE] nothing happening")
    sys.exit()

start_time = time.time()

# 获得当前目录
current_directory = os.getcwd()
csv_file = ""
csv_file_count = 0

# 遍历当前目录下的文件
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

csv_path = csv_file
new_csv_path = "US_Top_Search_Terms_" + str(wanted_lines) + "_lines.csv"
truncate_csv(csv_path, new_csv_path, wanted_lines)
print("[OUT]", new_csv_path)

end_time = time.time()
# 计算运行时长（秒）
run_time = end_time - start_time
run_time = round(run_time, 2)
print("[SPEND]", str(run_time), "S")

print("-----DONE-----")
