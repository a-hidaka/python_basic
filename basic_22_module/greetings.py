def say_hello(name):
    print(f"こんにちは{name}さん")

def say_goodbye(name):
    print(f"さようなら{name}さん")

organization = "バンタン"

print("greeetings.pyの__name__:",__name__)

if __name__ == "__main__":
    print("greetings.pyがメインでされている")
    say_goodbye("akira")
print("__name__",__name__)