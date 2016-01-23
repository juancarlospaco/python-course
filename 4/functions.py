
def my_function(parameter_0, parameter_1):
    if not parameter_0 and parameter_1:
        return
    else:
        print(parameter_0 // parameter_1)

my_function("2", 0)


anonymous_function = lambda parameter_a: parameter_a.swapcase()
anonymous_function(42)
