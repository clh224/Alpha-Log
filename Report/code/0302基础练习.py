# 1. 定义一个列表（用方括号 []）
device=["iPhone","Mac","Android"]#定义，用的[]代表集合
# 2. 往列表里加东西 (append)
device.append("Smarttv")#这个.append是往里面加东西
# 3. 取出列表里的东西
#Python 从 0 开始数，第 1 个设备是 devices[0]
print(f"列表中第一个设备是：{device[0]}")#先f格式化后{device[0]}代表直接找列表第一个
print(f"当前连接的设备是：{device}")
# 4. 看看总共有几个设备 (len)
print(f" 当前共有{len(device)}个设备连接在软路由上")#len数总数
#现在试试往我的device加东西 input输入
new_device=input("请输入新连接的设备名：")#输入新设备的名字
device.append(new_device)#把新设备输入进总列表中
print(f"您刚刚加入了这个设备{new_device}")#输出您刚刚加入的设备
print(f"现在您的总设备是{device}")#输出您现在的总设备
#笔记总结 用{len(devicce)}len来统计我定义的device有多少
#.append是往之前的集合中加东西
#[]属于集合 注意格式{device[0]}