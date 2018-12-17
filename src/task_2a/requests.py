
class RequestCheck:
    __expression = ''
    __simplify = False
    __errors = []

    def __init__(self, request):
        self.__errors = []
        json = request.get_json()
        if json:
            if 'expression' in json:
                self.__expression = json['expression']
            if 'simplify' in json:
                self.__simplify = json['simplify']
        if self.__expression == '':
            self.__errors.append('Request should contain an expression')

    @property
    def expression(self):
        return self.__expression

    @property
    def errors(self):
        return self.__errors

    @property
    def simplify(self):
        return self.__simplify

    def is_correct(self):
        return len(self.errors) == 0
