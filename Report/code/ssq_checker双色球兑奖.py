# clh224's Lottery Pro - 严谨拆分录入 + 倍率收益版
# 2026-02-22 Leon's Final Stable Version

def get_red_balls(prompt):
    """专门处理红球录入：6个、1-33、不重复"""
    while True:
        try:
            raw = input(f"{prompt}请输入 6 个红球 (01-33，空格隔开): ")
            reds = [int(n) for n in raw.split()]
            if len(reds) != 6:
                print(f"❌ 数量错误：你需要 6 个，现在有 {len(reds)} 个。")
                continue
            if any(n < 1 or n > 33 for n in reds):
                print("❌ 范围错误：红球必须在 01-33 之间！")
                continue
            if len(set(reds)) < 6:
                print("❌ 重复错误：红球号码不能重复。")
                continue
            return sorted(reds)
        except ValueError:
            print("❌ 输入非法：请输入纯数字。")

def get_blue_ball(prompt):
    """专门处理蓝球录入：1个、1-16"""
    while True:
        try:
            blue = int(input(f"{prompt}请输入 1 个蓝球 (01-16): "))
            if 1 <= blue <= 16:
                return blue
            print("❌ 范围错误：蓝球必须在 01-16 之间！")
        except ValueError:
            print("❌ 输入非法：请输入纯数字。")

def lottery_checker():
    # 1. 数据录入
    win_red = get_red_balls("【开奖】")
    win_blue = get_blue_ball("【开奖】")
    my_red = get_red_balls("【你的】")
    my_blue = get_blue_ball("【你的】")

    # [新增] 录入倍数逻辑
    try:
        times = int(input("\n💰 请输入购买倍数 (Multiplier): "))
        if times <= 0: times = 1
    except ValueError:
        times = 1

    # 2. 核心比对与奖金判定
    hit_red_count = len(set(win_red) & set(my_red))
    hit_blue = (win_blue == my_blue)

    # 奖金标准 (单注)
    bonus_dict = {
        "一等奖": 5000000, "二等奖": 200000, "三等奖": 3000,
        "四等奖": 200, "五等奖": 10, "六等奖": 5, "未中奖": 0
    }

    level, is_floating = "未中奖", False
    if hit_red_count == 6 and hit_blue:
        level, is_floating = "一等奖", True
    elif hit_red_count == 6:
        level, is_floating = "二等奖", True
    elif hit_red_count == 5 and hit_blue:
        level = "三等奖"
    elif (hit_red_count == 5) or (hit_red_count == 4 and hit_blue):
        level = "四等奖"
    elif (hit_red_count == 4) or (hit_red_count == 3 and hit_blue):
        level = "五等奖"
    elif hit_blue:
        level = "六等奖"

    total_bonus = bonus_dict.get(level, 0) * times

    # 3. 视觉增强输出
    pretty_f = lambda balls: "  ".join([f"{b:02d}" for b in balls])
    print("\n" + "★" * 15 + " 核对报告 " + "★" * 15)
    print(f"开奖号码：红 {pretty_f(win_red)} | 蓝 [{win_blue:02d}]")
    print(f"你的号码：红 {pretty_f(my_red)} | 蓝 [{my_blue:02d}]")
    print("-" * 40)
    print(f"🎯 命中情况：{hit_red_count}红 + {'1' if hit_blue else '0'}蓝")

    if total_bonus > 0:
        tag = "(含浮动奖池预测)" if is_floating else ""
        print(f"🎊 恭喜！中得【{level}】 x {times} 倍")
        print(f"💵 预计总收益：{total_bonus:,} 元 {tag}")
    else:
        print("🕯️ 遗憾未中奖，下次好运。")
    print("=" * 45)

if __name__ == "__main__":
    lottery_checker()

# 🚀 Future Roadmap:
# 1. v2.0 EXE: Use PyInstaller to build a standalone Windows app.
# 2. v2.1 GUI: Add a graphical interface using Tkinter or PyQt.
    
#EN🚀 Future Roadmap / 未来规划
#- [ ] **v2.0 Data Scraper**: Auto-fetch historical results and save to `data.txt`.
#- [ ] **v3.0 Prediction Engine**: Analyze frequency, hot/cold numbers, and odd/even ratios.
#- [ ] **v4.0 Self-Evolution**: Backtest strategies and optimize algorithm weights.
#> **Disclaimer**: This project is for technical exploration only. Lottery is random. Please play responsibly. (If this code wins, milk tea is on you! 🧋)

#ZH-HANS🚀 未来 roadmap / 画大饼时间（认真版）
# v2.0 爬虫模块：
# 自动爬取往期双色球开奖数据
# 生成/更新 data.txt 作为历史数据库
# 支持增量更新（只爬新的）
# v3.0 预测引擎：
# 基于历史数据分析（冷热号、连号、奇偶比）
# 独立运行的预测程序
# 输出"下一期推荐号码"
# v4.0 自我进化：
# 记录预测准确率
# 根据历史命中率调整算法权重
# 实现简单的"机器学习"（哪怕只是统计优化）、
# 💭 终极目标：让程序和彩票店老板比赛，谁先推荐中奖号？
# 注：纯技术挑战，不构成投资建议，中奖了请自觉请我喝奶茶。
