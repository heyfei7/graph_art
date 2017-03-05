import numpy
import pylab
import fei

def f1(x):
    return -1.28 * ((x ** 2) - ((1.25) ** 2))

def f2(x):
    return y2 * (x ** 2) * ((x ** 2) + 1)


f_1 = fei.PieceFun(f1)
f_2 = fei.PieceFun(f2)
Piece(f_1,2,4)
Piece(f_2,0,2)
Piece(f_2

c_1 = 2 * ((3) ** (1/2))
c_2 = 2.75
c_3 = 1.25
x3 = 1.5
y2 = (c_1 - 2) / ((x3 ** 2) * ((x3 ** 2) + 1))
m_1 = (3 - c_1) / (0.75 - 1)
m_2 = (c_1 - 3) / (0.75 - 1)

fei.ellipse(8, 4, -8, -4)
fei.ellipse(8, 4, 4, 8)
fei.ellipse(8.5, 4.5, -8.5, 8.5)
fei.plot_f(2, 4, f1, c=c_2, d=-c_1)
fei.plot_f(0, 2, f1, c=c_3, d=-c_1)
fei.plot_f(-4, -2, f1, c=-c_2, d=-c_1)
fei.plot_f(-2, 0, f1, c=-c_3, d=-c_1)
fei.line(-0.75, 0.75, b=3)
fei.line(0.75, 1, m_1, m_1 * (-0.75) + 3)
fei.line(-1, -0.75, m_2, m_2 * (0.75) + 3)
fei.plot_f(1, 4, f2, c=2.5, d=2)
fei.plot_f(-4, -1, f2, c=-2.5, d=2)
    
pylab.show() # show the plot

