# 打开对齐文档
al = open('align.txt', 'w')

# 提示文本
print('请按照提示输入，如果全部输入完成，请输入空格并连续敲击回车')

# 给出输入内容题头
original = str(input('原文内容 '))
translation = str(input('英译 '))

# 在用户界面和对齐文档内都输出内容
print(original, '\n', translation, sep='')
print(original, '\n', translation, sep='', file=al)

# 通过while循环实现重复输入，功能一致
while type(original) == str:
    original = str(input('原文内容 '))
    translation = str(input('英译 '))
    print(original, '\n', translation, sep='')
    print(original, '\n', translation, sep='', file=al)

    # 结束标记，用一个空格表示
    if original == ' ':
        break

# 完成内容，提示结果
print('输入完成！')

# 关闭并保存文件
al.close()
