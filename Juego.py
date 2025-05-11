import os # para limpiar la consola
import time # para pausar el juego
import random # para generar números aleatorios

#------------------#clase padre#--------------------#
class Personaje(): #Clase base para los personajes
    Vida_Base = 200 # Vida base de todos los personajes
    Defensa_Base = 3 # Defensa base de todos los personajes

    def __init__(self, nombre, ataque, especial): # Constructor de la clase
        self.nombre = nombre 
        self.vida = self.Vida_Base
        self.ataque = ataque
        self.especial = especial
        self.defensa = self.Defensa_Base
        self.turnos = 0
        self.puede_usar_especial = True
        self.defensa_temporal = 0

    def recibir_daño(self, daño): # Metodo para recibir daño de vida y de escudo
        Defensa_total = self.defensa + self.defensa_temporal
        daño_real = max(0, daño - Defensa_total)
        self.vida -= daño_real

    def usar_ataque(self): # Metodo para usar ataque normal
        return random.randint(self.ataque - 5, self.ataque + 5)
    
    def usar_ataque_especial(self): # Metodo para usar ataque especial
        if self.puede_usar_especial:
            self.puede_usar_especial = False # Desactiva el ataque especial, no se puede usar hasta el siguiente turno
            return random.randint(self.especial - 10, self.especial + 10)
        return -1 # Retorna -1 si no se puede usar el ataque especial
    
    def usar_defensa(self): # Metodo para usar defensa
        self.defensa_temporal = 5 # Aumenta la defensa temporalmente por ronda
    
    def actualizar_turno(self): # Metodo para actualizar el turno
        self.turnos += 1
        if self.turnos % 2 == 0:
            self.puede_usar_especial = True# Vuelve a activar el ataque especial cada 2 turnos
        self.defensa_temporal = 0 # Reinicia la defensa temporal cada turno

    def esta_vivo(self): # Metodo para verificar si el personaje esta vivo
        return self.vida > 0
    
    def __str__(self): # Metodo para imprimir el personaje, para mostrar sus estadisticas
        return f"{self.nombre} - Vida: {self.vida} - Ataque: {self.ataque} - Especial: {self.especial} - Defensa: {self.defensa}"
    
#--------------------#clase hija#------------------#
class Ripper(Personaje): # Clase hija de Personaje
    Defensa_Base = 12
    def __init__(self): # Constructor de la clase
        super().__init__("Ripper", 20, 30) # Llama al constructor de la clase padre

class Max(Personaje):
    Defensa_Base = 10
    def __init__(self):
        super().__init__("Max", 18, 35)

class Mussulini(Personaje):
    Defensa_Base = 14
    def __init__(self):
        super().__init__("Mussulini", 20, 32)

class Undertaker(Personaje):
    Defensa_Base = 15
    def __init__(self):
        super().__init__("Undertaker", 19, 34)

#-------------------#Lista de personajes#------------------#
#Diccionario de personajes
personajes_disponibles = [
    Ripper(),
    Max(),
    Mussulini(),
    Undertaker()
]

def Limpiar():# Funcion para limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')

def Historia():# Funcion para mostrar la historia del juego
    Limpiar()
    print("""
    |------------------------------------------------------------------------------------|      
    |                                -- Historia del juego --                            |
    |Año 3029. El mundo ha sido reducido a ruinas y las naciones ya no existen.          |
    |La paz es un mito, y la justicia... una reliquia olvidada.                          |
    |                                                                                    |
    |Los sobrevivientes más fuertes, los más despiadados, se enfrentan en un único lugar:|
    |la temida *Arena X*.                                                                |
    |                                                                                    |
    |Aquí no hay reglas. Solo un objetivo:                                               |
    |¡Sobrevivir y convertirse en el Último Guerrero!                                    |
    |                                                                                    |
    |¿Tienes lo que se necesita para dominar la Arena X?                                 |   
    |------------------------------------------------------------------------------------|
    """)
    input("Presiona Enter para Volver al menu...")
    
def Intrucciones():# Funcion para mostrar las instrucciones del juego
    Limpiar()
    print("""
    |-------------------------------------------------------------------------------------------|
    |                               -- Instrucciones del juego --                               |
    |      1. Elige uno de los cuatros peleadores seleccionables para comenzar tu combate.      |
    |      2. Cada personaje tiene habilidades unicas.                                          |
    |      3. El jugador tendra que elegir entre atacar o defenderse.                           |
    |      4. El jugador se va a enfrentar a un enemigo aleatorio controlado por la computadora.|
    |      5. El jugador ganara si logra reducir la vida del enemigo a 0.                       |
    |-------------------------------------------------------------------------------------------|
    """)
    input("Presiona Enter para Volver al menu...")
    
def jugar():# Funcion para jugar el juego.
    Limpiar()
    print("Elige tu personaje:")
    for i, p in enumerate(personajes_disponibles, start = 1):# Enumerate para mostrar los personajes.
        print(f"[{i}] {p.nombre} - Vida: {p.vida} - Ataque: {p.ataque} - Especial: {p.especial} - Defensa: {p.defensa}") #muestra los personajes disponibles.
        
    eleccion = input("Selecciona un personaje (1-4): ")
    while not eleccion.isdigit() or not (1 <= int(eleccion) <= 4): # Verifica que la eleccion sea un numero entre 1 y 4.
        eleccion = input("Opcion invalida. Selecciona un personaje (1-4): ")

    jugador = personajes_disponibles[int(eleccion) - 1] # Selecciona el personaje elegido por el jugador.
    enemigos = personajes_disponibles[:] # Copia la lista de personajes disponibles.
    enemigos.remove(jugador) # Elimina el personaje elegido por el jugador de la lista de enemigos.
    enemigo = random.choice(enemigos) # Selecciona un enemigo aleatorio de la lista de enemigos..

    while jugador.esta_vivo() and enemigo.esta_vivo(): # mientras el jugador y el enemigo esten vivos se ejecuta el combate.
        Limpiar()
        print(f"Tú: {jugador.nombre} - Vida: {jugador.vida}")           #muestra la vida del jugador y del enemigo.
        print(f"Enemigo: {enemigo.nombre} - Vida: {enemigo.vida}")
        print("""
        1. Atacar
        2. Ataque Especial
        3. defenderse    
         """)
        accion = input("Selecciona una acción (1-3): ")

        if accion == "1":
            daño = jugador.usar_ataque() #llama al metodo de ataque para que el jugador ataque.
            enemigo.recibir_daño(daño) #llama al metodo de recibir daño para que el enemigo reciba el daño.
            print(f"Has atacado a {enemigo.nombre} y le has hecho {daño} de daño.")
        elif accion == "2":
            daño = jugador.usar_ataque_especial()#llama al metodo de ataque especial para que el jugador ataque.
            if daño == -1: #se utilza el -1 para verificar si el ataque especial se puede usar.
                    print("Tu ataque especial aún no está disponible.")
            else:
                enemigo.recibir_daño(daño) #si no esta en -1 se llama al metodo de recibir daño para que el enemigo reciba el daño.
                print(f"Has usado tu ataque especial contra {enemigo.nombre} y le has hecho {daño} de daño.")
        elif accion == "3":
            jugador.usar_defensa()#llama al metodo de defensa para que el jugador se defienda.
            print(f"{jugador.nombre} se ha defendido. Su defensa aumentará este turno.")
        else:
            print("Acción inválida. Intenta de nuevo.")
            continue

        if enemigo.esta_vivo(): #si el enemigo sigue vivo puede ejecutar las siguientes acciones.
            accion_cpu = random.choice(["ataque", "especial", "defensa"]) #selecciona una accion aleatoria para el enemigo.
            if accion_cpu == "especial":
                daño = enemigo.usar_ataque_especial()#llama al metodo de ataque especial para que el enemigo ataque.
                if daño != -1: #si el ataque especial no es -1 se llama al metodo de recibir daño para que el jugador reciba el daño.
                    jugador.recibir_daño(daño)
                    print(f"{enemigo.nombre} ha usado su ataque especial y te ha hecho {daño} de daño.")
                else: #si el ataque especial es -1 el enemigo usara su ataque normal.
                    daño = enemigo.usar_ataque() #llama al metodo de ataque para que el enemigo ataque.
                    jugador.recibir_daño(daño)#llama al metodo de recibir daño para que el jugador reciba el daño.
                    print(f"{enemigo.nombre} te ha atacado y te ha hecho {daño} de daño.")
            elif accion_cpu == "ataque": #si la accion aleatoria es ataque el enemigo atacara.
                daño = enemigo.usar_ataque()
                jugador.recibir_daño(daño)
                print(f"{enemigo.nombre} te ha atacado y te ha hecho {daño} de daño.")
            else:#si la accion aleatoria es defensa el enemigo se defendera.
                enemigo.usar_defensa()#llama al metodo de defensa para que el enemigo se defienda.
                print(f"{enemigo.nombre} se ha defendido. Su defensa aumentará este turno.")

        jugador.actualizar_turno()#llama al metodo de actualizar turno para que el jugador actualice su turno.
        enemigo.actualizar_turno()#llama al metodo de actualizar turno para que el enemigo actualice su turno.
        time.sleep(3)

    Limpiar()
    if jugador.esta_vivo():# si el jugador sigue vivo se imprime el mensaje de victoria.
        print(f"¡Has ganado! {jugador.nombre} ha derrotado a {enemigo.nombre}.")
    else:# si el jugador no sigue vivo se imprime el mensaje de derrota.
        print(f"¡Has perdido! {enemigo.nombre} ha derrotado a {jugador.nombre}.")
    input("Presiona Enter para volver al menú...")

def Opciones_menu(): # Funcion para mostrar el menu de opciones.
    while True: # Bucle infinito para mostrar el menu de opciones.
        Limpiar()
        print("""
        |----------------------------------------------------------------|
        |                                                                |
        |  █████╗  ██████╗   ███████╗ ███╗   ██╗  █████╗        ██╗  ██╗ |
        | ██╔══██╗ ██╔══██╗  ██╔════╝ ████╗  ██║ ██╔══██╗       ╚██╗██╔╝ |
        | ███████║ ██████╔╝  █████╗   ██╔██╗ ██║ ███████║        ╚███╔╝  |
        | ██╔══██║ ██╔══██╗  ██╔══╝   ██║╚██╗██║ ██╔══██║        ██╔██╗  |
        | ██║  ██║ ██║  ║██╗ ███████╗ ██║ ╚████║ ██║  ██║       ██╔╝ ██╗ |
        | ╚═╝  ╚═╝ ╚═╝  ╚══╝ ╚══════╝ ╚═╝  ╚═══╝ ╚═╝  ╚═╝       ╚═╝  ╚═╝ |
        |----------------------------------------------------------------|
              
        |----------------------------------------------------------------|
        |                             1. Historia                        |
        |                             2. Instrucciones                   |
        |                             3. Jugar                           |
        |                             4. Salir                           |
        |----------------------------------------------------------------|""")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            Historia()
        elif opcion == "2":
            Intrucciones()
        elif opcion == "3":
            jugar()
        elif opcion == "4":
            Limpiar()
            print("Gracias por jugar. ¡Hasta la próxima!")
            print("Creado por: Gabriel Rivero - 2025")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
            time.sleep(2)
            Limpiar()

Opciones_menu() # Llama a la funcion de opciones del menu para iniciar el juego.

