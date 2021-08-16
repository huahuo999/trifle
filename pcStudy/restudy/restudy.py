import re

line = "bobby123"

regex_str = "^b."
# ^b 以b开头
# .代表任意字符
# *前面这个字符可以重复任意多次

if re.match(regex_str, line):
    print("b.* yes")

regex_str = "^a."
if re.match(regex_str, line):
    print("a,*  yes")

regex_str = "^.*3$"
if re.match(regex_str, line):
    print("^.*3$  yes")
# 以$表示以其前一个字符结尾的字符串


regex_str = "^b.*3$"
if re.match(regex_str, line):
    print("^b.*3$  yes")

line = "bboooooooobby123"
regex_str = ".*(b.*b).*"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
    print("yes")
# ()表示提取括号内的字符串
# 正则表达式从反向开始匹配(贪婪) 从右边开始

regex_str = ".*?(b.*b).*"

match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))

# 加入?从左侧提取且提取一个就够了 不贪婪

# +表示至少出现一次才能匹配成功