

global_vsriable = "グローバル変数です。"

def my_function():
    print(global_vsriable)

my_function()
print(global_vsriable)


def my_function():
    local_var = "ローカル変数です。"
    print(local_var)

my_function()  #ここは出力される
#print(local_var)　　　＃ここはエラーになる


name = "グローバル変数です。"

def my_function():
    name = "ローカル変数です。"
    print(name)

my_function()
print(name)



x = 10
def add():
    global x 
    x = 20
    return x
print(add())
print(x)
