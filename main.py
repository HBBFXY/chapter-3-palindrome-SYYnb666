# 从键盘输入一个五位数
num = int(input（"请输入一个五位数："))
original_num = num  # 保存原数，用于最后比较
reverse_num = 0
while num > 0:
    # 取出最后一位数字
    digit = num % 10
    # 构建反转后的数
    reverse_num = reverse_num * 10 + digit
    # 去掉最后一位数字
    num = num // 10
# 判断是否为回文数
if original_num == reverse_num:
    print(f"{original_num} 是回文数")
else:
    print(f"{original_num} 不是回文数")
