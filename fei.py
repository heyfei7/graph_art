import numpy
import pylab


## --------------------------------------------------
max_dots = 100


##
##
def plot_f(s, e, f, a=None, c=None, d=None, v=None):
    if not c:
        c = 0
    if not d:
        d = 0
    if not a:
        a = 1
    x = numpy.linspace(s, e, max_dots)
    y = f(x - c)

    if not v:
        pylab.plot(x, a * y + d, "k")
    else:
        pylab.plot(a * y + d, x, "k")


## --------------------------------------------------
##
##
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

##
##
class Piece:
    def __init__(self, o, s=None, e=None, a=None, c=None, d=None, v=None):
        self.o = o
        if not not self.o.s:
            self.s = self.o.s
        else:
            self.s = s

        if not not self.o.e:
            self.e = self.o.e
        else:
            self.e = e

        if not a:
            self.a = 1
        else:
            self.a = a
        if not c:
            self.c = 0
        else:
            self.c = c
        if not d:
            self.d = 0
        else:
            self.d = d
        if not self.o.v:
            self.v = v
        else:
            self.v = self.o.v

    def display(self):
        plot_f(self.s, self.e, self.o.f, self.a, self.c, self.d, self.v)


## --------------------------------------------------
## DIFFERENT SHAPE PIECES
## --------------------------------------------------
##
##
class Line:
    def __init__(self, m=None, b=None, p1=None, p2=None):
        self.v = None
        self.s = None
        self.e = None
        if (not not p1) and (not not p2):
            self.p = True
            if (p1.x - p2.x) == 0:
                m = 0
                b = p1.x
                self.v = True
                self.s = p1.y
                self.e = p2.y
            else:
                m = (p1.y - p2.y) / (p1.x - p2.x)
                b = - m * p1.x + p1.y
                self.s = p1.x
                self.e = p2.x
        else:
            if not m:
                m = 0
            if not b:
                b = 0

        def f(x):
            return m * x + b
        
        self.m = m
        self.b = b
        self.f = f 


##
##
class Parabola:
    def __init__(self, a=None, b=None, c=None):
        if not a:
            a = 0
        if not b:
            b = 0
        if not c:
            c = 0
        def f(x):
            return a * (x ** 2) + b * x + c
        self.f = f
        self.s = None
        self.e = None
        self.v = None


##
##
class PieceFun:
    def __init__(self, f):
        self.f = f
        self.s = None
        self.e = None
        self.v = None

## --------------------------------------------------
##
##
class Shape:
    def __init__(self, lop=None):
        if not lop:
            self.lop = []
        else:
            self.lop = lop

    def add_piece(self, piece):
        self.lop.append(piece)

    def display(self):
        for piece in self.lop:
            piece.display()


##
##
class Rectangle:
    def __init__(self, tl, br):
        self.shape = Shape()
        self.shape.add_piece(Piece(Line(p1=tl, p2=Point(tl.x,br.y))))
        self.shape.add_piece(Piece(Line(p1=tl, p2=Point(br.x,tl.y))))
        self.shape.add_piece(Piece(Line(p1=br, p2=Point(tl.x,br.y))))
        self.shape.add_piece(Piece(Line(p1=br, p2=Point(br.x,tl.y))))

    def transform(self,a=None, c=None, d=None, v=None):
        pass
        ##self.shape.display(a=a,c=c,d=d,v=v)

    def display(self):
        self.shape.display()
##
##
class Triangle:
    def __init__(self, p1, p2, p3):
        self.shape = Shape()
        self.shape.add_piece(Piece(Line(p1=p1, p2=p2)))
        self.shape.add_piece(Piece(Line(p1=p1, p2=p3)))
        self.shape.add_piece(Piece(Line(p1=p2, p2=p3)))

    def transform(self,a=None, c=None, d=None, v=None):
        pass
        ##self.shape.display(a=a,c=c,d=d,v=v)

    def display(self):
        self.shape.display()
        

##
##
class Ellipse:
    def __init__(self, x_f, y_f=None, s=None, e=None):
        if not y_f:
            y_f = x_f

        if not s:
            s = x_f
        if not e:
            e = -s
            
        def f(x):
            return ((1 - ((x / x_f) ** 2)) * (y_f ** 2)) ** (1 / 2)

        self.piece1 = Piece(PieceFun(f), s, e)
        self.piece2 = Piece(PieceFun(f), s, e)
        

    def display(self,a=None, c=None, d=None, v=None):
        self.piece1.s += c
        self.piece1.e += c
        self.piece2.s += c
        self.piece2.e += c
        print(self.piece1.s,self.piece1.e,self.piece2.s,self.piece2.e)
        if not a:
            a = 1
        self.piece1.display(a=a,c=c,d=d,v=v)
        self.piece2.display(a=-a,c=c,d=d,v=v)
