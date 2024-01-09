class Fraction:
    def __init__(self,num,den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self,other):
        new_num = self.num*other.den+self.den*other.num
        new_den = self.den*other.den
        return f"{new_num}/{new_den}"

    def __sub__(self,other):
        new_num = self.num*other.den-self.den*other.num
        new_den = self.den*other.den
        return f"{new_num}/{new_den}"

    def __mul__(self,other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        return f"{new_num}/{new_den}"

    def __truediv__(self,other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        return f"{new_num}/{new_den}"


fr1 = Fraction(5,4)
fr2 = Fraction(3,4)

print(fr1,fr2)
print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)