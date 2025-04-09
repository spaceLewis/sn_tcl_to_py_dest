

package util

import math

def add(a: float, b: float) -> float:
    """
    Returns the sum of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    try:
        return a + b
    except TypeError:
        raise TypeError("Both inputs must be numbers")

def subtract(a: float, b: float) -> float:
    """
    Returns the difference of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference of a and b.
    """
    try:
        return a - b
    except TypeError:
        raise TypeError("Both inputs must be numbers")

def multiply(a: float, b: float) -> float:
    """
    Returns the product of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    try:
        return a * b
    except TypeError:
        raise TypeError("Both inputs must be numbers")

def divide(a: float, b: float) -> float:
    """
    Returns the quotient of two numbers.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient of a and b.

    Raises:
        ValueError: If the divisor is zero.
    """
    try:
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
    except TypeError:
        raise TypeError("Both inputs must be numbers")
    """
    except ValueError as e:
        raise e

def power(a: float, b: float) -> float:
    """
    Returns the result of raising a number to a power.

    Args:
        a (float): The base.
        b (float): The exponent.

    Returns:
        float: The result of a raised to the power of b.
    """
    try:
        return a ** b
    except TypeError:
        raise TypeError("Both inputs must be numbers")

def sqrt(a: float) -> float:
    """
    Returns the square root of a number.

    Args:
        a (float): The number.

    Returns:
        float: The square root of a.

    Raises:
        ValueError: If the input is negative.
    """
    try:
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)
    except TypeError:
        raise TypeError("Input must be a number")

def log(a: float, base: float) -> float:
    """
    Returns the logarithm of a number with a given base.

    Args:
        a (float): The number.
        base (float): The base.

    Returns:
        float: The logarithm of a with base.

    Raises:
        ValueError: If the input is non-positive or the base is invalid.
    """
    try:
        if a <= 0:
            raise ValueError("Cannot calculate logarithm of non-positive number")
        if base <= 0 or base == 1:
            raise ValueError("Invalid base for logarithm")
        return math.log(a, base)
    except TypeError:
        raise TypeError("Both inputs must be numbers")

def sin(a: float) -> float:
    """
    Returns the sine of an angle.

    Args:
        a (float): The angle in radians.

    Returns:
        float: The sine of a.
    """
    try:
        return math.sin(a)
    except TypeError:
        raise TypeError("Input must be a number")

def cos(a: float) -> float:
    """
    Returns the cosine of an angle.

    Args:
        a (float): The angle in radians.

    Returns:
        float: The cosine of a.
    """
    try:
        return math.cos(a)
    except TypeError:
        raise TypeError("Input must be a number")

def tan(a: float) -> float:
    """
    Returns the tangent of an angle.

    Args:
        a (float): The angle in radians.

    Returns:
        float: The tangent of a.
    """
    try:
        return math.tan(a)
    except TypeError:
        raise TypeError("Input must be a number")

def asin(a: float) -> float:
    """
    Returns the arcsine of a number.

    Args:
        a (float): The number.

    Returns:
        float: The arcsine of a.

    Raises:
        ValueError: If the input is out of range.
    """
    try:
        if a < -1 or a > 1:
            raise ValueError("Invalid input for arcsine")
        return math.asin(a)
    except TypeError:
        raise TypeError("Input must be a number")

def acos(a: float) -> float:
    """
    Returns the arccosine of a number.

    Args:
        a (float): The number.

    Returns:
        float: The arccosine of a.

    Raises:
        ValueError: If the input is out of range.
    """
    try:
        if a < -1 or a > 1:
            raise ValueError("Invalid input for arccosine")
        return math.acos(a)
    except TypeError:
        raise TypeError("Input must be a number")

def atan(a: float) -> float:
    """
    Returns the arctangent of a number.

    Args:
        a (float): The number.

    Returns:
        float: The arctangent of a.
    """
    try:
        return math.atan(a)
    except TypeError:
        raise TypeError("Input must be a number")