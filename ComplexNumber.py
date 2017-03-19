import sys


class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __sub__(self, obj):
        return ComplexNumber(self.real - obj.real,
                             self.imaginary - obj. imaginary)

    def __add__(self, obj):
        return ComplexNumber(self.real + obj.real,
                             self.imaginary + obj. imaginary)

    def __mul__(self, obj):
        f = self.real * obj.real - self.imaginary * obj.imaginary
        s = self.imaginary * obj.real + self.real * obj.imaginary
        return ComplexNumber(f, s)

    def __truediv__(self, obj):
        chisl = ComplexNumber(obj.real, -obj.imaginary)
        chisl = self * chisl
        znam = obj.real ** 2 + obj.imaginary ** 2
        return ComplexNumber((chisl.real / znam), (chisl.imaginary / znam))

    def __str__(self):
        s = ''
        if self.real == 0 and self.imaginary == 0:
            s = '0.00'
        elif self.real == 0:
            if self.imaginary < 0:
                s = "%.2f" % self.imaginary + "i"
            else:
                s = "%.2f" % self.imaginary + "i"
        elif self.imaginary == 0:
            s = "%.2f" % self.real
        elif self.imaginary < 0:
            s = "%.2f" % self.real + " - " + "%.2f" % (-self.imaginary) + "i"
        else:
            s = "%.2f" % self.real + " + " + "%.2f" % self.imaginary + "i"
        return s

if __name__ == "__main__":
    for line in sys.stdin.readlines():
        print(eval(line.strip()))
