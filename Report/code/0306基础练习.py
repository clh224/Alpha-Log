#今天主要学for循环
devices=["MAC","PS4PRO","iPhone","Android"]#依旧定义 依旧集合
for device in devices:#临时的定义device
    if "iPhone" in device:
        print(f"{device}发现核心设备")#f格式化字符串
    else:
        print(f"{device}扫描正常")#f格式化
#做个今日笔记总结
#还是要f格式字符串，for即是用简短的几行代替很多行一行行敲 像是直接从集合提取 执行循环
