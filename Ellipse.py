import drawing_a_grid as dg
import tkinter


class Ellipse:
    def __init__(self, raio_horizontal, raio_vertical, x_central, y_central):
        self.raio_horizontal_quadrado = raio_horizontal ** 2
        self.raio_vertical_quadrado = raio_vertical ** 2

        self.x = 0
        self.y = raio_vertical

        # Derivadas parciais de x e y
        self.dx = 2 * self.raio_vertical_quadrado * self.x
        self.dy = 2 * self.raio_horizontal_quadrado * self.y

        self.erro = raio_vertical * self.raio_horizontal_quadrado + self.raio_horizontal_quadrado * 0.25

    def desenha_quatro(self):
        dg.DesenharPixel(self.x, self.y, '#f00')
        dg.DesenharPixel(-self.x, self.y, '#f00')
        dg.DesenharPixel(self.x, -self.y, '#f00')
        dg.DesenharPixel(-self.x, -self.y, '#f00')

    def ellipse(self):
        # Região 1
        while self.dx < self.dy:
            self.desenha_quatro()
            self.x += 1
            self.erro += self.dx + self.raio_vertical_quadrado
            self.dx += 2 * self.raio_vertical_quadrado

            if self.erro > 0:
                self.y -= 1
                self.erro += self.raio_horizontal_quadrado - self.dy
                self.dy -= 2 * self.raio_horizontal_quadrado

        self.erro = self.raio_vertical_quadrado * ((
                                                               self.x + 0.5) ** 2) + self.raio_horizontal_quadrado * self.y * self.y - self.raio_horizontal_quadrado * self.raio_vertical_quadrado

        # Região 2
        while self.y >= 0:
            self.desenha_quatro()
            self.y -= 1
            self.erro += self.raio_horizontal_quadrado - self.dy
            self.dy -= 2 * self.raio_horizontal_quadrado

            if self.erro < 0:
                self.x += 1
                self.erro += self.dx + self.raio_vertical_quadrado
                self.dx += 2 * self.raio_vertical_quadrado

def main():
    raio_horizontal = int(input("Defina o valor do raio horizontal:"))
    raio_vertical = int(input("Defina o valor do raio vertical:"))
    entrada_central = str(input("Defina as coordenadas do centro do círculo:")).split()
    x_central, y_central = int(entrada_central[0]), int(entrada_central[1])
    print(x_central, y_central)
    ellipse = Ellipse(raio_horizontal, raio_vertical, x_central, y_central)
    ellipse.ellipse()
    dg.CriarTemplate()
    tkinter.mainloop()

    return 0

if __name__ == "__main__":
    main()