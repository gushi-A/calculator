# calculator/calculations.py

"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

def add(a: float | int, b: float | int) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0


    Args:
        a: A number representing the first addend in the addition
        b: A number representing the second addend in the addition

    Returns:
        A number representing the arithmetic sum of `a` and `b`
    """
    return float(a + b)

def subtract(a: float | int, b: float | int) -> float:
    """Calculate the difference between two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a: A number representing the minuend in the subtraction.
        b: A number representing the subtrahend in the subtraction.

    Returns:
        A number representing the difference between `a` and `b`.
    """    
    return float(a - b)

def multiply(a: float | int, b: float | int) -> float:
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a: A number representing the multiplicand in the multiplication.
        b: A number representing the multiplier in the multiplication.

    Returns:
        A number representing the product of `a` and `b`.
    """    
    return float(a * b)

def divide(a: float | int, b: float | int) -> float:
    """Compute and return the quotient of two numbers.

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0
        >>> divide(4, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero

    Args:
        a: A number representing the dividend in the division.
        b: A number representing the divisor in the division.

    Raises:
        ZeroDivisionError: An error occurs when the divisor is `0`.

    Returns:
        A number representing the quotient of `a` and `b`.
    """     
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)