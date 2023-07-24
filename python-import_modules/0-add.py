from add_0 import add
a = 1
b = 2
if __name__ == "__main__":
    try:
        print("{} + {} = {}".format(a, b, add(a, b)))
    except TypeError:
        print("Traceback (most recent call last):")
        print("{} + {}".format(a, b))