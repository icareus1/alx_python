def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    except TypeError:
        print("Error: Both operands must be integers.")
    finally:
        print("Inside result: {}".format(result))
        return result