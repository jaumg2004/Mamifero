from abc import ABC, abstractmethod

class Mamifero(ABC):
    def __init__(this, nome, vida):
        this._nome = nome
        this._vida = vida

    @abstractmethod
    def emitir_som(self):
        pass

    def mostrar_info(self):
        print(f"Nome: {self._nome}")
        print(f"Vida: {self._vida}")

class Aquatico(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Cachorro(Mamifero):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def emitir_som(self):
        print("auauaau")

class Boi(Mamifero):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def emitir_som(self):
        print("muuuuu")

class Lontra(Mamifero, Aquatico):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def emitir_som(self):
        print("uuhhhhhhau")

    def nadar(self):
        print(f"{self._nome} está nadando")


cachorro = Cachorro("Doki", 1000.0)
boi = Boi("Oddy", 1500.0)
lontra = Lontra("Ari", 2000.0)


lontra.emitir_som()
lontra.mostrar_info()
lontra.nadar()

cachorro.emitir_som()
cachorro.mostrar_info()

boi.emitir_som()
boi.mostrar_info()
