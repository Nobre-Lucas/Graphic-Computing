def bresenham(xa=0, ya=0, xb=6, yb=6):
    m = (yb - ya) / (xb - xa) # linear coefficient of a function
    e = m - 0.5 # aux variable
    xaux, yaux = xa, ya
    x_pixels = []
    y_pixels = []

    while (xaux < xb) and (yaux < yb):
        x_pixels.append(xaux)
        y_pixels.append(yaux)
        xaux += 1
        if e > 0:
            e -= 1
            yaux += 1

        e += m

    x_pixels.append(xaux)
    y_pixels.append(yaux)
    return (x_pixels, y_pixels)


def main():

    xy = input("Valores de x1 e y1: ").split()
    x1, y1 = int(xy[0]), int(xy[1])
    xy = input("Valores de x2 e y2: ").split()
    x2, y2 = int(xy[0]), int(xy[1])
    x_pixels, y_pixels = bresenham(x1, y1, x2, y2)
    print(f"{x_pixels}\n{y_pixels}")

    return 0


if __name__ == "__main__":
    main()