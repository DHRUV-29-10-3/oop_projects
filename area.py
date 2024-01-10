class Rectangle:

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        perimeter = 2*self.length+2*self.breadth
        return perimeter

    def area(self):
        return self.length*self.breadth

    def display(self):
        print(f"length of rectangle is : {self.length}")
        print(f"breadth of rectangle is : {self.breadth}")
        print(f"perimeter of a rectangle is : {self.perimeter()}")
        print(f"area of a rectangle is {self.area()}")

my_rectangle = Rectangle(3 , 4)
my_rectangle.display()