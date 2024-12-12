def function_with_uncommon_error_solution(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print("Error: Division by zero")
            return None
    else:
        print("Error: Invalid input type. Both inputs must be numbers.")
        return None

# Example usage with input validation
value1 = 10
value2 = "hello"
result = function_with_uncommon_error_solution(value1, value2)
print(f"Result: {result}")

value3 = 10
value4 = 2
result = function_with_uncommon_error_solution(value3, value4)
print(f"Result: {result}")

value5 = 10.5
value6 = 2.5
result = function_with_uncommon_error_solution(value5, value6)
print(f"Result: {result}") 