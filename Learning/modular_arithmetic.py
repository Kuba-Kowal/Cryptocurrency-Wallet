from math import trunc
# Congruent [≡] (Modular Arithmetic) ## Two numbers leave the same remainder when divided by a given number
#                                       This means that 17 ≡ 5 (mod 12) or 36 ≡ 10 (mod 26)

# Modulus can be described as a limiter set on the two numbers 
# For every mod, the value starts at 0 and ends at 1 less than N (mod N).

# https://www.youtube.com/watch?v=Eg6CTCu8iio Introduction to modular arithmetic. Explains the formula utilised for the non-extended euclidian algorithm
# Greated Common Divisor
# n = qm + R is the equation utilised to retrieve the required mod to create a congruent equation.abs
# n: The number that is to be converted
# q: The variable number decided to make the statement congruent
# m: The mod value placed upon "q" to make the statement congruent
# r: The reaminder of the modulus equation

# FINDING THE GREATEST COMMON DIVISOR (The largest number that divides into 2 numbers without leaving a remainder)
# Get your 2 variables
n = 252
q = 198

# Finding the integer quotient 
m = (n // q)            # The integer quotient tells us how many whole times b divides into a
#                        based on this we know that if you multiply the number being divided into by the truncated modulus we are left with "x" The decimal part after the whole number
#                           
#                        You can figure out whether there is a remainder by multiply (the number being divided into) by the quotient. If there is a difference "x" between that number and the divided number.
#                        Then the problem can be replaced by a smaller one that has the same GCD.a
#
#                        Picture we had a: 48, b: 18.      m = trunc(48 / 18) ∣ 2
#                                                          48 = 2 * 18 + 12.
#       
#                                               Therefore  GCD(48,18) = GCD(18,12)
#                        
#                        If d, divides both 48 and 18, then it must also divide any whole number combination of them, such as 48 - 2 * 18.
#                        So every common divisor of 48 and 18, is also a divisor of 12. Because if d can divide both pieces on the right hand side. It must also divide their sum
# 

# EUCLIDIEN ALGORITHM

# Now it's time to find the GCD for 252 and 198.
# 
# So we plug these numbers back into the equation, replacing "n" with "q" AND "q" with "r". And calculating the new integer quotient
def test():
    r = int
    while r != 0:           # Until our remainder is 0, which means the number cannot be split up even more and is common factor of both numbers.
        m = (n // q)        # This creates a table of results
    #                           252 = 198(1) + 54
        r = n - (q*m)       #   198 = 54(3)  + 36
    #                           54  = 36(1)  + 18
        print(r)            #   36  = 18(2)  + 0            

        n = q               # The reason why the remainder replaces the value of q (the smaller number). Is because its a combination of n and q.
        q = r               # It essentially carries the information removed by the quotient about their other common divisors.

    #                       So now we know how to calculate the GCD, for the case of 2 distinct prime numbers, the GCD will ALWAYS be 1.

# https://www.youtube.com/watch?v=Jwf6ncRmhPg  Provides a visualisation as to why it works. Good for conceptualisation.
# https://www.youtube.com/watch?v=7dA8tR_LUOA  Explains the actual algorithm
# THE EXTENDED EUCLIDIEN ALGORITH
# GCD(a,b) = ax + by
# We now know that GCD(252, 198) = 18   Based on the table above.
# Now the goal is to make an equation for every step of calculating the GCD, where R is by itself
#                           n   = qm     + r      ->     r  = n   - qm
#                           252 = 198(1) + 54            54 = 252 - 198(1)          [Equation 3]
#                           198 = 54(3)  + 36            36 = 198 - 54(3)---∣        [Equation 2]
#                           54  = 36(1)  + 18            18 = 54  - 36(1)   ∣        [Equation 1]
#                           36  = 18(2)  + 0                                ∣
#                                                                           ∣
#                           We take the first equation                      ∣
#                           18 = 54 - 36(1)  ∣-------------------------------
#                                            ∣
#                           18 = 54 - (198 - 54(3))(1)  Substitue the value of 36, into the equation.
#                           
#                           18 = 54 - 198 + 54(3)       This can be re-written. The 1 cancels itself out, while a "-" before a parenthesis is equivelant to multiplying everything by 1 # -1(198 - 54(3))
#
#                           18 = 54(4) - 198            This can be re-written
#
#                           Now we take the third equation. The top one.
#                           18 = (252 - 198(1))(4) - 198
#
#                           18 = 4(252 - 198) - 198
#
#                           18 = 252(4) - 198(5)
#
#                           GCD(252, 198) = 252x + (-198y)
def euclidean(a, b):
    eq_list = {}
    eq_number = s
    # b = am + r
    m = (b // a)
    r = b - am

    
def extended_euclidean():
    a = 252
    b = 198

    while a != 0 or b != 0:
        if a > b:
            a = b
            b = a
        

# For runtime, the extended euclidean algorith:
# O(log(min(a,b)))

# MODULAR INVERSES
def inverse_mod(n):
    least_residue = [i for i in range(1, n)]
    inverses = {}
    
    for a in least_residue:
        for b in least_residue:
            if ((a * b) % n) == 1:
                inverses[a] = b
                break

    return inverses

print(inverse_mod(n=9))

def standard_euclidean_algorithm(a, b):
    list_of_equations = {}

    start_a = a
    start_b = b
    r = a % b
    i = 1
    # a = bq + r
    while r != 0:
        q = a // b

        r = a % b

        list_of_equations[r] = {
            "a": a,
            "b": b,
            "r": r,
            "q": q
        }

        if r != 0:
            a = b
            b = r

    print(f"\nGCD({start_a},{start_b}) = {b}")

    return dict(reversed(list_of_equations.items())), b

print(standard_euclidean_algorithm(252,198))

def extended_euclidean_algorithm(list_of_equations, gcd): # Allows us to express the GCD of 2 numbers as ax + by where a and y are known as bezouts coefficients
    for i, values in list_of_equations.items():
        temp_sub = 1
        if i == 0:
            continue

        the_equation = "gcd = values.a - (values.b * values.q)"

        if values.b in list_of_equations.values():
            new_values = list_of_equations[values.b]

            new_equation = "gcd = values.a - (new_values.a - (new_values.b * new_values.q) * values.q"


        
        

list_of_equations, gcd = standard_euclidean_algorithm(252, 198)
print(extended_euclidean_algorithm(list_of_equations, gcd))
# These have to be prime because when being factored they cannot be broken down into more than those two factors. Which means the eonly factors they will share are 1
# For example if you have 12 * 18 thats the same as 2 * 2 * 2 * 3 * 3 * 3. While if you have 5 * 11. those will always be the lowest common factors.
p = 5
q = 11

# This number becomes part of the public key


# FERMAT'S LITTLE THEOREM
# a^p ≡ a (mod p) 
# a^p-1 ≡ 1 (mod p)

def fermat_theorem_test():
    a = 5 # Random number not divisible by p (p ∤ a)
    p = 113 # Prime Number

    print("A TO POWER OF P")
    print((a**p))

    print("\nA^P-1 MOD P")
    remainder = ((a**(p-1)) % p)
    print(remainder)
    print("\n1 MOD P")
    print(1 % p)
