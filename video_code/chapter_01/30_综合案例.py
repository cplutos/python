print('欢迎来到答题闯关，输入q可以随时退出')
question1, answer1 = 'python中的输出函数是？', 'print'
question2, answer2 = 'python中并且关键字是？', 'and'
question3, answer3 = 'python是解释型还是编译型？', '解释型'
max_tries = 3
count = 0
total_levels = 3
is_playing = True
for level in range(1, total_levels + 1):
    print(f"*******第{level}关*******\n")
    #     取出当前关卡所对应的答案
    if level == 1:
        question, answer = question1, answer1
    elif level == 2:
        question, answer = question2, answer2
    else:
        question, answer = question3, answer3
    tries = 1
    while tries<=max_tries:
        user_input = input(question)
        if user_input == answer:
            print("回答正确！\n")
            break
        elif user_input == '':
            print('你输入为空，请重新作答！\n')
        elif user_input == 'q':
            print("您已退出游戏\n")
            is_playing = False
            break
        else:
            leave = max_tries-tries
            if leave > 0:
                print(f'回答错误，你还剩{leave}次机会\n')
                tries+=1
                continue
            else:
                print(f"挑战结束，次数已用尽，本题答案为{answer}")
                is_playing = False
                break
    if not is_playing:
        break
    if is_playing and level == 3:
        print('完美通关')
