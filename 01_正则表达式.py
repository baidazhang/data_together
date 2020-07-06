import re

# result = re.match(正则表达式，要匹配的字符串)
#如果匹配到数据可以使用result.group()提取数据
#re.math()根据正则表达式从头开始匹配字符串数据
result = re.match('itcast','itcast.cn')
info = result.group()
# print(info)

#匹配单个字符串
# .任意一个字符串，除\n ，匹配[]中列举的字符，\d 匹配0-9
# \D 匹配非数字， \s匹配空白，即是空格，tab键,\S匹配非空
# \w 匹配非特殊字符，即a-z A-Z 0-9 _ 汉字 \W 相反
ret = re.match('.','c')
print(ret.group())

ret = re.match('t.o','too')
print(ret.group())

ret = re.match('t.o','two')
print(ret.group())
#匹配0-9
ret = re.match('[0-9]hello python','8hello python')
print(ret.group())
ret = re.match("[0-35-9]Hello Python","7Hello Python")
print(ret.group())
mathch_obj = re.match('\D','f')
print(mathch_obj.group())
match_obj = re.match("hello\sworld", "hello world")
print(match_obj.group())
match_obj = re.match("\w", "A")
print(match_obj.group())

#匹配多个字符
print('匹配多个字符')
# * 匹配前一个字符出现0次或无限次
# + 匹配前一个字符1次或者无限次
# ? 匹配前一个字符1次或者0次
#{m}次  {m,n} 匹配前一个m到n次 ，都是前一个字符
ret = re.match('[A-Z][a-z]*','M')
print(ret.group())
ret = re.match("[A-Z][a-z]*","MnnM")
print(ret.group())
ret = re.match('[A-Z][a-z]*','AabcdeFcDaa')
print(ret.group())
match_obj = re.match("t.+o", "two")
print(mathch_obj.group())
match_obj = re.match('https?','http')
print(match_obj.group())

ret = re.match('[a-zA-Z0-9_]{6}','12a3g3432')
print(ret.group())
ret = re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66")
print(ret.group())
#匹配开头和结尾
mathch_obj = re.match('^\d.*','3hello')
print(mathch_obj.group())
mathch_obj = re.match('.*\d$','hello5')
print(mathch_obj.group())
mathch_obj = re.match('^\d.*\d$','4lsdjfls5')
print(mathch_obj.group())

# 除了指定字符外都匹配
# [^dsfl]表示除了指定字符都匹配
match_obj = re.match('[^aeiou]','h')
print(match_obj.group())

# 匹配分组
# \ 匹配左右任意一个表达式，
#(ab)将括号中字符作为一个分组
# \num 引用分组num 匹配到的字符串
# (?P<name>) 分组起别名
# (?P=name) 引用别名为name分组匹配到的字符
match_obj = re.match('apple|pear','apple')
print(match_obj.group())

match_obj = re.match('(qq):([1-9]\d{4,10})','qq:102322234')
print(match_obj.group())
# \num使用
ret = re.match("<([a-zA-Z1-6]+)>.*</\\1>", "<html>hh</html>")
print(ret.group())
match_obj = re.match("<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")
print(match_obj.group())