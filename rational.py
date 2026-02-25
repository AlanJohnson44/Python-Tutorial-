
import math

class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        # Reduce the fraction
        common_divisor = math.gcd(numerator, denominator)
        self._numerator = numerator // common_divisor
        self._denominator = denominator // common_divisor
        
        # Standardize the negative sign to the numerator
        if self._denominator < 0:
            self._numerator = -self._numerator
            self._denominator = -self._denominator

    def getNumerator(self):
        return self._numerator

    def getDenominator(self):
        return self._denominator

    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)
        return f"{self._numerator}/{self._denominator}"

    def __add__(self, other):
        new_num = (self._numerator * other._denominator) + (other._numerator * self._denominator)
        new_den = self._denominator * other._denominator
        return Rational(new_num, new_den)

    def __sub__(self, other):
        new_num = (self._numerator * other._denominator) - (other._numerator * self._denominator)
        new_den = self._denominator * other._denominator
        return Rational(new_num, new_den)

    def __mul__(self, other):
        return Rational(self._numerator * other._numerator, self._denominator * other._denominator)

    def __eq__(self, other):
        return (self._numerator == other._numerator) and (self._denominator == other._denominator)

    def __lt__(self, other):
        return (self._numerator * other._denominator) < (other._numerator * self._denominator)

    def __gt__(self, other):
        return (self._numerator * other._denominator) > (other._numerator * self._denominator)


# --- Helper functions for safe user input ---
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_denominator(prompt):
    while True:
        val = get_integer(prompt)
        if val == 0:
            print("Denominator cannot be zero. Please try again.")
        else:
            return val

# --- User Input Implementation ---
if __name__ == "__main__":
    print("--- Rational Number Calculator ---")
    
    # 1. Get input for the first fraction
    print("Enter the details for Fraction 1:")
    num1 = get_integer("  Numerator: ")
    den1 = get_denominator("  Denominator: ")
    r1 = Rational(num1, den1)
    
    # 2. Get input for the second fraction
    print("\nEnter the details for Fraction 2:")
    num2 = get_integer("  Numerator: ")
    den2 = get_denominator("  Denominator: ")
    r2 = Rational(num2, den2)
    
    # 3. Print the results of the overloaded operations
    print("\n--- Results ---")
    print(f"Fraction 1 (Reduced): {r1}")
    print(f"Fraction 2 (Reduced): {r2}")
    print("-" * 20)
    print(f"Addition ({r1} + {r2}): {r1 + r2}")
    print(f"Subtraction ({r1} - {r2}): {r1 - r2}")
    print(f"Multiplication ({r1} * {r2}): {r1 * r2}")
    print("-" * 20)
    print(f"Are they equal? ({r1} == {r2}): {r1 == r2}")
    print(f"Is Fraction 1 less than Fraction 2? ({r1} < {r2}): {r1 < r2}")
    print(f"Is Fraction 1 greater than Fraction 2? ({r1} > {r2}): {r1 > r2}")
