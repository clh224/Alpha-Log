#今天学dict
# 1. 定义字典（用花括号 {}，Key 和 Value 之间用冒号 :）
router = {
    "brand": "小米",
    "model": "AX3600",
    "price": 599,
    "is_online": True
}

# 2. 查：通过 Key 拿 Value
print(f"设备型号是：{router['model']}")#f格式 解释为 router这个花括号里面的[]为产品

# 3. 改：就像给变量赋值一样
router["price"] = 499  # 降价了 注意空格
print(f"调整后的价格：{router['price']}")

# 4. 增：直接写一个新的 Key 进去
router["owner"] = "me"#加新的东西
print(router)

#总结笔记 先定义词典 ：连接键和值 花括号负责括起来
