import Personagem as personagem
import Model as model

class Animal(personagem.Personagem): 

    def __init__(self, nome, vida, ataque, defesa, agilidade, statusVida, especie, movimento, habitat, idade):
        super().__init__(nome, vida, ataque, defesa, agilidade, statusVida)
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.agilidade = agilidade
        self.statusVida = statusVida
        self.especie = especie
        self.movimento = movimento
        self.habitat = habitat
        self.idade = idade

    def cadastrarAnimal(self):
        idAnimal = model.Model.getNovoId(self, "animais")
        animalNome = str(input("Digite o nome do animal a ser criado:  "))
        vida = int(input("Digite a vida do animal:  "))
        ataque = int(input("Digite o ataque do animal:  "))
        defesa = int(input("Digite a defesa do animal:  "))
        agilidade = int(input("Digite a agilidade do animal:  "))
        statusVida = "vivo"
        especie = str(input("Digite a especie do animal:  "))
        movimento = str(input("Digite o movimento do animal:  "))
        habitat = str(input("Digite o habitat do animal:  "))
        idade = int(input("Digite a idade do animal:  "))
        data = {
            "id": idAnimal,
            "nome": animalNome,
            "vida": vida,
            "ataque": ataque,
            "defesa": defesa,
            "agilidade": agilidade,
            "statusVida": statusVida,
            "especie": especie,
            "movimento": movimento,
            "habitat": habitat,
            "idade": idade
        }
        resposta = model.Model.setDadosApi(self, "animais", data)
        if(resposta):
            print("Animal Cadastrado com sucesso")
            return True
        else:
            print('Ouve um erro ao cadastrar o animal')
            return False
