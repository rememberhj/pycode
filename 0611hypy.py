import tkinter as tk
from tkinter import ttk
import time

# 创建主窗口
root = tk.Tk()
root.title("数据对比工具 - wsTel hj")
root.geometry('800x600')

# 设置主题风格
style = ttk.Style()
style.theme_use('clam')

# 颜色配置
bg_color = "#f0f0f0"
text_bg = "#ffffff"
button_bg = "#4CAF50"
button_fg = "white"

# 配置主窗口背景
root.configure(bg=bg_color)

# 创建主框架
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# 文本框 - 只用于数据输入和结果展示
text_font = ('Microsoft YaHei', 10)
enHj = tk.Text(main_frame, width=80, height=20, 
               font=text_font, bg=text_bg, 
               wrap=tk.WORD, padx=5, pady=5)
enHj.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

# 控制面板框架（包含按钮和提示）
control_panel = ttk.Frame(main_frame)
control_panel.pack(fill=tk.X, pady=5)

# 按钮框架
button_frame = ttk.Frame(control_panel)
button_frame.pack(side=tk.LEFT)

# 导入按钮
btn_import = ttk.Button(button_frame, text="导入数据", 
                       command=lambda: getData(), 
                       style='Accent.TButton')
btn_import.pack(side=tk.LEFT, padx=5, ipadx=20)

# 对比按钮
btn_compare = ttk.Button(button_frame, text="开始对比", 
                        command=lambda: compDate())
btn_compare.pack(side=tk.LEFT, padx=5, ipadx=20)

# 提示信息标签（放在按钮右侧）
info_label = ttk.Label(control_panel, text="就绪", 
                      foreground="#666666", 
                      font=('Microsoft YaHei', 9))
info_label.pack(side=tk.LEFT, padx=20)

# 全局变量
text_contentall = []
str_arr = []
str_arr2 = ""

def show_info(message, color="#666666"):
    """显示提示信息到标签"""
    info_label.config(text=message, foreground=color)
    root.after(3000, lambda: info_label.config(text="就绪", foreground="#666666"))

def clear_text():
    """清空编辑框"""
    enHj.delete("0.0", "end")

def getData():
    global text_contentall, str_arr, str_arr2
    
    content = enHj.get("0.0", "end").strip()
    if not content:
        show_info("错误: 没有输入数据", "red")
        return
        
    # 处理数据
    text_contentall = [line.replace(" ", "") for line in content.split("\n") if line.strip()]
    str_arr = text_contentall
    str_arr2 = '\n'.join(str_arr)
    
    # 显示提示信息
    show_info(f"成功导入 {len(text_contentall)} 行数据", "green")
    # 清空编辑框，准备新输入
    clear_text()

def compDate():
    global str_arr3, str_arr4, str_arr5
    
    if not str_arr:
        show_info("错误: 请先导入数据", "red")
        return
        
    content = enHj.get("0.0", "end").strip()
    if not content:
        show_info("错误: 没有输入对比数据", "red")
        return
        
    # 处理对比数据
    str_arr3 = [line.replace(" ", "") for line in content.split("\n") if line.strip()]
    str_arr4 = []
    
    for element in str_arr3:
        for element2 in str_arr:
            parts = element2.split('\t')
            if len(parts) > 0 and element == parts[0]:
                str_arr4.append(element2)
    
    # 显示对比结果
    clear_text()
    if str_arr4:
        enHj.insert('0.0', '\n'.join(str_arr4))
        show_info(f"对比完成，找到 {len(str_arr4)} 条匹配数据", "green")
    else:
        show_info("对比完成，没有匹配数据", "orange")

# 运行主循环
root.mainloop()