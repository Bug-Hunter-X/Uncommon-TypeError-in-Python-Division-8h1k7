def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None

# Example usage with an uncommon error
value1 = 10
value2 = "hello"
result = function_with_uncommon_error(value1, value2)
print(f"Result: {result}")