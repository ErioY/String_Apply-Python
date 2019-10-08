'''
@Autor: ErioY
@Date: 2019-10-08 19:07:27
@Email: 1973545559@qq.com
@Github: https://github.com/ErioY
@LastEditors: ErioY
@LastEditTime: 2019-10-08 21:05:57
'''
# 有一段英文文本，其中有单词连续重复了2次，编写程序检查重复的单词并只保留一个。例如：文本内容为“This is a desk.”，程序输出为“This is a desk.”
str = "Chinese Chinese people have have happiness"
print("原字符串为：" + str)
arr = str.split()
for i in range(0, len(arr) - 1):
    if arr[i] == arr[i+1]:
        arr[i+1] = " "
# 去掉多余的空格
arr1 = " ".join(arr).split()
str = " ".join(arr1)
print("去重后的字符串为：" + str)
