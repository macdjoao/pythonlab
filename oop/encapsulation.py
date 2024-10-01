# Encapsulamento

# Em python, usamos dois underlines para indicar que um atributo/método é privado.
# Um atributo/método privado indica que, aquele atributo/método só deve ser acessado/usado, DIRETAMENTE, pela própria classe.
# Quando usamos atributos privados, o recomendado é que se utilize "getters" e "setters" para acessar/alterar esses atributos.


class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.__doc = None # Atributo privado
        self.id = None

    def get_doc(self) -> str:
        print(f'doc: {self.__doc}')
        return self.__doc
    
    def set_doc(self, doc: str) -> None:
        self.__doc = doc
        self.id = self.__generate_id()

    def __generate_id(self): # Método privado
        return f'{self.name}{self.__doc}'

obj = Person(name='Doe')
obj.get_doc()
print(f'id: {obj.id}')
obj.set_doc(doc='ABC123')
obj.get_doc()
print(f'id: {obj.id}')