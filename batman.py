import numpy
import pylab
import fei
from fei import Shape
from fei import Point
from fei import Piece
from fei import Display

c_1 = 2 * ((3) ** (1/2))
c_2 = 2.75
c_3 = 1.25
x3 = 1.5
y2 = (c_1 - 2) / ((x3 ** 2) * ((x3 ** 2) + 1))
m_1 = (3 - c_1) / (0.75 - 1)
m_2 = (c_1 - 3) / (0.75 - 1)

def f1(x):
    return -1.28 * ((x ** 2) - ((1.25) ** 2))

def f2(x):
    return y2 * (x ** 2) * ((x ** 2) + 1)

batman = Shape()

f1_piece = Piece(f1)
f1_piece.add_display(Display(2, 4, c = c_2, d = -c_1))
f1_piece.add_display(Display(0, 2, c = c_3, d = -c_1))
f1_piece.add_display(Display(-4, -2, c = -c_2, d = -c_1))
f1_piece.add_display(Display(-2, 0, c = -c_3, d = -c_1))
f2_piece = Piece(f2, [Display(1, 4, c = 2.5, d = 2),
                      Display(-4, -1, c = -2.5, d = 2)])

batman.add_piece(f1_piece)
batman.add_pieces(fei.ellipse_list(8,4, [Display(-8, -4),
                                         Display(4, 8)]))
batman.add_pieces(fei.ellipse_list(8.5, 4.5))
batman.add_piece(fei.line_slope([Display(-0.75, 0.75)],
                                b = 3))
batman.add_piece(fei.line_slope([Display(0.75, 1)], m = m_1,
                                b = m_1 * (-0.75) + 3))
batman.add_piece(fei.line_slope([Display(-1, -0.75)], m = m_2,
                                b = m_2 * (0.75) + 3))
batman.add_piece(f2_piece)

batman.display()
pylab.show() # show the plot
