
def decor(x):
    def wrap():
        print("========================")
        x()
        print("========================")
    return wrap
@decor
def print_text():
    print("this is it")

decorate = decor(print_text)
decorate()


def decor(func):
    def wrap():
        print("==========================")
        func()
        print("==========================")
    return wrap


decorate = decor(print_text)

decorate()

print_ = decor(print_text)

print_()

print_text()
