import drawing_a_grid as dg
import tkinter


class Line:
    def __init__(self, xa, ya, xb, yb):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.m = (self.yb - self.ya) / (self.xb - self.xa)  # linear coefficient of a line

    def bresenham(self):
        e = self.m - 0.5  # aux variable / error from the mid point
        x_aux, y_aux = self.xa, self.ya

        while (x_aux < self.xb) and (y_aux < self.yb):
            dg.DesenharPixel(x_aux, y_aux, '#f00')

            x_aux += 1
            if e > 0:
                e -= 1
                y_aux += 1

            e += self.m

        dg.DesenharPixel(x_aux, y_aux, '#f00')


def main():
    xy = input("Valores de x1 e y1: ").split()
    x1, y1 = int(xy[0]), int(xy[1])
    xy = input("Valores de x2 e y2: ").split()
    x2, y2 = int(xy[0]), int(xy[1])
    line = Line(x1, y1, x2, y2)
    line.bresenham()
    dg.CriarTemplate()
    tkinter.mainloop()

    return 0


if __name__ == "__main__":
    main()