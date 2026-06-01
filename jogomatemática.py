import pygame
import random
import sys
import math

# Inicializa o pygame
pygame.init()

# Tela cheia
info_tela = pygame.display.Info()
WIDTH, HEIGHT = info_tela.current_w, info_tela.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Mini TuxMath Espacial")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 180, 255)
CYAN = (0, 255, 255)
PURPLE = (180, 0, 255)

# Fontes
font = pygame.font.Font(None, 72)
small_font = pygame.font.Font(None, 48)

# Fundo estrelado
estrelas = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(200)]

def desenhar_fundo():
    screen.fill((5, 5, 20))
    for estrela in estrelas:
        pygame.draw.circle(screen, WHITE, estrela, 1)

# Classe Meteoro
class Meteoro:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -50
        self.vel = random.uniform(0.3, 0.8)
        self.operacao, self.resultado = self.gerar_operacao()
        self.raio = 40
        self.explodindo = False
        self.explosao_frames = 0
        self.particulas = []

    def gerar_operacao(self):
        a = random.randint(-20, 20)
        b = random.randint(-15, 15)
        op = random.choice(["+", "-", "*", "/"])
        if op == "+":
            return f"{a} + {b}", a + b
        elif op == "-":
            return f"{a} - {b}", a - b
        elif op == "*":
            return f"{a} * {b}", a * b
        else:
            b = random.randint(1, 10)
            resultado = a
            a = a * b
            return f"{a} / {b}", resultado

    def mover(self):
        if not self.explodindo:
            self.y += self.vel
            self.x += math.sin(pygame.time.get_ticks() / 200) * 0.4
            # Partículas da cauda
            self.particulas.append([
                self.x + random.randint(-5, 5),
                self.y + random.randint(10, 20),
                random.randint(3, 6),
                random.choice([(255, 150, 0), (255, 100, 0), (255, 200, 50)])
            ])
            if len(self.particulas) > 25:
                self.particulas.pop(0)

    def desenhar(self):
        if self.explodindo:
            cor = YELLOW if self.explosao_frames % 2 == 0 else RED
            pygame.draw.circle(screen, cor, (int(self.x), int(self.y)),
                               self.raio + self.explosao_frames * 2, 3)
            self.explosao_frames += 1
        else:
            # Cauda
            for p in self.particulas:
                pygame.draw.circle(screen, p[3], (int(p[0]), int(p[1])), p[2])

            # Corpo do meteoro cartoon
            pygame.draw.circle(screen, (255, 80, 0), (int(self.x), int(self.y)), self.raio)
            pygame.draw.circle(screen, (255, 180, 0), (int(self.x), int(self.y)), self.raio - 10)
            pygame.draw.circle(screen, (255, 255, 50), (int(self.x), int(self.y)), 10)

            # Operação
            texto = font.render(self.operacao, True, WHITE)
            screen.blit(texto, (self.x - texto.get_width() // 2, self.y - 30))

# Feixe de Laser
class FeixeLaser:
    def __init__(self, origem_x, origem_y, alvo):
        self.origem_x = origem_x
        self.origem_y = origem_y
        self.alvo = alvo
        self.ativo = True
        self.frames = 0
        self.max_frames = 8
        if self.alvo:
            self.alvo.explodindo = True

    def atualizar(self):
        self.frames += 1
        if self.frames > self.max_frames:
            self.ativo = False

    def desenhar(self):
        if self.ativo:
            for i in range(3):
                offset = random.randint(-3, 3)
                pygame.draw.line(screen, CYAN, (self.origem_x + offset, self.origem_y - 10),
                                 (self.alvo.x + offset, self.alvo.y), 3)
            pygame.draw.line(screen, PURPLE, (self.origem_x, self.origem_y - 10),
                             (self.alvo.x, self.alvo.y), 1)

# Disco voador estilizado
class DiscoVoador:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 150
        self.feixes = []
        self.pulsar = 0
        self.sentido = 1

    def desenhar(self):
        brilho = abs(math.sin(pygame.time.get_ticks() / 300)) * 60
        pygame.draw.ellipse(screen, (0, 255, 200, 80),
                            (self.x - 60, self.y + 10, 120, 30))
        pygame.draw.ellipse(screen, (80, 255, 120), (self.x - 50, self.y, 100, 25))
        pygame.draw.ellipse(screen, (30, 120, 70), (self.x - 50, self.y, 100, 25), 3)
        self.pulsar += self.sentido * 0.3
        if self.pulsar > 6 or self.pulsar < 0:
            self.sentido *= -1
        pygame.draw.circle(screen, (0, 200, 255),
                           (int(self.x), int(self.y)), 15 + int(self.pulsar))
        pygame.draw.circle(screen, (255, 255, 255),
                           (int(self.x), int(self.y)), 8, 1)
        pygame.draw.ellipse(screen, (180, 180, 180),
                            (self.x - 45, self.y + 10, 90, 20))
        pygame.draw.ellipse(screen, (100, 100, 100),
                            (self.x - 45, self.y + 10, 90, 20), 2)
        for i in range(6):
            ang = i * (math.pi / 3)
            lx = self.x + math.cos(ang) * 40
            ly = self.y + 12 + math.sin(ang) * 5
            cor = random.choice([(255, 80, 0), (255, 255, 0), (0, 255, 255)])
            pygame.draw.circle(screen, cor, (int(lx), int(ly)), 4)

    def disparar_feixe(self, alvo):
        self.feixes.append(FeixeLaser(self.x, self.y, alvo))

# Inicialização
meteoros = [Meteoro() for _ in range(4)]
input_text = ""
pontos = 0
vidas = 3
clock = pygame.time.Clock()
disco = DiscoVoador()

# Loop principal
rodando = True
while rodando:
    desenhar_fundo()

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.strip() != "":
                    try:
                        if "." in input_text:
                            resposta = float(input_text)
                        else:
                            resposta = int(input_text)
                        acertou = False
                        for m in meteoros:
                            if abs(resposta - m.resultado) < 0.001 and not m.explodindo:
                                disco.disparar_feixe(m)
                                pontos += 10
                                acertou = True
                                break
                        if not acertou:
                            pontos -= 5
                    except:
                        pass
                    input_text = ""
            elif event.unicode.isdigit() or event.unicode in ["-", "."]:
                input_text += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]

    # Atualiza feixes
    for feixe in disco.feixes[:]:
        feixe.atualizar()
        feixe.desenhar()
        if not feixe.ativo:
            disco.feixes.remove(feixe)

    # Atualiza meteoros
    for m in meteoros[:]:
        if m.explodindo:
            if m.explosao_frames > 10:
                meteoros.remove(m)
                meteoros.append(Meteoro())
            else:
                m.desenhar()
        else:
            m.mover()
            m.desenhar()
            if m.y > HEIGHT:
                meteoros.remove(m)
                meteoros.append(Meteoro())
                vidas -= 1
                if vidas == 0:
                    rodando = False

    # Desenha disco e HUD
