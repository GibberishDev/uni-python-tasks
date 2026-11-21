import math
def triangle_area(base,height):
    print(f"Triangle area is: {format(float(0.5*base*height),'.2f')}")
def rectangle_area(height:float,width:float):
    print(f"Rectangle area is: {format(float(height*width),'.2f')}")
def circle_area(radius:float):
    print(f"Circle area is: {format(float(radius**2*math.pi),'.2f')}")
choice=str(input("Which shape do you want to calculate area of?\n[triangle/rectrangle/circle]: "))
match choice.lower():
    case "triangle"|"t"|"1"|"tri":
        triangle_area(float(input("Enter base of the triangle: ")),float(input("Enter height of the triangle: ")))
    case "rectangle"|"r"|"2"|"rec":
        rectangle_area(float(input("Enter height of the rectangle: ")),float(input("Enter width of the rectangle: ")))
    case "circle"|"c"|"3"|"cir":
        circle_area(float(input("Enter radius of the circle: ")))
    case _:
        print("Invalid choice")
