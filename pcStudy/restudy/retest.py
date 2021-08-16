import re
#\d代表数字
line = "XXX出生于2001年6月1日"
line1 = "XXX出生于2001/6/1"
line2 = "XXX出生于2001-6-1"
line3 = "XXX出生于2001-06-01"
line4 = "XXX出生于2001-06"
regex_str = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}[日]*|[月/-]$|\d{1,2}[日]*|$))"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
