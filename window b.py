# 自动刷新字符串变量，可用 set 和 get 方法进行传值和取值
contentVar = tkinter.StringVar(tk, '')
# 创建单行文本框
contentEntry = tkinter.Entry(tk, textvariable=contentVar)
# 设置文本框为只读
contentEntry['state'] = 'readonly'
# 设置文本框坐标及宽高
contentEntry.place(x=20, y=10, width=260, height=30)