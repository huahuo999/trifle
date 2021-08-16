import re

# +表示+前面的字符至少出现一次才能匹配成功
line = "boooobaaaooobbbbbby123"
regex_str = ".*(b.+b).*"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))

# {number1, number2}前面的字符满足
# 最少number1次
# 最多number2次才能匹配
regex_str = ".*(b.{1}b).*"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))

# A|B表示或者 满足哪个返回哪个 如果都满足就返回最前面的
line = "bobby123"
regex_str = "(bobby|bobby123)"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))

line = "boobby123"
regex_str = "((bobby|boobby)123)"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
    print(match_obj.group(2))
# group(number)表示取第number个括号的词

line = "boobby123"
# []表示满足[]内任意字符即可匹配,若满足多个取后面的
regex_str = "([abcd]oobby123)"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))

# [0-9]还可以用来表示范围0到9内任意字符 [^1]表示不等于1即可
    # [.*]中括号内的符号不再有特殊用途
    line = "18782902222"
    regex_str = "(1[48357][0-9]{9})"
    match_obj = re.match(regex_str, line)
    if match_obj:
        print(match_obj.group(1))
# \s表示一个空格
# \S表示只要不是空格都行
line = "你 好"
regex_str = "(你\s好)"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))

# \w = [A-Za-z0-9_]表示word字符都行
# \W 不为字符A-Za-z0-9_就行