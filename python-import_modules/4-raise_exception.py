def raise_exception():
    try:
        10 + "hello"
    except TypeError as e:
        print("Exception has been raised")