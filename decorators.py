# def outer_function(msg):
#     print("Abhishek.....")

#     def inner_function():
#         print(msg)
#     return inner_function


# a = outer_function('hi')
# a()


# decorator
def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed")
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("display function ran")


# decorated_display = decorator_function(display)
# decorated_display()

display()