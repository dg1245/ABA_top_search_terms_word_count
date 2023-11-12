# ABA_top_search_terms_word_count

author: dg1245

e-mail: dg1245@qq.com

start-date: 2023-11-11

python-version: 3.12

协助：豆包 https://www.doubao.com/chat/

# word count 使用说明

先去亚马逊后台 -> Brands -> Brand Analytics -> Search Analytics-> Top Search Terms -> Generate Report -> Download Manager -> 下载csv

第21行代码填入wanted_word，运行代码即可

result文件夹里会生成2个包含word_count和keyword_rank的csv文件

# truncate 使用说明

先去亚马逊后台 -> Brands -> Brand Analytics -> Search Analytics-> Top Search Terms -> Generate Report -> Download Manager -> 下载csv

第40行代码填入wanted_lines，运行代码即可

当前文件夹里会生成1个包含Top_Search_Terms和wanted_lines的csv文件

特别说明：csv里可能包含非英文字符，直接用excel打开会出现乱码或行错乱，解决方案如下：excel-数据标签--导入csv--选择utf-8编码--导入即可，或者使用wps office以表格形式打开，或者使用vs code, pycharm, 记事本等以文本形式打开

特别说明：最新版excel最大显示行数为1,048,576，表头2行已占用，所以wanted_lines不要超过1,048,574，否则exel无法完整显示csv所有行


