from controlador import Controlador

agenda = []

print('~'*40)
print('Bem vindo a Agenda telefonica do Grupo 3')
print('~'*40)

while True:
  print('\n1 - Cadastrar contato.')
  print('2 - Listar contato.')
  print('3 - Listar todos os contatos.')
  print('4 - Apagar contato.')
  print('5 - Apagar todos os contatos.')
  print('6 - Salvar Ageenda no arquivo txt.')
  print('7 - Ver Ageenda salva no arquivo.')
  print('8 - Organizar a Agenda em ordem alfabética.')
  print('9 - Sair.')

  escolha = int(input('Entre com a opção desejada: '))

  if escolha == 1:
    nome = input('Digite o nome:')
    if not (Controlador.nomeDuplicado(agenda, nome)):
      endereco = input('Digite o endereço:')
      telefone1 = int(input('Digite o telefone1:'))
      telefone2 = int(input('Digite o telefone2:'))
      aniversario = input('Digite o aniversario:')
      email = input('Digite o email:')
      agenda.append(Controlador.inserir(nome, endereco, telefone1, telefone2, aniversario, email))
      print('Contato adicionado com sucesso!')
  elif escolha == 2:
    print('\nEscolha a forma da pesquisa:')
    print('1 - Através do nome.')
    print('2 - Através do email.')
    escolha_procura = int(input('Entre com a opção desejada: '))
    if escolha_procura == 1:
      nome = input('Digite o nome para a pesquisa:')
      Controlador.listarNome(agenda, nome)
    elif escolha_procura == 2:
      email = input('Digite o email para a pesquisa:')
      Controlador.listarEmail(agenda, email)
  elif escolha == 3:
    Controlador.listarAll(agenda)
  elif escolha == 4:
    nome = input('Digite o nome para deletar da lista:')
    print(Controlador.deletarNome(agenda, nome))
  elif escolha == 5:
    print(Controlador.deletarAll(agenda))
  elif escolha == 6:
    print(Controlador.salvarArquivo(agenda))
  elif escolha == 7:
    Controlador.lerArquivo()
  elif escolha == 8:
    print(Controlador.sort(agenda))
  elif escolha == 9:
    break
  else:
    print('Digite a opção correta!')

print('\nObrigado por usar a nossa agenda!!!')
print('~'*40)
