
def speak(msg):
    print("----------")
    print(msg)
    print("----------")

def greet(name,msg):
    print(f'我叫{name}，我想说的话在下面：')
    speak(msg)
    print('嗯，我说完了')

greet('靓仔','广东我最靓')


