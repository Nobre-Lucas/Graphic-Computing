import drawing_a_grid as dg
import tkinter


class Circle:
    def __init__(self, raio, x_central, y_central):
        self.x_central = x_central
        self.y_central = y_central

        self.x = 0
        self.y = raio
        self.erro = -raio

    def desenha_oito(self):
        dg.DesenharPixel(self.x, self.y, '#f00')
        dg.DesenharPixel(-self.x, self.y, '#f00')
        dg.DesenharPixel(self.x, -self.y, '#f00')
        dg.DesenharPixel(-self.x, -self.y, '#f00')
        dg.DesenharPixel(self.y, self.x, '#f00')
        dg.DesenharPixel(-self.y, self.x, '#f00')
        dg.DesenharPixel(self.y, -self.x, '#f00')
        dg.DesenharPixel(-self.y, -self.x, '#f00')

    def circle(self):
        self.desenha_oito()
        while self.x < self.y:
            self.erro += (2 * self.x + 1)
            self.x += 1

            if self.erro >= 0:
                self.erro += 2 - 2 * self.y
                self.y -= 1

            self.desenha_oito()

def main():
    raio = int(input("Defina o valor do raio:"))
    entrada_central = str(input("Defina as coordenadas do centro do círculo:")).split()
    x_central, y_central = int(entrada_central[0]), int(entrada_central[1])
    circle = Circle(raio, x_central, y_central)
    circle.circle()
    dg.CriarTemplate()
    tkinter.mainloop()

    return 0


if __name__ == "__main__":
    main()