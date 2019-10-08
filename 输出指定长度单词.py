'''
@Autor: ErioY
@Date: 2019-10-08 19:08:19
@Email: 1973545559@qq.com
@Github: https://github.com/ErioY
@LastEditors: ErioY
@LastEditTime: 2019-10-08 20:54:30
'''
# 编写程序，用户输入一段英文，然后输出这段英文中所有长度为3个字母的单词。
# str = input("please input sth: ")
str = "abcd abb aa vvv"
arr = []
arr = str.split()
print("长度为3的单词为：")
for i in range(0, len(arr)):
    if len(arr[i]) == 3:
        print(arr[i])
