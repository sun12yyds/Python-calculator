# 点击事件
def onclick(btn):
    # 运算符
    operation = ('+', '-', '*', '/', '**', '//')
    # 获取文本框中的内容
    content = contentVar.get()
    # 如果已有内容是以小数点开头的，在前面加 0
    if content.startswith('.'):
        content = '0' + content  # 字符串可以直接用+来增加字符
    # 根据不同的按钮作出不同的反应
    if btn in '0123456789':
        # 按下 0-9 在 content 中追加
        content += btn
    elif btn == '.':
        # 将 content 从 +-*/ 这些字符的地方分割开来
        lastPart = re.split(r'\+|-|\*|/', content)[-1]
        if '.' in lastPart:
            # 信息提示对话框
            tkinter.messagebox.showerror('错误', '重复出现的小数点')
            return
        else:
            content += btn
    elif btn == 'C':
        # 清除文本框
        content = ''
    elif btn == '=':
        try:
            # 对输入的表达式求值
            content = str(eval(content))
        except:
            tkinter.messagebox.showerror('错误', '表达式有误')
            return
    elif btn in operation:
        if content.endswith(operation):
            tkinter.messagebox.showerror('错误', '不允许存在连续运算符')
            return
        content += btn
    elif btn == '√':
        # 从 . 处分割存入 n，n 是一个列表
        n = content.split('.')
        # 如果列表中所有的都是数字，就是为了检查表达式是不是正确的
        if all(map(lambda x: x.isdigit(), n)):
            content = eval(content) ** 0.5
        else:
            tkinter.messagebox.showerror('错误', '表达式错误')
            return
    # 将结果显示到文本框中
    contentVar.set(content)