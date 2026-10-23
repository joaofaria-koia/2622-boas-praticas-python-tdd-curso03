from bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario("Teste", "23/03/2000", 1111)
    print(f"Teste = {funcionario_teste.idade()}")

teste_idade()