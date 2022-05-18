import drawing_a_grid as dg
import tkinter


class Bresenham:
    def __init__(self, xa: int, ya: int, xb: int, yb: int):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb

        self.m = (self.yb - self.ya) / (self.xb - self.xa)  # linear coefficient of a line

        # attributes for reflect_pixels method
        self.reflect_xy = False
        self.reflect_x = False
        self.reflect_y = False

        if (self.xb - self.xa) < (self.yb - self.ya):
            self.reflect_pixels()
            self.m = (self.yb - self.ya) / (self.xb - self.xa)  # linear coefficient of a line

    def reflect_pixels(self):
        if self.m > 1 or self.m < -1:
            aux = self.xb
            self.xb = self.yb
            self.yb = aux
            if not self.reflect_xy:
                self.reflect_xy = True
            else:
                self.reflect_xy = False

        if self.xa > self.xb:
            self.xa *= -1
            self.xb *= -1
            print(self.xa, self.xb)
            if not self.reflect_x:
                self.reflect_x = True
            else:
                self.reflect_x = False

        if self.ya > self.yb:
            self.ya *= -1
            self.yb *= -1
            print(self.ya, self.yb)
            if not self.reflect_y:
                self.reflect_y = True
            else:
                self.reflect_y = False

    def bresenham(self):
        e = self.m - 0.5  # aux variable / error from the mid point
        x_aux, y_aux = self.xa, self.ya
        while x_aux <= self.xb:
            print(x_aux, y_aux)
            if self.reflect_y:
                dg.DesenharPixel(x_aux, y_aux*(-1), '#f00')
            if self.reflect_x:
                dg.DesenharPixel(x_aux*(-1), y_aux, '#f00')
            if self.reflect_xy:
                dg.DesenharPixel(y_aux, x_aux, '#f00')
            else:
                dg.DesenharPixel(x_aux, y_aux, '#f00')

            x_aux += 1
            if e > 0:
                e -= 1
                y_aux += 1

            e += self.m


def main():
    xy = input("Valores de x1 e y1: ").split()
    x1, y1 = int(xy[0]), int(xy[1])
    xy = input("Valores de x2 e y2: ").split()
    x2, y2 = int(xy[0]), int(xy[1])
    line = Bresenham(x1, y1, x2, y2)
    line.bresenham()
    dg.CriarTemplate()
    tkinter.mainloop()

    return 0


if __name__ == "__main__":
    main()
