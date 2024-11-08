# 创建主窗口
tk = tkinter.Tk()
# 设置窗口大小和位置
tk.geometry('300x210+500+200')
# 不允许改变窗口大小
tk.resizable(False, False)
# 设置窗口标题
tk.title('计算器')