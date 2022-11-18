import numpy as np
import re
import time

start=time.time()
the_keyword = ["auto", "break", "case", "char", "levelst", "leveltinue", "default", "do",
                 "double", "else", "enum", "extern", "float", "for", "goto", "if",
                 "int", "long", "register", "return", "short", "signed", "sizeof", "stastic",
                 "struct", "switch", "typedef", "union", "unsigned", "void", "else-if", "while"]
path = "D:\【桌面】\EE308_LAB1_2.cpp"
f = open(path, "r")
now_line = f.readline()
now_line = now_line[:-1]
the_keywords_length = 32
num_a = 0
num_b = []
flag_if = 0
flag_else_if = 0
num_if_else = 0
num_if_else_if_else = 0
sentences = []
x_len = 100000
count = np.zeros(the_keywords_length, dtype=int)



# level 1_2


while now_line:
    now_line = f.readline()
    now_line = now_line[:-1]
    now_line = now_line.replace("else if", "else-if")   ## 将else if 更换成else-if便于操作
    x = re.split(' |\(|\;|\\t|\:|\{|\/\/', now_line)

    for i in x:
        if (i == "if" or i == "else" or i == "else-if"):
            sentences.append(x)
            continue
    for i in x:
        for j in range(32):
            if (i == the_keyword[j]):
                if (i == "switch"):
                    num_b.append(num_a)
                    num_a = 0
                if (i == "case"):
                    num_a += 1
                count[j] += 1

f.close()
num_b.append(num_a)  ## 第一次默认的num=0的遗留问题，它占位了，最后一次记录的case数量，刚好抓在手上，这个时候要放进去
sum = 0
for i in range(32):
    if (count[i] != 0):
        sum += count[i]
        if (i == 30):
            sum += count[i]


# level 3_4


for i in sentences:
    if (len(i) < x_len):
        x_len = len(i)


for j in range(x_len):
    for i in sentences:
        if (i[j] == "if"):
            flag_if = 1
        if (i[j] == "else-if"):
            flag_else_if = 1
        if (i[j] == "else"):
            if (flag_else_if == 1):
                num_if_else_if_else += 1
            elif (flag_if == 1):
                num_if_else += 1
            flag_else_if = 0
            flag_else = 0
end=time.time()


##print("running time",-start+end)

level = int(input("level of stastic (from 1 to 4): "))
if (level == 1):
    print("sum : ", sum)  # 1
if (level == 2):
    print("sum : ", sum)  # 1
    print(the_keyword[25], " num : ", count[25])  # 2
    print("case num", num_b[1:3])  # 2
if (level == 3):
    print("sum : ", sum)  # 1
    print(the_keyword[25], " num : ", count[25])  # 2
    print("case num", num_b[1:3])  # 2
    print("if-else num:", num_if_else)  # 3
if (level == 4):
    print("sum : ", sum)  # 1
    print(the_keyword[25], " num : ", count[25])  # 2
    print("case num", num_b[1:3])  # 2
    print("if-else num:", num_if_else)   # 3
    print("if-elseif-else num:", num_if_else_if_else)   # 4





