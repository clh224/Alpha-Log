# Intelligent Converter

def main():
    print("--- 欢迎使用换算工具 ---")
    # 1. 询问用户想干什么
    choice = input("请选择模式 (按1: CNY兑换USD | 按2: USD兑换CNY): ")

    # 2. 用 if 来判断
    if choice == "1":
        # 模式 1 的逻辑
        cny = float(input("请输入人民币金额: "))
        rate = 6.91 #根据实时汇率更改
        print(f">>> 折合美金约为: ${round(cny / rate, 2)}")
        print("当前汇率1USD=6.91CNY")

    elif choice == "2":
        # 模式 2 的逻辑
        usd = float(input("请输入美金金额: "))
        rate = 6.91 #根据实时汇率更改
        print(f">>> 折合人民币约为: ¥{round(usd * rate, 2)}")
        print("当前汇率1 USD = 6.91 CNY")

    else:
        # 如果用户乱按（比如按了 3 或者敲了字母）
        print("⚠️ 输入错误，请输入 1 或 2")
# 启动
main()
#本次更新v1.10新增逻辑控制： 引入 if-else 分支导航，支持 CNY/USD 双向自主切换，再也不用手动改公式了。
#交互细节优化： 结果输出增添“约”字描述，遵循金融严谨性原则，减少认知误差。
#状态实时回显： 每次计算后自动打印当前参考汇率，确保每一分资产变动都尽在掌握。
#修复了一些已知问题： 优化了变量命名逻辑，提升了代码在老旧设备上的“精神流畅度”。
#Updated the currency conversion tool to support both CNY to USD and USD to CNY conversions. Improved user interaction and fixed known issues.
