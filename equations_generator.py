"""
Complex equations generator
Author: Nick  Chaplahin, 2025
Copyright: Nick Chaplahin

Automatic equations generator.
Configurable:
- number of values in equation
- values types, probabilities to appear in equation,  and ranges. On adding new types add its support in
     _service_generate_value()
- operations of equation.  On adding new operations add its support to _service_apply_action()
- probabilities of operands to appear in equation

returns:
- equation in string format
- result of equation
- equation in LaTeX format   (on adding new operation add support for LaTeX in  _service_apply_action()

"""

import fractions
import math  # math import is required for eval execution when math.log, math.e or any other math.xxx available.
import random


class EquationGenerator:
    def _service_generate_value(self):
        types = list(self.type_ranges.keys())
        value_type = random.choices(types, weights=self.type_probabilities)[0]

        if value_type == "integer":
            num = random.randint(self.type_ranges["integer"][0], self.type_ranges["integer"][1])
            while num == 0:
                num = random.randint(self.type_ranges["integer"][0], self.type_ranges["integer"][1])
            return {'str': str(num), 'eval_str': str(num), 'latex_str': str(num), 'num': num}
        elif value_type == 'float':
            num = round(random.uniform(self.type_ranges["float"][0], self.type_ranges["float"][1]), 5)
            while num == 0.0:
                num = round(random.uniform(self.type_ranges["float"][0], self.type_ranges["float"][1]), 5)
            return {'str': f"{num:.5f}", 'eval_str': f"{num:.5f}", 'latex_str': f"{num:.5f}", 'num': num}
        else:  # fraction
            numerator = random.randint(self.type_ranges["fraction"][0][0], self.type_ranges["fraction"][0][1])
            while numerator == 0:
                numerator = random.randint(self.type_ranges["fraction"][0][0], self.type_ranges["fraction"][0][1])
            denominator = random.randint(self.type_ranges["fraction"][1][0], self.type_ranges["fraction"][1][1])
            while denominator == 0:
                denominator = random.randint(self.type_ranges["fraction"][1][0], self.type_ranges["fraction"][1][1])
            num = fractions.Fraction(numerator, denominator)
            str_val = f"({num.numerator}/{num.denominator})"
            return {'str': str_val, 'eval_str': str_val,
                    'latex_str': f"\\frac{{{num.numerator}}}{{{num.denominator}}}", 'num': num}

    def _service_apply_action(self, left, right, action):
        left_str, left_eval, left_latex, left_num = left['str'], left['eval_str'], \
            left['latex_str'], left['num']
        right_str, right_eval, right_latex, right_num = right['str'], right['eval_str'], \
            right['latex_str'], right['num']

        try:
            if action == 'add':
                return f"{left_str} {self.operation_operands['add']} {right_str}", f"{left_eval} + {right_eval}", \
                    f"{left_latex} + {right_latex}", left_num + right_num
            elif action == 'sub':
                return f"{left_str} {self.operation_operands['sub']} {right_str}", f"{left_eval} - {right_eval}", \
                    f"{left_latex} - {right_latex}", left_num - right_num
            elif action == 'multiply':
                return f"{left_str} {self.operation_operands['multiply']} {right_str}", f"{left_eval} * {right_eval}", \
                    f"{left_latex} * {right_latex}", left_num * right_num
            elif action == 'divide':
                if right_num == 0:
                    raise ZeroDivisionError
                return f"{left_str} {self.operation_operands['divide']} {right_str}", f"{left_eval} / {right_eval}", \
                    f"{left_latex} / {right_latex}", left_num / right_num
            elif action == 'power':
                result = eval(f"{left_eval} ** {right_eval}")
                if isinstance(result, complex):
                    raise ValueError
                return f"{left_str}{self.operation_operands['power']}{right_str}",\
                    f"{left_eval} ** {right_eval}", f"{left_latex}^{{{right_latex}}}", result
            elif action == 'logarithm':
                if left_num <= 0 or left_num == 1 or right_num <= 0:
                    raise ValueError
                result = eval(f"math.log({right_eval}, {left_eval})")
                return self.operation_operands['logarithm'].format(right_str, left_str), \
                    f"math.log({right_eval}", f"{left_eval})", f"\\log_{{{left_latex}}}({right_latex})", result
            elif action == 'euler_num':
                result = eval(f"{left_eval} * math.e ** {right_eval}")
                return self.operation_operands['euler_num'].format(left_str, right_str), \
                    f"{left_eval} * math.e ** {right_eval}", f"{left_latex} * e^{{{right_latex}}}", result
        except (ValueError, ZeroDivisionError, OverflowError):
            raise ValueError

    def generate_equation(self):
        actions = list(self.operation_probabilities.keys())
        weights = list(self.operation_probabilities.values())
        values_num = random.randint(self.values_num[0], self.values_num[1])
        values = [self._service_generate_value() for _ in range(values_num)]

        while len(values) > 1:
            i = random.randint(0, len(values) - 2)
            left = values.pop(i)
            right = values.pop(i)
            action = random.choices(actions, weights=weights)[0]
            try:
                new_str, new_eval, new_latex, new_num = self._service_apply_action(left, right, action)
                if random.random() < self.expression_probability:
                    new_str = f"({new_str})"
                    new_eval = f"({new_eval})"
                    new_latex = f"({new_latex})"

                values.insert(i, {'str': new_str, 'eval_str': new_eval, 'latex_str': new_latex, 'num': new_num})
            except ValueError:
                # Insrt values back for future use
                values.insert(i, right)
                values.insert(i, left)
                continue

        try:
            self.result = eval(values[0]['eval_str'])
            self.equation = values[0]['str']

            self.latex_equation = f"${values[0]['latex_str']}$"
        except(ZeroDivisionError, OverflowError):
            print(f"ERROR: {values[0]['eval_str']}")
            print(f"ERROR: {self.latex_equation}")

        # Convert result to appropriate type
        if isinstance(self.result, fractions.Fraction):
            self.result = float(self.result) if self.result.denominator != 1 else int(self.result)
        elif isinstance(self.result, float):
            self.result = round(self.result, 4)

    def set_values_num(self, values):
        if not isinstance(values, tuple):
            raise ValueError("ERROR: values should be a tuple")
        if len(values) != 2:
            raise ValueError("ERROR: values should be a tuple containing exactly 2 values")
        if values[0]> values[1]:
            raise ValueError("ERROR: values should be a tuple (min,max)")
        self.values_num = values

    def get_values_num(self):
        return self.values_num

    def get_types(self):
        return list(self.type_ranges.keys())

    def set_type_ranges(self, ranges):
        if not isinstance(ranges, dict):
            raise ValueError("ERROR: Type Ranges should be a dict")
        self.type_ranges = ranges.copy()

    def get_type_ranges(self):
        return self.type_ranges

    def set_operation_probabilities(self, probabilities):
        if not isinstance(probabilities, dict):
            raise ValueError("ERROR: Operation probabilities must be a dict")
        self.operation_probabilities = probabilities.copy()

    def get_operation_probabilities(self):
        return self.operation_probabilities

    def set_operation_operands(self, operands):
        if not isinstance(operands, dict):
            raise ValueError("ERROR: Operation probabilities must be a dict")
        self.operation_operands = operands.copy()

    def get_operation_operands(self):
        return self.operation_operands

    def set_expression_probability(self, probability):
        self.expression_probability = probability

    def get_expression_probability(self):
        return self.expression_probability

    def get_info(self):
        return self.equation, self.result

    def get_equation(self):
        return self.equation

    def get_latex_equation(self):
        return self.latex_equation

    def get_result(self):
        return self.result

    def __init__(self):
        # Configuration parameters
        self.values_num = (20, 30)
        self.type_probabilities = [0.4, 0.4, 0.2]  # [integer, float, fraction]
        self.type_ranges = {
            "integer": (-200, 200),
            "float": (-200.0, 200.0),
            "fraction": ((-200, 200), (-400, 400))
        }
        self.operation_probabilities = {
            'add': 0.25,
            'sub': 0.25,
            'multiply': 0.15,
            'divide': 0.15,
            'power': 0.1,
            'logarithm': 0.05,
            'euler_num': 0.05
        }
        self.operation_operands = {
            'add': '+',
            'sub': '-',
            'multiply': '*',
            'divide': '/',
            'power': ' ** ',
            'logarithm': 'log({}, {})',
            'euler_num': '{} * e^{}'
        }
        self.expression_probability = 0.3
        self.equation = ""
        self.latex_equation = ""
        self.result = 0
        # Generate equation
        self.generate_equation()


# Example Code
equation = EquationGenerator()
equation.set_values_num((10, 15))
for idx in range(5):
    equation.generate_equation()
    print("Equation: {}".format(equation.get_equation()))
    print("LaTeX Equation: {}".format(equation.get_latex_equation()))
    print("Result: {}".format(equation.get_result()))
operation_text_operands = {
    'add': 'add',
    'sub': 'sub',
    'multiply': 'multiply by',
    'divide': 'divide by',
    'power': 'power to',
    'logarithm': 'logarithm of {} base {}',
    'euler_num': '{} multiply by e power to {}'
}
equation.set_operation_operands(operation_text_operands)
for idx in range(5):
    equation.generate_equation()
    print("Equation: {}".format(equation.get_equation()))
    print("LaTeX Equation: {}".format(equation.get_latex_equation()))
    print("Result: {}".format(equation.get_result()))
