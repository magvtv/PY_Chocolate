# """
#     Using bisector method to solve the root of a given non-linear polynomial equation
# """

# import math
# import timeit

# start_time = timeit.default_timer()
# def f(x, a, b, c, d):
#     return a * x**3 + b * x**2 + c * x + d


# def bisection_method(a, b, c, d, xl, xu, es, imax):
#     fl = f(xl, a, b, c, d)
#     fu = f(xu, a, b, c, d)
#     if fl * fu > 0:
#         return None, None, None

#     xr_old = None
#     xr = (xl + xu) / 2
#     ea = 100
#     i = 0

#     while i < imax and ea > es:
#         xr_old = xr
#         xr = (xl + xu) / 2
#         fr = f(xr, a, b, c, d)

#         if fr == 0:
#             ea = 0
#         else:
#             ea = abs((xr - xr_old) / xr) * 100

#         if fl * fr < 0:
#             xu = xr
#         elif fl * fr > 0:
#             xl = xr
#             fl = fr
#         else:
#             ea = 0

#         i += 1

#     return xr, f(xr, a, b, c, d), ea


# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
# d = float(input("Enter coefficient d: "))

# xl = float(input("Enter lower bound: "))
# xu = float(input("Enter upper bound: "))

# es = float(input("Enter desired relative error (e.g. 0.01 for 1%): "))
# imax = int(input("Enter maximum number of iterations: "))

# root, froot, ea = bisection_method(a, b, c, d, xl, xu, es, imax)

# if root is None:
#     print("Error: the function has the same sign at both endpoints.")
# else:
#     print(f"Root: {root}")
#     print(f"f(root): {froot}")
#     print(f"Estimated error: {ea}%")

# end_time = timeit.default_timer()
# print(f"Exact duration of execution: {round((end_time- start_time), 2)}")


# def secant_method(f, x0, x1, tol=1e-6, max_iter=10):
#     """
#     Implementation of the Secant Method for finding roots of a given function f.
    
#     Args:
#     - f (function): The function whose root needs to be found.
#     - x0 (float): Initial guess for the root.
#     - x1 (float): Another initial guess for the root.
#     - tol (float, optional): Tolerance for convergence. Default is 1e-6.
#     - max_iter (int, optional): Maximum number of iterations. Default is 100.
    
#     Returns:
#     - float: The approximate root found using the Secant Method.
#     """
#     iter_count = 0
#     while abs(f(x1)) > tol and iter_count < max_iter:
#         x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
#         x0 = x1
#         x1 = x2
#         iter_count += 1

#     if iter_count == max_iter:
#         print("Secant Method did not converge within the specified maximum number of iterations!")
#     else:
#         print(f"Root found: {x1}")
#     return x1


# # Example usage:

# # Define the polynomial equation
# def f(x):
#     return x**3 - 5*x**2 + 4*x + 2


# # Initial guesses for the roots
# x0 = 0.5
# x1 = 1.0

# # Call the secant_method() function to find the root
# root = secant_method(f, x0, x1)
