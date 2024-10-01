# O decorator @property serve para que "um método se comporte como um atributo".
# Usando @property, é como se o retorno do método fosse um atributo da classe.
# Métodos que tenham @property devem ser chamados sem (), já que "são atributos, e não métodos da classe".


class Person:
    def __init__(self, name) -> None:
        self.name = name

    @property
    def get_name(self) -> str:
        return self.name
    
obj = Person(name='Doe')
print(obj.get_name)