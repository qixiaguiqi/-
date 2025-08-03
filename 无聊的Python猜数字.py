import random

def guess_number():
    # 生成一个 1-100 的随机整数
    target = random.randint(1, 100)
    attempts = 0  # 记录猜测次数
    max_attempts = 10  # 最多允许猜10次

    print(" 欢迎来到猜数字游戏！")
    print(f" 我已经想好了 1-100 之间的一个数字，你有 {max_attempts} 次机会猜中它~")

    while attempts < max_attempts:
        try:
            guess = int(input("\n 请输入你的猜测（1-100）："))
            
            # 输入合法性检查
            if guess < 1 or guess > 100:
                print("⚠ 请输入1-100之间的数字！")
                continue

            attempts += 1

            # 判断猜测结果
            if guess < target:
                print(f" 猜小了！剩余次数：{max_attempts - attempts}")
            elif guess > target:
                print(f" 猜大了！剩余次数：{max_attempts - attempts}")
            else:
                print(f"\n🎉 恭喜！你用了 {attempts} 次猜中了数字 {target}！")
                return

        except ValueError:
            print("⚠ 请输入有效的整数！")

    # 机会用完仍未猜中
    print(f"\n 很遗憾，正确数字是 {target}。下次加油哦！")

# 启动游戏
if __name__ == "__main__":
    guess_number()

    NameError