#!/usr/bin/env python

# Space Invaders
# Created by Lee Robinson

from pygame import *
import sys
from os.path import abspath, dirname
from random import choice

BASE_PATH = abspath(dirname(__file__))
FONT_PATH = BASE_PATH + '/fonts/'
IMAGE_PATH = BASE_PATH + '/images/'
SOUND_PATH = BASE_PATH + '/sounds/'

# Colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

SCREEN = display.set_mode((800, 600))
FONT = FONT_PATH + 'space_invaders.ttf'
IMG_NAMES = ['ship', 'mystery',
             'enemy1_1', 'enemy1_2',
             'enemy2_1', 'enemy2_2',
             'enemy3_1', 'enemy3_2',
             'explosionblue', 'explosiongreen', 'explosionpurple',
             'laser', 'enemylaser']
IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES}

BLOCKERS_POSITION = 450
ENEMY_DEFAULT_POSITION = 65  # Initial value for a new game
ENEMY_MOVE_DOWN = 35


class Ship(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(375, 540))
        self.speed = 5

    def update(self, keys, *args):
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 740:
            self.rect.x += self.speed
        game.screen.blit(self.image, self.rect)


class Bullet(sprite.Sprite):
    def __init__(self, xpos, ypos, direction, speed, filename, side):
        sprite.Sprite.__init__(self)
        self.image = IMAGES[filename]
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.speed = speed
        self.direction = direction
        self.side = side
        self.filename = filename

    def update(self, keys, *args):
        game.screen.blit(self.image, self.rect)
        self.rect.y += self.speed * self.direction
        if self.rect.y < 15 or self.rect.y > 600:
            self.kill()

#Esta clase es para un enemigo en el videojuego.
#Es una subclase para sprite.Sprite.
#Se usa para hacer la animación del enemigo en el juego.
class Enemy(sprite.Sprite):
#El constructor __init__ se encarga de inicializar la instancia de la clase Enemy.
#Toma dos argumentos: row y column, que indican la posición del enemigo en alguna estructura de filas y columnas.
    def __init__(self, row, column):
#Llama al constructor de la superclase sprite.Sprite para inicializar la instancia.
#Asigna los valores row y column a los atributos de la instancia.
        sprite.Sprite.__init__(self)
#Asigna los valores row y column a los atributos de la instancia. 
        self.row = row
        self.column = column
#Crea una lista vacía self.images. 
        self.images = []
#Llama al método load_images() para cargar las imágenes del enemigo.
        self.load_images()
#Inicializa un índice self.index en 0, que se utilizará para controlar la animación. 
        self.index = 0
#Inicializa el atributo self.image con la primera imagen en self.images
        self.image = self.images[self.index]
#Crea un rectángulo self.rect basado en la imagen actual.
        self.rect = self.image.get_rect()
#Este método se encarga de cambiar la imagen del enemigo para lograr una animación. 
    def toggle_image(self):
#Incrementa el índice self.index y, si el índice supera la cantidad de imágenes en self.images, lo reinicia a 0. 
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
#Luego, actualiza el atributo self.image con la nueva imagen basada en el índice.
        self.image = self.images[self.index]
#Este método es parte de la estructura de sprites y se llama en cada fotograma del juego.
#Su función es dibujar la imagen actual del enemigo en la pantalla del juego utilizando game.screen.blit. Esto permite que el sprite del enemigo se muestre en la posición correcta en la pantalla.
    def update(self, *args):
        game.screen.blit(self.image, self.rect)
#Este método carga las imágenes del enemigo en la lista self.images según la fila row del enemigo.
    def load_images(self):
        images = {0: ['1_2', '1_1'],
                  1: ['2_2', '2_1'],
                  2: ['2_2', '2_1'],
                  3: ['3_1', '3_2'],
                  4: ['3_1', '3_2'],
                  }
#Las imágenes se almacenan en un diccionario llamado IMAGES y se escalan a un tamaño de 40x35 píxeles antes de agregarlas a la lista self.images.
        img1, img2 = (IMAGES['enemy{}'.format(img_num)] for img_num in
                      images[self.row])
        self.images.append(transform.scale(img1, (40, 35)))
        self.images.append(transform.scale(img2, (40, 35)))


class EnemiesGroup(sprite.Group):
    def __init__(self, columns, rows):
        sprite.Group.__init__(self)
        self.enemies = [[None] * columns for _ in range(rows)]
        self.columns = columns
        self.rows = rows
        self.leftAddMove = 0
        self.rightAddMove = 0
        self.moveTime = 600
        self.direction = 1
        self.rightMoves = 30
        self.leftMoves = 30
        self.moveNumber = 15
        self.timer = time.get_ticks()
        self.bottom = game.enemyPosition + ((rows - 1) * 45) + 35
        self._aliveColumns = list(range(columns))
        self._leftAliveColumn = 0
        self._rightAliveColumn = columns - 1

    def update(self, current_time):
        if current_time - self.timer > self.moveTime:
            if self.direction == 1:
                max_move = self.rightMoves + self.rightAddMove
            else:
                max_move = self.leftMoves + self.leftAddMove

            if self.moveNumber >= max_move:
                self.leftMoves = 30 + self.rightAddMove
                self.rightMoves = 30 + self.leftAddMove
                self.direction *= -1
                self.moveNumber = 0
                self.bottom = 0
                for enemy in self:
                    enemy.rect.y += ENEMY_MOVE_DOWN
                    enemy.toggle_image()
                    if self.bottom < enemy.rect.y + 35:
                        self.bottom = enemy.rect.y + 35
            else:
                velocity = 10 if self.direction == 1 else -10
                for enemy in self:
                    enemy.rect.x += velocity
                    enemy.toggle_image()
                self.moveNumber += 1

            self.timer += self.moveTime

    def add_internal(self, *sprites):
        super(EnemiesGroup, self).add_internal(*sprites)
        for s in sprites:
            self.enemies[s.row][s.column] = s

    def remove_internal(self, *sprites):
        super(EnemiesGroup, self).remove_internal(*sprites)
        for s in sprites:
            self.kill(s)
        self.update_speed()

    def is_column_dead(self, column):
        return not any(self.enemies[row][column]
                       for row in range(self.rows))

    def random_bottom(self):
        col = choice(self._aliveColumns)
        col_enemies = (self.enemies[row - 1][col]
                       for row in range(self.rows, 0, -1))
        return next((en for en in col_enemies if en is not None), None)

    def update_speed(self):
        if len(self) == 1:
            self.moveTime = 200
        elif len(self) <= 10:
            self.moveTime = 400

    def kill(self, enemy):
        self.enemies[enemy.row][enemy.column] = None
        is_column_dead = self.is_column_dead(enemy.column)
        if is_column_dead:
            self._aliveColumns.remove(enemy.column)

        if enemy.column == self._rightAliveColumn:
            while self._rightAliveColumn > 0 and is_column_dead:
                self._rightAliveColumn -= 1
                self.rightAddMove += 5
                is_column_dead = self.is_column_dead(self._rightAliveColumn)

        elif enemy.column == self._leftAliveColumn:
            while self._leftAliveColumn < self.columns and is_column_dead:
                self._leftAliveColumn += 1
                self.leftAddMove += 5
                is_column_dead = self.is_column_dead(self._leftAliveColumn)

#Es una subclase de la clase sprite.Sprite.
#Esta clase sirve para diseñar los bloques del videojuego.
class Blocker(sprite.Sprite):
#Se llama cuando se crea una instancia de Blocker. 
#Toma cuatro parámetros:
#size: El tamaño (ancho y alto) del bloque.
#color: El color del bloque.
#row: La fila en la que se ubicará el bloque.
#column: La columna en la que se ubicará el bloque.
    def __init__(self, size, color, row, column):
        sprite.Sprite.__init__(self)
#self.height y self.width son el alto y ancho del bloque, respectivamente.
        self.height = size
        self.width = size
#self.color es el color del bloque.
        self.color = color
#self.image es una superficie (Surface) del mismo tamaño que el bloque y se llena con el color especificado.
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
#self.rect es un rectángulo que abarca la superficie del bloque.
        self.rect = self.image.get_rect()
#self.row y self.column almacenan la fila y columna en la que se encuentra el bloque.
        self.row = row
        self.column = column
#Se utiliza para dibujar el bloque en la pantalla. 
#Utiliza el atributo self.image (la superficie del bloque) y lo coloca en la posición definida por self.rect en la pantalla del juego (game.screen). 
    def update(self, keys, *args):
        game.screen.blit(self.image, self.rect)

#Es una subclase de la clase sprite.Sprite.
class Mystery(sprite.Sprite):
#El constructor de la clase se llama cuando se crea una instancia de la clase "Mystery".
    def __init__(self):
#Se llama al constructor de la clase base "Sprite" utilizando sprite.Sprite.__init__(self) para inicializar la funcionalidad básica de un sprite.
        sprite.Sprite.__init__(self)
#Se carga una imagen desde un diccionario llamado "IMAGES" y se almacena en la propiedad "self.image".
#La imagen se redimensiona a 75x35 píxeles.
#Se crea un rectángulo asociado a la imagen y se coloca en la posición (-80, 45).
        self.image = IMAGES['mystery']
        self.image = transform.scale(self.image, (75, 35))
        self.rect = self.image.get_rect(topleft=(-80, 45))
#Se inicializan varias propiedades como "self.row", "self.moveTime", "self.direction", "self.timer", y "self.playSound".
        self.row = 5
        self.moveTime = 25000
        self.direction = 1
        self.timer = time.get_ticks()
#Se carga un archivo de sonido y se asocia con "self.mysteryEntered". Luego, se establece su volumen en 0.3 (30%).
        self.mysteryEntered = mixer.Sound(SOUND_PATH + 'mysteryentered.wav')
        self.mysteryEntered.set_volume(0.3)
        self.playSound = True
#Este método se llama en cada ciclo del juego para actualizar el objeto "Mystery". 
    def update(self, keys, currentTime, *args):
        resetTimer = False
#Calcula el tiempo transcurrido desde la última actualización en la variable "passed".
        passed = currentTime - self.timer
#Si ha pasado más tiempo que el valor de "self.moveTime":
#Si el objeto está fuera de la pantalla (a la izquierda o a la derecha) y "self.playSound" es verdadero, reproduce un sonido ("self.mysteryEntered") y establece "self.playSound" en falso para evitar que se reproduzca varias veces.
#Mueve el objeto hacia la derecha si "self.direction" es 1 o hacia la izquierda si "self.direction" es -1. Durante el movimiento, también realiza un fadeout del sonido "self.mysteryEntered" durante 4 segundos.
#Dibuja la imagen en la pantalla del juego en la nueva posición del objeto.
#Si el objeto se encuentra a la derecha de la pantalla (más allá de x=830), reinicia el sonido y cambia la dirección a -1.
#Si el objeto se encuentra a la izquierda de la pantalla (más allá de x=-90), reinicia el sonido y cambia la dirección a 1.
#Si se cumplen las condiciones anteriores y "resetTimer" es verdadero, actualiza el temporizador "self.timer" con el tiempo actual. Esto asegura que el objeto vuelva a moverse después de un reinicio.
        if passed > self.moveTime:
            if (self.rect.x < 0 or self.rect.x > 800) and self.playSound:
                self.mysteryEntered.play()
                self.playSound = False
            if self.rect.x < 840 and self.direction == 1:
                self.mysteryEntered.fadeout(4000)
                self.rect.x += 2
                game.screen.blit(self.image, self.rect)
            if self.rect.x > -100 and self.direction == -1:
                self.mysteryEntered.fadeout(4000)
                self.rect.x -= 2
                game.screen.blit(self.image, self.rect)

        if self.rect.x > 830:
            self.playSound = True
            self.direction = -1
            resetTimer = True
        if self.rect.x < -90:
            self.playSound = True
            self.direction = 1
            resetTimer = True
        if passed > self.moveTime and resetTimer:
            self.timer = currentTime

#Es una subclase de la clase sprite.Sprite.
#Esta subclase esta echa para hacer la explocion de los enemigos.
class EnemyExplosion(sprite.Sprite):
#El constructor de la clase se llama cuando se crea una instancia de "EnemyExplosion". Recibe dos parámetros: 
#"enemy" (el enemigo que explotó) 
#"*groups" (una tupla de grupos de sprites a los que se va a agregar este sprite).
    def __init__(self, enemy, *groups):
#Inicia la funcionalidad básica de un sprite y agregarlo a los grupos especificados.
        super(EnemyExplosion, self).__init__(*groups)
#Se obtiene una imagen de explosión llamando al método estático "get_image(enemy.row)" y se escala a un tamaño de 40x35 píxeles, lo que representa la primera etapa de la explosión.
#Se obtiene una segunda imagen de explosión del mismo tipo, pero se escala a un tamaño de 50x45 píxeles, que representa la segunda etapa de la explosión.
        self.image = transform.scale(self.get_image(enemy.row), (40, 35))
        self.image2 = transform.scale(self.get_image(enemy.row), (50, 45))
#Se crea un rectángulo asociado a la imagen y se coloca en la misma posición que el enemigo ("enemy") que explotó.
        self.rect = self.image.get_rect(topleft=(enemy.rect.x, enemy.rect.y))
#Se registra el tiempo actual en "self.timer" utilizando time.get_ticks().
        self.timer = time.get_ticks()

    @staticmethod
#Este método estático se utiliza para obtener la imagen de explosión correspondiente a la fila del enemigo que explotó.
#El parámetro "row" se utiliza para determinar el tipo de imagen de explosión que se necesita. 
    def get_image(row):
#Se crea una lista llamada "img_colors" que contiene nombres de colores.
        img_colors = ['purple', 'blue', 'blue', 'green', 'green']
#La función busca la imagen de explosión en el diccionario "IMAGES" utilizando el color correspondiente al valor de "row".
#La imagen seleccionada se devuelve como resultado.
        return IMAGES['explosion{}'.format(img_colors[row])]
#Este método se llama en cada ciclo del juego para actualizar el objeto "EnemyExplosion". 
    def update(self, current_time, *args):
#Calcula el tiempo transcurrido desde la creación del objeto, usando la diferencia entre el tiempo actual ("current_time") y el tiempo registrado en "self.timer".
        passed = current_time - self.timer
#Luego, dependiendo del valor de "passed" (el tiempo transcurrido), se controla la aparición de las imágenes de explosión:
#Si "passed" está en el rango de 0 a 100, se muestra la primera imagen de explosión en la posición del enemigo.
#Si "passed" está en el rango de 100 a 200, se muestra la segunda imagen de explosión ligeramente desplazada.
#Si "passed" supera los 400 milisegundos, el objeto "EnemyExplosion" se elimina del juego llamando a self.kill().
        if passed <= 100:
            game.screen.blit(self.image, self.rect)
        elif passed <= 200:
            game.screen.blit(self.image2, (self.rect.x - 6, self.rect.y - 6))
        elif 400 < passed:
            self.kill()

#Es una subclase de la clase sprite.Sprite.
#Esta subclase esta echa para hacer una explocion de un misterio en el juego y adquirir la puntuacion de la misma
class MysteryExplosion(sprite.Sprite):
#El constructor de la clase se llama cuando se crea una instancia de "MysteryExplosion". 
#Recibe tres parámetros: 
#"mystery" (un objeto Mystery que ha explotado),
#"score" (la puntuación obtenida por la explosión), 
#"*groups" (una tupla de grupos de sprites a los que se va a agregar este sprite).
    def __init__(self, mystery, score, *groups):
#Inicia la funcion básica de un sprite y lo agrega a los grupos especificados.
        super(MysteryExplosion, self).__init__(*groups)
#Se crea un objeto de texto ("self.text") utilizando una clase llamada "Text". Este objeto de texto se utiliza para mostrar la puntuación en la pantalla. 
#El texto se crea con un tipo de fuente ("FONT"), un tamaño de fuente de 20, el valor de "score" convertido a una cadena, el color blanco ("WHITE"), y se coloca en una posición ligeramente desplazada desde la posición del objeto "mystery".
        self.text = Text(FONT, 20, str(score), WHITE,
                         mystery.rect.x + 20, mystery.rect.y + 6)
#Se registra el tiempo actual en "self.timer" utilizando time.get_ticks().
        self.timer = time.get_ticks()
#Este método se llama en cada ciclo del juego para actualizar el objeto "MysteryExplosion". 
    def update(self, current_time, *args):
#Calcula el tiempo transcurrido desde la creación del objeto, usando la diferencia entre el tiempo actual ("current_time") y el tiempo registrado en "self.timer", que se almacenó en el constructor.
        passed = current_time - self.timer
#Dependiendo del valor de "passed" (el tiempo transcurrido), se controla la aparición y desaparición del texto de puntuación:
#Si "passed" está en el rango de 0 a 200 o en el rango de 400 a 600, se llama al método "draw" del objeto de texto ("self.text") para mostrar el texto en la pantalla del juego.
#Si "passed" supera los 600 milisegundos, el objeto "MysteryExplosion" se elimina del juego llamando a self.kill().

        if passed <= 200 or 400 < passed <= 600:
            self.text.draw(game.screen)
        elif 600 < passed:
            self.kill()


class ShipExplosion(sprite.Sprite):
    def __init__(self, ship, *groups):
        super(ShipExplosion, self).__init__(*groups)
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(ship.rect.x, ship.rect.y))
        self.timer = time.get_ticks()

    def update(self, current_time, *args):
        passed = current_time - self.timer
        if 300 < passed <= 600:
            game.screen.blit(self.image, self.rect)
        elif 900 < passed:
            self.kill()


class Life(sprite.Sprite):
    def __init__(self, xpos, ypos):
        sprite.Sprite.__init__(self)
        self.image = IMAGES['ship']
        self.image = transform.scale(self.image, (23, 23))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, *args):
        game.screen.blit(self.image, self.rect)


class Text(object):
    def __init__(self, textFont, size, message, color, xpos, ypos):
        self.font = font.Font(textFont, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))

    def draw(self, surface):
        surface.blit(self.surface, self.rect)


class SpaceInvaders(object):
    def __init__(self):
        # It seems, in Linux buffersize=512 is not enough, use 4096 to prevent:
        #   ALSA lib pcm.c:7963:(snd_pcm_recover) underrun occurred
        mixer.pre_init(44100, -16, 1, 4096)
        init()
        self.clock = time.Clock()
        self.caption = display.set_caption('Space Invaders')
        self.screen = SCREEN
        self.background = image.load(IMAGE_PATH + 'background.jpg').convert()
        self.startGame = False
        self.mainScreen = True
        self.gameOver = False
        # Counter for enemy starting position (increased each new round)
        self.enemyPosition = ENEMY_DEFAULT_POSITION
        self.titleText = Text(FONT, 50, 'Space Invaders', WHITE, 164, 155)
        self.titleText2 = Text(FONT, 25, 'Press any key to continue', WHITE,
                               201, 225)
        self.gameOverText = Text(FONT, 50, 'Game Over', WHITE, 250, 270)
        self.nextRoundText = Text(FONT, 50, 'Next Round', WHITE, 240, 270)
        self.enemy1Text = Text(FONT, 25, '   =   10 pts', GREEN, 368, 270)
        self.enemy2Text = Text(FONT, 25, '   =  20 pts', BLUE, 368, 320)
        self.enemy3Text = Text(FONT, 25, '   =  30 pts', PURPLE, 368, 370)
        self.enemy4Text = Text(FONT, 25, '   =  ?????', RED, 368, 420)
        self.scoreText = Text(FONT, 20, 'Score', WHITE, 5, 5)
        self.livesText = Text(FONT, 20, 'Lives ', WHITE, 640, 5)

        self.life1 = Life(715, 3)
        self.life2 = Life(742, 3)
        self.life3 = Life(769, 3)
        self.livesGroup = sprite.Group(self.life1, self.life2, self.life3)

    def reset(self, score):
        self.player = Ship()
        self.playerGroup = sprite.Group(self.player)
        self.explosionsGroup = sprite.Group()
        self.bullets = sprite.Group()
        self.mysteryShip = Mystery()
        self.mysteryGroup = sprite.Group(self.mysteryShip)
        self.enemyBullets = sprite.Group()
        self.make_enemies()
        self.allSprites = sprite.Group(self.player, self.enemies,
                                       self.livesGroup, self.mysteryShip)
        self.keys = key.get_pressed()

        self.timer = time.get_ticks()
        self.noteTimer = time.get_ticks()
        self.shipTimer = time.get_ticks()
        self.score = score
        self.create_audio()
        self.makeNewShip = False
        self.shipAlive = True

    def make_blockers(self, number):
        blockerGroup = sprite.Group()
        for row in range(4):
            for column in range(9):
                blocker = Blocker(10, GREEN, row, column)
                blocker.rect.x = 50 + (200 * number) + (column * blocker.width)
                blocker.rect.y = BLOCKERS_POSITION + (row * blocker.height)
                blockerGroup.add(blocker)
        return blockerGroup

    def create_audio(self):
        self.sounds = {}
        for sound_name in ['shoot', 'shoot2', 'invaderkilled', 'mysterykilled',
                           'shipexplosion']:
            self.sounds[sound_name] = mixer.Sound(
                SOUND_PATH + '{}.wav'.format(sound_name))
            self.sounds[sound_name].set_volume(0.2)

        self.musicNotes = [mixer.Sound(SOUND_PATH + '{}.wav'.format(i)) for i
                           in range(4)]
        for sound in self.musicNotes:
            sound.set_volume(0.5)

        self.noteIndex = 0

    def play_main_music(self, currentTime):
        if currentTime - self.noteTimer > self.enemies.moveTime:
            self.note = self.musicNotes[self.noteIndex]
            if self.noteIndex < 3:
                self.noteIndex += 1
            else:
                self.noteIndex = 0

            self.note.play()
            self.noteTimer += self.enemies.moveTime

    @staticmethod
    def should_exit(evt):
        # type: (pygame.event.EventType) -> bool
        return evt.type == QUIT or (evt.type == KEYUP and evt.key == K_ESCAPE)

    def check_input(self):
        self.keys = key.get_pressed()
        for e in event.get():
            if self.should_exit(e):
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if len(self.bullets) == 0 and self.shipAlive:
                        if self.score < 1000:
                            bullet = Bullet(self.player.rect.x + 23,
                                            self.player.rect.y + 5, -1,
                                            15, 'laser', 'center')
                            self.bullets.add(bullet)
                            self.allSprites.add(self.bullets)
                            self.sounds['shoot'].play()
                        else:
                            leftbullet = Bullet(self.player.rect.x + 8,
                                                self.player.rect.y + 5, -1,
                                                15, 'laser', 'left')
                            rightbullet = Bullet(self.player.rect.x + 38,
                                                 self.player.rect.y + 5, -1,
                                                 15, 'laser', 'right')
                            self.bullets.add(leftbullet)
                            self.bullets.add(rightbullet)
                            self.allSprites.add(self.bullets)
                            self.sounds['shoot2'].play()

    def make_enemies(self):
        enemies = EnemiesGroup(10, 5)
        for row in range(5):
            for column in range(10):
                enemy = Enemy(row, column)
                enemy.rect.x = 157 + (column * 50)
                enemy.rect.y = self.enemyPosition + (row * 45)
                enemies.add(enemy)

        self.enemies = enemies

    def make_enemies_shoot(self):
        if (time.get_ticks() - self.timer) > 700 and self.enemies:
            enemy = self.enemies.random_bottom()
            self.enemyBullets.add(
                Bullet(enemy.rect.x + 14, enemy.rect.y + 20, 1, 5,
                       'enemylaser', 'center'))
            self.allSprites.add(self.enemyBullets)
            self.timer = time.get_ticks()

    def calculate_score(self, row):
        scores = {0: 30,
                  1: 20,
                  2: 20,
                  3: 10,
                  4: 10,
                  5: choice([50, 100, 150, 300])
                  }

        score = scores[row]
        self.score += score
        return score

    def create_main_menu(self):
        self.enemy1 = IMAGES['enemy3_1']
        self.enemy1 = transform.scale(self.enemy1, (40, 40))
        self.enemy2 = IMAGES['enemy2_2']
        self.enemy2 = transform.scale(self.enemy2, (40, 40))
        self.enemy3 = IMAGES['enemy1_2']
        self.enemy3 = transform.scale(self.enemy3, (40, 40))
        self.enemy4 = IMAGES['mystery']
        self.enemy4 = transform.scale(self.enemy4, (80, 40))
        self.screen.blit(self.enemy1, (318, 270))
        self.screen.blit(self.enemy2, (318, 320))
        self.screen.blit(self.enemy3, (318, 370))
        self.screen.blit(self.enemy4, (299, 420))

    def check_collisions(self):
        sprite.groupcollide(self.bullets, self.enemyBullets, True, True)

        for enemy in sprite.groupcollide(self.enemies, self.bullets,
                                         True, True).keys():
            self.sounds['invaderkilled'].play()
            self.calculate_score(enemy.row)
            EnemyExplosion(enemy, self.explosionsGroup)
            self.gameTimer = time.get_ticks()

        for mystery in sprite.groupcollide(self.mysteryGroup, self.bullets,
                                           True, True).keys():
            mystery.mysteryEntered.stop()
            self.sounds['mysterykilled'].play()
            score = self.calculate_score(mystery.row)
            MysteryExplosion(mystery, score, self.explosionsGroup)
            newShip = Mystery()
            self.allSprites.add(newShip)
            self.mysteryGroup.add(newShip)

        for player in sprite.groupcollide(self.playerGroup, self.enemyBullets,
                                          True, True).keys():
            if self.life3.alive():
                self.life3.kill()
            elif self.life2.alive():
                self.life2.kill()
            elif self.life1.alive():
                self.life1.kill()
            else:
                self.gameOver = True
                self.startGame = False
            self.sounds['shipexplosion'].play()
            ShipExplosion(player, self.explosionsGroup)
            self.makeNewShip = True
            self.shipTimer = time.get_ticks()
            self.shipAlive = False

        if self.enemies.bottom >= 540:
            sprite.groupcollide(self.enemies, self.playerGroup, True, True)
            if not self.player.alive() or self.enemies.bottom >= 600:
                self.gameOver = True
                self.startGame = False

        sprite.groupcollide(self.bullets, self.allBlockers, True, True)
        sprite.groupcollide(self.enemyBullets, self.allBlockers, True, True)
        if self.enemies.bottom >= BLOCKERS_POSITION:
            sprite.groupcollide(self.enemies, self.allBlockers, False, True)

    def create_new_ship(self, createShip, currentTime):
        if createShip and (currentTime - self.shipTimer > 900):
            self.player = Ship()
            self.allSprites.add(self.player)
            self.playerGroup.add(self.player)
            self.makeNewShip = False
            self.shipAlive = True

    def create_game_over(self, currentTime):
        self.screen.blit(self.background, (0, 0))
        passed = currentTime - self.timer
        if passed < 750:
            self.gameOverText.draw(self.screen)
        elif 750 < passed < 1500:
            self.screen.blit(self.background, (0, 0))
        elif 1500 < passed < 2250:
            self.gameOverText.draw(self.screen)
        elif 2250 < passed < 2750:
            self.screen.blit(self.background, (0, 0))
        elif passed > 3000:
            self.mainScreen = True

        for e in event.get():
            if self.should_exit(e):
                sys.exit()

    def main(self):
        while True:
            if self.mainScreen:
                self.screen.blit(self.background, (0, 0))
                self.titleText.draw(self.screen)
                self.titleText2.draw(self.screen)
                self.enemy1Text.draw(self.screen)
                self.enemy2Text.draw(self.screen)
                self.enemy3Text.draw(self.screen)
                self.enemy4Text.draw(self.screen)
                self.create_main_menu()
                for e in event.get():
                    if self.should_exit(e):
                        sys.exit()
                    if e.type == KEYUP:
                        # Only create blockers on a new game, not a new round
                        self.allBlockers = sprite.Group(self.make_blockers(0),
                                                        self.make_blockers(1),
                                                        self.make_blockers(2),
                                                        self.make_blockers(3))
                        self.livesGroup.add(self.life1, self.life2, self.life3)
                        self.reset(0)
                        self.startGame = True
                        self.mainScreen = False

            elif self.startGame:
                if not self.enemies and not self.explosionsGroup:
                    currentTime = time.get_ticks()
                    if currentTime - self.gameTimer < 3000:
                        self.screen.blit(self.background, (0, 0))
                        self.scoreText2 = Text(FONT, 20, str(self.score),
                                               GREEN, 85, 5)
                        self.scoreText.draw(self.screen)
                        self.scoreText2.draw(self.screen)
                        self.nextRoundText.draw(self.screen)
                        self.livesText.draw(self.screen)
                        self.livesGroup.update()
                        self.check_input()
                    if currentTime - self.gameTimer > 3000:
                        # Move enemies closer to bottom
                        self.enemyPosition += ENEMY_MOVE_DOWN
                        self.reset(self.score)
                        self.gameTimer += 3000
                else:
                    currentTime = time.get_ticks()
                    self.play_main_music(currentTime)
                    self.screen.blit(self.background, (0, 0))
                    self.allBlockers.update(self.screen)
                    self.scoreText2 = Text(FONT, 20, str(self.score), GREEN,
                                           85, 5)
                    self.scoreText.draw(self.screen)
                    self.scoreText2.draw(self.screen)
                    self.livesText.draw(self.screen)
                    self.check_input()
                    self.enemies.update(currentTime)
                    self.allSprites.update(self.keys, currentTime)
                    self.explosionsGroup.update(currentTime)
                    self.check_collisions()
                    self.create_new_ship(self.makeNewShip, currentTime)
                    self.make_enemies_shoot()

            elif self.gameOver:
                currentTime = time.get_ticks()
                # Reset enemy starting position
                self.enemyPosition = ENEMY_DEFAULT_POSITION
                self.create_game_over(currentTime)

            display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
