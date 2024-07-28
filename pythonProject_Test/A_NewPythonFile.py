import math
from Cat import Cat, CyberCat
from pathlib import Path
import json

print(math.log2(8))
'''字符串打印'''
# .remove suffix("你想移除的后缀").remove prefix()前缀.strip()左边空格移除.strip()移除两边
# 首字母大写, 全大写全小写, 原不动
a = 'I never like Joe\'s jack'
print(a.upper(), "\n", a.lower(), "\n", a.title())
# 三引号换行
print('''helloworld
你妈的
可以换行了'''

      '当然\n不行')
# 转义换行tab
a = '\n \t这样也\t\t行?'
print(
    a.lstrip()
)
# 转义避免引号重叠

'''变量'''
# 赋值变量带空格
my_love = "宝"
# py语法糖
a = b = c = 2
print(a, b, c)
# 字符串中使用变量
print(f"字符串中{a}")
# format方法
message = '''
{0}'你好(*´▽｀)ノノ'
{1}'你不好'
'''.format('wy', 'wyf')

'''列表'''
a = [1, 2, 3.0, True, 1.5]
a[1] = 2
a.insert(7, "aaa")
print(a)
del a[-1]
print(max(a), min(a), sorted(a))

'''元组, 字典'''
# 用圆括号避免陈思佳2问题
PhoneNumber = {("张伟", 1): "张伟1的电话",
               ('张伟', 2): 456,
               ('张伟', 3): 789}
print("\n", PhoneNumber[('张伟', 1)], '\n', PhoneNumber)

# 键值对遍历
for a, b in PhoneNumber.items():
    print(a, b, end='')

'''函数'''


# 他甚至标明了调用次数, 我哭死
# 默认值放最后,实参名称应该小写
def dog(b1, a1=6):
    return a1 + b1


# 默认值一定要用不可变对象，否则默认值会可能随着调用发生变化,默认值不用可变对象
def err_demo2(a1, b1, c1=None):
    if c1 is None:
        c1 = []
    c1.append(a1)
    c1.append(b1)
    print(a1, b1, c1)


print("\n")
err_demo2(1, 2)
err_demo2(3, 4)
# 给实参按顺序, 除非指明
print("\n", dog(9, a1=4), dog(9))

'''类'''

# 封装, 继承, 多态
# 首字母大写的是类
# 形参self必不可少,因为调用创建cat实例时会自动传入实参self.他是一个只想实力本身的引用,让实例能够防雾灯类众的属性和方法

# 在类后要有两空行,逗号后空格
tom = Cat('tom', 18, 2)
tom.attackplus()
tom.attack()
cyber_tom = CyberCat("tom", 18, 2)
# tmd代码最后留且只留一行空
# 类采用大驼峰命名

'''文件读取'''
path = Path('ok.py')
contents = path.read_text()
print(contents.rstrip())
# 访问文件时中文支持呢在井号后面?
line = contents.splitlines()
path.write_text('This is last sentence\n')
# 如果置顶的内容已经存在,path 会删掉覆盖
for li in line:
    print(li)
# 显示文字绝对路径时windows会显示反斜杠,但是你应该用斜杠,,可以自动转化

'''try'''
#
# a = int(input('\n这里输入'))
# b = int(input("\n这里再输入"))
# try:
#     answer = a/b
# except ZeroDivisionError:
#     pass
#     # pass不挡啊
#     print("就你tm除零是吧")
# else:
#     print(answer)
try:
    p = Path('jason.json')
except FileNotFoundError:
    pass
else:
    # dumps存储,loads取出
    js = json.dumps([1, 2])
    p.write_text(js)
    c = json.loads(js)
    print(js, c)
if path.exists():
    print(path, p)
