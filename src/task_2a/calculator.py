import re


class Calculator:
    __errors = []
    __expression = ''
    __operators = {
        '-': lambda a, b: a - b,
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    def __init__(self, expression):
        self.__errors = []
        self.__expression = expression.replace(' ', '')

    @property
    def errors(self):
        return self.__errors

    # Calculate with semantic analyzer
    def calc(self):
        try:
            analizer = Analyzer()
            analizer.tokenize(self.__expression)
        except Exception as e:
             self.__errors.append(str(e))
        else:
            return self.__calculate_rpn(analizer.stack)

    # Calculate Reverse Polish Notation
    def __calculate_rpn(self, rpn):
        self.__operators
        res = []
        for val in rpn:
            if val in self.__operators:
                op2 = res.pop()
                op1 = res.pop()
                res.append(self.__operators[val](float(op1), float(op2)))
            else:
                res.append(val)
        return res[0]

    # This is a very simple implementation of task
    def simple_calc(self):
        try:
            return eval(self.__expression)
        except Exception as e:
            self.__errors.append(str(e))
            return None


class Analyzer:
    token_re = re.compile(r"""
    (?P<numbers>(\d*\.\d+|\d+))
    |(?P<operators>[+-/*])
    |(?P<open_bracket>[(])
    |(?P<close_bracket>[)])
    """, re.VERBOSE)

    __stack = None
    __operators = None
    __nnegative = False  # flag that next is a negative number

    def __init__(self):
        self.__stack = []
        self.__operators = []

    @property
    def stack(self):
        return self.__stack

    def tokenize(self, expression):
        pos = 0
        while True:
            token = self.token_re.match(expression, pos)
            if not token:
                break
            pos = token.end()
            self.__to_ast(token.lastgroup, token.group(token.lastgroup))
        while len(self.__operators):
            op = self.__operators.pop(0)
            if op == '(':
                raise Exception('Check the brackets')
            self.__stack.append(op)

    # Shunting-yard algorithm
    def __to_ast(self, groupname, value):
        if groupname == 'open_bracket':
            self.__operators.insert(0, value)
        elif groupname == 'close_bracket':
            while True:
                op = self.__operators.pop(0)
                if op == '(':
                    break
                elif not op:
                    raise Exception('Check the brackets')
                self.__stack.append(op)
        elif groupname == 'operators':
            ###
            # The next condition needs for negative numbers,
            # especially at begin of the expression or after the bracket:
            # e.g.: -3 * ..., (-6.8 + ...)
            ###
            if (len(self.__stack) == 0 or
                (len(self.__operators) > 0 and self.__operators[0] == '(')) and value == '-':
                self.__nnegative = True
            else:
                self.__precedence(value)
        elif groupname == 'numbers':
            if self.__nnegative:
                value = '-' + value  # because right now - this is a string
                self.__nnegative = False
            self.__stack.append(value)

    # Calculate precedence of operators
    def __precedence(self, op):
        prec = {'*': 3, '/': 3, '-': 2, '+': 2}
        ret = None
        ###
        # The main rules:
        # 1. all highest operators should be append to the operators stack;
        # 2. all equal operators or lower by precedence should be append to value stack
        # 3. stop on open brackets
        ###
        if len(self.__operators) > 0:
            # stop if the next operator is "("
            if self.__operators[0] == '(':
                self.__operators.insert(0, op)
                return
            while True:
                if len(self.__operators) == 0 or self.__operators[0] not in prec:
                    break
                if prec[op] <= prec[self.__operators[0]]:
                    self.__stack.append(self.__operators.pop(0))
                else:
                    break
            self.__operators.insert(0, op)
        else:
            self.__operators.insert(0, op)

