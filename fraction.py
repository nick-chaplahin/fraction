"""
Copyright by Nick Chaplahin 2024. All rights reserved, but you can use it, if do not forget to mention me as an author.
Part of Entire Math project.
"""

from math import gcd

# Element of the Fraction can be Integer or Fraction.


class Fraction:
    def __new__(cls, numerator, denominator=1):
        if (not isinstance(numerator, int) and not isinstance(numerator, Fraction)) or \
                (not isinstance(denominator, int) and not isinstance(denominator, Fraction)):
            print("ERROR: numerator and denominator must be Integer or Fraction")
            return None
        if numerator is None:
            print("ERROR: Numerator is None, Fraction can not be initiated")
            return None
        if numerator == 0:
            # print("WARNING: Numerator is 0, entire number is 0")
            numerator = 0
            denominator = 1
        if denominator is None:
            print("ERROR: Denominator is None, Fraction can not be initiated")
            return N0ne
        if denominator == 0:
            print("ERROR: Denominator is 0, number can not be initiated")
            return None
        new_class = super().__new__(cls)
        return new_class

    def __init__(self, numerator, denominator=1):
        """
            Constructor for Fraction. Applies Numerator and Denominator.
            Numerator and Denominator can be Fractions themselves.
            Denominator can not be 0
        :param numerator:    Numerator of the Fraction. Must be Integer or Fraction
        :param denominator:  Denominator of the Fraction. Must be Integer or Fraction
        """
        # Verification of initial values to avoid unacceptable combinations
        if numerator == 0:
            # print("WARNING: Numerator is 0, entire number is 0")
            numerator = 0
            denominator = 1
        # Applying initial values
        self.numerator = numerator
        self.denominator = denominator

    def bring_to_general(self):
        """
           Function that brings Fraction into simple int/int structure, if it contains Fraction(s) in numerator or
           denominator. After simplifying structure to int/int function divs numerator and denominator by common
           divisor to minimize numbers.
           IMPORTANT: For DEMO reasons this function is not called automatically and should be called
           from DEMO code before operations with Fractions.
        :return:
            No return, simplifies internal data structure of self.numerator and self.denominator.
        """
        # Fraction processing
        if isinstance(self.numerator, Fraction):
            self.numerator.bring_to_general()
            absolute_numerator = self.numerator.get_numerator()
            absolute_denominator = self.numerator.get_denominator()
        else:
            absolute_numerator = self.numerator
            absolute_denominator = 1
        if isinstance(self.denominator, Fraction):
            self.denominator.bring_to_general()
            absolute_denominator = absolute_denominator * self.denominator.get_numerator()
            absolute_numerator = absolute_numerator * self.denominator.get_denominator()
        else:
            # absolute_numerator is unchanged
            # absolute denominator updated with actual denominator
            absolute_denominator = absolute_denominator * self.denominator

        # Sign processing
        if absolute_numerator < 0 and absolute_denominator < 0:
            absolute_numerator = abs(absolute_numerator)
            absolute_denominator = abs(absolute_denominator)
        elif absolute_denominator < 0:
            absolute_numerator = 0 - absolute_numerator
            absolute_denominator = abs(absolute_denominator)

        if absolute_denominator == 0:
            print("ERROR: Denominator become 0, not acceptable, returning None")
            return None
        if absolute_numerator == 0:
            absolute_denominator == 1
        self.numerator = absolute_numerator
        self.denominator = absolute_denominator
        common_divisor = gcd(absolute_numerator, absolute_denominator)
        self.numerator = self.numerator // common_divisor
        self.denominator = self.denominator // common_divisor

    def add(self, second):
        """
           Function to sum two Fractions. Fractions must be brought to general calling bring_to_general function.
        :param second: Will sum THIS Fraction with Second Fraction.
        :return:
            Fraction - result of sum operations with 2 Fractions.
        """
        if isinstance(self.numerator, Fraction) or \
                isinstance(self.denominator, Fraction) or \
                isinstance(second.numerator, Fraction) or \
                isinstance(second.denominator, Fraction):
            print("ERROR: Fractions must be simplified before operations!")
            return None
        numerator = (self.numerator * second.denominator +
                     second.numerator * self.denominator)
        denominator = self.denominator * second.denominator
        return Fraction(numerator, denominator)

    def sub(self, second):
        """
           Function to sub two Fractions. Fractions must be brought to general calling bring_to_general function.
        :param second: Will sub Second Fraction from THIS Fraction.
        :return:
            Fraction - result of sub operations with 2 Fractions.
        """
        if isinstance(self.numerator, Fraction) or \
                isinstance(self.denominator, Fraction) or \
                isinstance(second.numerator, Fraction) or \
                isinstance(second.denominator, Fraction):
            print("ERROR: Fractions musct be simplified before operations!")
            return None
        numerator = (self.numerator * second.denominator -
                     second.numerator * self.denominator)
        denominator = self.denominator * second.denominator
        return Fraction(numerator, denominator)

    def mul(self, second):
        """
           Function to multiply two Fractions. Fractions must be brought to general calling bring_to_general function.
        :param second: Will multiply THIS Fraction by Second Fraction.
        :return:
            Fraction - result of multiply operations with 2 Fractions.
        """
        if isinstance(self.numerator, Fraction) or \
                isinstance(self.denominator, Fraction) or \
                isinstance(second.numerator, Fraction) or \
                isinstance(second.denominator, Fraction):
            print("ERROR: Fractions musct be simplified before operations!")
            return None
        numerator = self.numerator * second.numerator
        denominator = self.denominator * second.denominator
        return Fraction(numerator, denominator)

    def div(self, second):
        """
           Function to divide two Fractions. Fractions must be brought to general calling bring_to_general function.
        :param second: Will divide THIS Fraction by Second Fraction.
        :return:
            Fraction - result of divide operations with 2 Fractions.
        """
        if isinstance(self.numerator, Fraction) or \
                isinstance(self.denominator, Fraction) or \
                isinstance(second.numerator, Fraction) or \
                isinstance(second.denominator, Fraction):
            print("ERROR: Fractions musct be simplified before operations!")
            return None
        if second.numerator == 0:
            print("ERROR: Cannot divide by zero.")
            return None
        numerator = self.numerator * second.denominator
        denominator = self.denominator * second.numerator
        if denominator == 0:
            print("ERROR: Denominator become 0, not acceptable, returning None")
            return None
        return Fraction(numerator, denominator)

    def power(self, power=1):
        """
           Function to power Fraction. Power value must be integer.
        :param power: Power value to apply to THIS fraction.
        :return:
            Fraction - result of power operations on THIS Fraction
        """
        if power != int(power):
            print("ERROR: power should be real value")
            return None
        if power == 0:
            return Fraction(1, 1)
        numerator, denominator = self.get()
        if power == 1:
            return Fraction(numerator, denominator)
        if power < 0:
            numerator = self.numerator ** abs(power)
            denominator = self.denominator ** abs(power)
            return Fraction(denominator, numerator)
        return Fraction(self.numerator ** power, self.denominator ** power)

    # ============================== Getters and Describe operations

    def get_numerator(self):
        """
            Returns numerator of the Fraction
        """
        return self.numerator

    def get_denominator(self):
        """
            Returns denominator of the Fraction
        """
        return self.denominator

    def get(self):
        """
            Returns numerator and denominator of the Fraction
        """
        return self.numerator, self.denominator

    def get_integer(self):
        """
            Returns integer part of the Fraction
        """
        if isinstance(self.numerator, Fraction) or isinstance(self.denominator, Fraction):
            print("ERROR: Integer part can be detected after simplification only!")
            return None
        if self.numerator == 0:
            return 0
        if abs(self.numerator) < abs(self.denominator):
            if self.numerator < 0:
                return -1
            else:
                return 1
        if self.numerator < 0:
            return 0 - (abs(self.numerator) // self.denominator)
        else:
            return self.numerator // self.denominator

    def get_remainder(self):
        """
            Returns remainder part of the Fraction
        """
        if isinstance(self.numerator, Fraction) or isinstance(self.denominator, Fraction):
            print("ERROR: Reminder part can be detected after simplification only!")
            return None
        remainder = abs(self.numerator) % self.denominator
        if remainder == 0:
            remainder = 1
        return remainder, self.denominator

    def get_absolute_result(self):
        """
            Returns float result of numerator divide by denominator
        """
        if isinstance(self.numerator, Fraction) or isinstance(self.denominator, Fraction):
            print("ERROR: Absolute result can be calculated after simplification only!")
            return None
        return self.numerator/self.denominator

    def describe(self):
        """
            Returns text representation of the Fraction
        """
        if isinstance(self.numerator, Fraction):
            general_numerator = "(" + self.numerator.describe() + ")"
        else:
            general_numerator = str(self.numerator)
        if isinstance(self.denominator, Fraction):
            general_denominator = "(" + self.denominator.describe() + ")"
        else:
            general_denominator = str(self.denominator)
        return "{} / {}".format(general_numerator, general_denominator)

# EQUATIONS