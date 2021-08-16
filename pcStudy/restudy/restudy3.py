import re

# [\u4500-\u9FA5]提取中文
line = "你好ss"
regex_str = "([\u4500-\u9FA5]+)"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))

line = "study in 南京大学"
regex_str = ".*?([\u4500-\u9FA5]+大学)"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))

line = "XXX出生于2001年"
regex_str = ".*?(\d+)年"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))

