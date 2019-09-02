print("This is a triangle classification program")
a = int(input("Enter side one's length: "))
b = int(input("Enter side two's length: "))
c = int(input("Enter side three's length: "))

def classify_triangle(a,b,c):
    result=""
    max = a
    short1 = b
    short2 = c
    if b > max:
       max = b
       short1 = a
       short2 = c
    if c > max:
       max = c
       short1 = a
       short2 = b

    compare = short1 + short2
    a2 = short1 * short1
    b2 = short2 * short2
    pag = a2 + b2
    c2 = max * max

    if max>compare:
        print("This is not a triangle")
    else:
        x = 2
        if pag == c2:
            result = "This is a right triangle and "
        if a == b or a == c or b == c:
            if a == b == c:
                result = result + "This is an equilateral triangle"
            else:
                result = result + "This is an isosceles triangle"
        if a!=b!=c:
            result = result + "This is a scalene triangle"
    return result


print(classify_triangle(a,b,c))
