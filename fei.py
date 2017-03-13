import numpy
import pylab


## --------------------------------------------------
max_dots = 100


## --------------------------------------------------
##
##
def plot_f(s, e, f, a=1, c=0, d=0, v=False,clr="k"):
    x = numpy.linspace(s, e, max_dots)
    y = f(x - c)

    if not v:
        pylab.plot(x, a * y + d, clr)
    else:
        pylab.plot(a * y + d, x, clr)


## --------------------------------------------------
## POINTS


##
##
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


## --------------------------------------------------
## PIECES

##
##
class Display:
    def __init__(self, s, e, a=1, c=0, d=0, v=False, clr="k"):
        self.s = s
        self.e = e
        self.a = a
        self.c = c
        self.d = d
        self.v = v
        self.clr = clr


##
##
class Piece:
    def __init__(self, f, lod=[]):
        self.f = f
        self.lod = lod

    def display(self):
        for dis in self.lod:
            plot_f(dis.s, dis.e,
                   self.f,
                   dis.a,
                   dis.c, dis.d,
                   dis.v, dis.clr)

    def add_display(self,dis):
        self.lod.append(dis)


##
##            
def line_slope(lod, m=0, b=0):
    def f(x):
        return m * x + b
    return Piece(f,lod)


##
##
def line_points(p1, p2):
    if (p1.x - p2.x) == 0:
        m = 0
        b = p1.x
        v = True
        s = p1.y
        e = p2.y
    else:
        m = (p1.y - p2.y) / (p1.x - p2.x)
        b = - m * p1.x + p1.y
        v = False
        s = p1.x
        e = p2.x
        
    def f(x):
        return m * x + b
    
    return Piece(f,[Display(s=s, e=e, v=v)])


##
##
def parabola(lod, a=0, b=0, c=0):
    def f(x):
        return a * (x ** 2) + b * x + c
    return Piece(f, lod)


## --------------------------------------------------
## SHAPES
class Shape:
    def __init__(self, lop=[]):
        self.lop = lop

    def add_pieces(self, lop):
        for p in lop:
            self.lop.append(p)

    def add_piece(self,p):
        self.lop.append(p)

    def display(self):
        for piece in self.lop:
            piece.display()


##
##
def ellipse_list(a, b=None,lod=None):
    if not b:
        b = a

    if not lod:
        lod = [Display(s=-a,e=a)]

    for dis in lod:
        if dis.s <= -a:
            dis.s = -a
        if dis.e >= a:
            dis.e = a
        
    def f(x):
        return ((1 - ((x / a) ** 2)) * (b ** 2)) ** (1 / 2)

    new_lod = []
    for dis in lod:
        new_lod.append(Display(s = dis.s, e = dis.e,
                               a = -dis.a,
                               c = dis.c, d = dis.d,
                               v = dis.v,
                               clr = dis.clr))
    
    lop = [Piece(f,lod),
           Piece(f,new_lod)]
    
    return lop


##
##
def rectangle_list(tl, br):
    lop = [line_points(tl, Point(tl.x, br.y)),
           line_points(tl, Point(br.x, tl.y)),
           line_points(br, Point(tl.x, br.y)),
           line_points(br, Point(br.x, tl.y))]
    return lop


##
##
def triangle_list(p1, p2, p3):
    lop = [line_points(p1, p2),
           line_points(p2, p3),
           line_points(p1, p3)]
    return lop
