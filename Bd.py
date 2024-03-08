import sqlite3

class AnimalDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS animais 
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                especie TEXT NOT NULL,
                                idade INTEGER NOT NULL)''')
        self.conn.commit()

    def adicionar_animal(self, animal):
        self.cursor.execute('''INSERT INTO animais (nome, especie, idade) 
                               VALUES (?, ?, ?)''', (animal.nome, animal.especie, animal.idade))
        self.conn.commit()

    def listar_animais(self):
        self.cursor.execute('''SELECT * FROM animais''')
        return self.cursor.fetchall()

    def buscar_animal(self, id):
        self.cursor.execute('''SELECT * FROM animais WHERE id=?''', (id,))
        return self.cursor.fetchone()

    def atualizar_animal(self, animal):
        self.cursor.execute('''UPDATE animais SET nome=?, especie=?, idade=? WHERE id=?''',
                            (animal.nome, animal.especie, animal.idade, animal.id))
        self.conn.commit()

    def deletar_animal(self, id):
        self.cursor.execute('''DELETE FROM animais WHERE id=?''', (id,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()
