# O decorator @classmethod serve para transformar um método de instância em um método de classe.
# O método não precisa de uma instância da classe para ser chamado
# Ele é chamado diretamente na classe e tem acesso ao objeto cls, que representa a classe em si (diferente de self, que representa uma instância).

# O primeiro argumento que ele recebe é a própria classe (cls), e não uma instância dela (self).
# Isso permite que você acesse e modifique atributos da classe e chame outros métodos de classe.

class Person:
    specie = 'Human'  # Atributo de classe

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_specie(cls, new_specie):
        cls.specie = new_specie
        # Person.specie = new_specie

    def change_name(self, new_name):
        self.name = new_name
        # obj.name = new_name

    def hello(self):
        print(
            f'My name is {self.name}. Im {self.age} years old. Im a {self.specie}')


obj1 = Person(name='John', age=30)
obj1.hello()
print(obj1.specie)
obj1.specie = 'Elf'
print(obj1.specie)
obj1.hello()

# Usando o classmethod para modificar o atributo de classe sem instanciar
Person.change_specie('Alien')
print(obj1.specie)
obj1.hello()
print(Person.specie)

# # Instanciando e observando o efeito do classmethod
# obj = Person('Doe', 30)
# obj.hello()


class Foo(object):
    def __init__(self):
        pass

    def bar(self, a, b, c):
        print(a, b, c)


foo = Foo()
foo.bar(1, 2, 3)

fn = foo.bar    # fn aqui é um bound method, ligado a "foo"
fn(1, 2, 3)     # Ainda passa "foo" como 1º argumento para "bar"
