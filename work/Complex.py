
class my_complex:

    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def __add__(self, c):
        return my_complex(self.real + c.real, self.imag + c.imag)

    def __isub__(self, c):
        return my_complex(self.real - c.real, self.imag - c.imag)

    def __sub__(self, c):
        return my_complex(self.real - c.real, self.imag - c.imag)

    def __str__(self):
        if self.imag < 0:
            return "({}{}j)".format(self.real, self.imag)
        return "({}+{}j)".format(self.real, self.imag)

    def __eq__(self, c):
        if not isinstance(c, my_complex):
            return False
        return self.real == c.real and self.imag == c.imag

    def conjugate(self):
        return my_complex(self.real, -self.imag)
