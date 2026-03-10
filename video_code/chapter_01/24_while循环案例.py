print("你身处密室，需要正确回答出问题的答案后，才可逃出密室！")
question = "你是什么人"
answer = '你的心上人'
guest = ''
while guest != answer:
    if guest != '':
        print("回答错误！请重新回答！！")
    print(f"问题：{question}?,请回答：")
    guest = input()
print('恭喜你逃出密室')