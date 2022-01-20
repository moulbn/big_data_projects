class Rectangle:
    def __init__(self, rectangle_area, rectangle_perimeter):
        self.rectangle_area = rectangle_area
        self.rectangle_perimeter = rectangle_perimeter

    def method_area(self):
        area= self.rectangle_area*self.rectangle_perimeter
        return area
        print("the area of the rectangle is",area)
  

    def method_perimeter(self):
        peri= 2*self.rectangle_area + 2*self.rectangle_perimeter
        return peri
        print("The perimeter of the rectangle is",peri)
    
    
    @staticmethod
    def static_method():
        return "Do you like rectangles?"