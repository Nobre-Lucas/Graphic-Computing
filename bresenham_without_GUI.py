class Line:
    def __init__(self, xa, ya, xb, yb):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.m = (self.yb - self.ya) / (self.xb - self.xa)  # linear coefficient of a line

    def bresenham(self):
        e = self.m - 0.5  # aux variable / error from the mid point
        xaux, yaux = self.xa, self.ya
        x_pixels = []
        y_pixels = []

        while (xaux < self.xb) and (yaux < self.yb):
            x_pixels.append(xaux)
            y_pixels.append(yaux)
            xaux += 1
            if e > 0:
                e -= 1
                yaux += 1

            e += self.m

        x_pixels.append(xaux)
        y_pixels.append(yaux)
        return (x_pixels, y_pixels)


def main():
    xy = input("Valores de x1 e y1: ").split()
    x1, y1 = int(xy[0]), int(xy[1])
    xy = input("Valores de x2 e y2: ").split()
    x2, y2 = int(xy[0]), int(xy[1])
    line = Line(x1, y1, x2, y2)
    x_pixels, y_pixels = line.bresenham()
    print(f"{x_pixels}\n{y_pixels}")

    return 0


if __name__ == "__main__":
    main()
