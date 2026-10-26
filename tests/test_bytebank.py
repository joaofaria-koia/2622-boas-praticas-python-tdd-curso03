from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_26(self):
        # Given - Contexto
        entrada = "13/03/2000"
        esperado = 26

        funcionario_teste = Funcionario("Teste", entrada, 1200)
        # When - Ação
        resultado = funcionario_teste.idade()

        # Then - Desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        # Given - Contexto
        entrada = "Lucas Carvalho "
        esperado = "Carvalho"

        # When - Ação
        lucas = Funcionario(entrada, "11/11/2000", 1231)
        resultado = lucas.sobrenome()

        # Then - Desfecho
        assert resultado == esperado