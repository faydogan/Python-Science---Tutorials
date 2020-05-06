# TERNARY OPERATOR
"""
    Ternary operators (aka. three-piece operators) are used for 
    single line conditional assignments.

    In Python, ternary operators has two representations:
        (1) [on_true] if [conditional_exp] else [on_false]
            also can be used as nested ternary operations
            (([on_true] if [conditional_exp_1] else [on_false_true])
             if [conditional_exp_2] else [on_false_false])
        (2) (on_false, on_true)[conditonal_exp] also can be used as
            {True: on_true, False: on_false}[conditonal_exp]            
"""

k = 6
d = 5
m = 34
n = 97

# BASIC USE OF TERNARY OPERATORS

# Can use single ternary operator like below
max_value = k if k > d else d
print("The maximum of k and d is", max_value)

max_value = (d, k)[k > d]
print("The maximum of k and d is", max_value)

max_value = {True: k, False: d}[(k > d) or (d > m)]
print("The maximum of k and d is", max_value)

# Can use nested ternary operator like below
max_value2 = ((k if k > d else d) if d > m else m) if m > n else n
print("The maximum of k, d, m and n is", max_value2)

max_value2 = ((d, k)[k > d], m)[m > (d, k)[k > d]]
print("The maximum of k, d and m is", max_value2)

# Can use multiple condintion in a ternary operator d,k,m | m,k,d
middle_value = True if (k > d and k < m) or (k < d and k > m) else False
print("Is k the middle value of k, d and m:", middle_value)

#Ternary for imitating switch case
print({6: "Happy", 5:"Sad", 34:"Wow"}[k])