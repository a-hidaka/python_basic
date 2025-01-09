def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "0は使えません"
    
print("__name__",__name__)
if __name__ == "__main__":
    print("Hello.World!")