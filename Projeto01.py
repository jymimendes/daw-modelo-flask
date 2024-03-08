class Animal:
    def __init__(self, id, nome, especie, idade):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Espécie: {self.especie}, Idade: {self.idade}"


if __name__ == "__main__":
    db = AnimalDB("fazenda.db")

    novo_animal = Animal(None, "Branquinho", "Vaca", 5)
    db.adicionar_animal(novo_animal)

    print("Lista de Animais:")
    for animal in db.listar_animais():
        print(animal)

    animal_id = 1
    animal_encontrado = db.buscar_animal(animal_id)
    print(f"\nAnimal encontrado com ID {animal_id}: {animal_encontrado}")
  
    animal_encontrado.nome = "Branquinha"
    db.atualizar_animal(animal_encontrado)

    db.deletar_animal(animal_id)

    db.fechar_conexao()

