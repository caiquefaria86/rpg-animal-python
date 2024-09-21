import Model as model
import random
class Ambiente:
    def __init__(self, nome):
        self.nome = nome

    def verificaDesvantagens(self, nome, habitatePersonagem):
        print("A desvantagem do ambiente é: ")

    def defineAmbiente(self, ambientes):
        ambientes = model.Model.getDadosApi(self,"ambientes")
        qtdAmbientes = len(ambientes.json())
        alet = random.randint(0, qtdAmbientes - 1)
        print("O ambiente definido foi ", ambientes.json()[alet]['nome'])
        return ambientes.json()[alet]['nome']

    def cadastrarAmbiente(self):
        idAmbiente = model.Model.getNovoId(self, "ambientes")
        ambienteNome = str(input("Digite o nome do ambiente a ser criado:  "))
        data = {
            "id": idAmbiente,
            "nome": ambienteNome
        }
        resposta = model.Model.setDadosApi(self, "ambientes", data)
        if(resposta):
            print("Ambiente Cadastrado com sucesso")
            return True
        else:
            print('Ouve um erro ao cadastrar o ambiente')
            return False

