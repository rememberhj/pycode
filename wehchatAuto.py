#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np  # 引入numpy库，目的是将读取的数据转换为列表
import pandas as pd  # 引入pandas库，用来读取csv数据
import chardet
from uiautomation import WindowControl  # 引入uiautomation库中的WindowControl类，用来进行图像识别和模拟操作
# 绑定微信主窗口
wx = WindowControl(
    Name='微信',
    searchDepth=1
)
# 切换窗口
wx.ListControl()
wx.SwitchToThisWindow()
# 寻找会话控件绑定
# hw = wx.ListControl(Name='会话')
if wx.ListControl(Name='综合x服务支撑群'):
    print("找到窗口")
    hw = wx.ListControl(Name='会话')
# 通过pd读取数据   
df = pd.read_csv('回复数据2.csv')
# 死循环接收消息
while True:
    # 从查找未读消息
    we = hw.TextControl(searchDepth=4)
    # 死循环维持，没有超时报错
    while not we.Exists():
        pass
    # 存在未读消息
    if we.Name:
        # 点击未读消息
        we.Click(simulateMove=False)
        # 读取最后一条消息
        last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name
        # 判断关键字
        msg = df.apply(lambda x: x['回复内容'] if x['关键词'] in last_msg else None, axis=1)
        print(msg)
        # 数据筛选，移除空数据
        msg.dropna(axis=0, how='any', inplace=True)
        # 做成列表
        ar = np.array(msg).tolist()
        # 能够匹配到数据时
        if ar:
            # 将数据输入
            # 替换换行符号
            wx.SendKeys(ar[0].replace('{br}', '{Shift}{Enter}'), waitTime=1)
            # 发送消息 回车键
            wx.SendKeys('{Enter}', waitTime=1)
            # 通过消息匹配检索会话栏的联系人
            wx.TextControl(SubName=ar[0][:5]).RightClick()
        # 没有匹配到数据时
        else:
            wx.SendKeys('我不理解你什么意思', waitTime=1)
            wx.SendKeys('{Enter}', waitTime=1)
            wx.TextControl(SubName=last_msg[:5]).RightClick()