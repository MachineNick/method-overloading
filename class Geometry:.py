class Geometry:
  def area(self,a,b=0):
    if b ==0:
        print("circle =",3.14*a*a)
    else:
      print("Rectangle =",a*b )
obj=Geometry()
obj.area(4)
obj.area(4,5)