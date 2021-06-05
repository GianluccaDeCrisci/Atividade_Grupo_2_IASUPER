from contatos import Contatos

class Controlador():
  def inserir(nome, endereco, telefone1, telefone2, aniversario, email):
    return Contatos(nome, endereco, telefone1, telefone2, aniversario, email)

  def listarAll(agendaTelefonica):
    for user in agendaTelefonica:
      print('Nome: {} | Endereço: {} | Telefone 1: {} | Telefone 2: {} | Aniversário: {} | Email: {}'.format(user.getNome(), user.getEndereco(), user.getTelefone1(), user.getTelefone2(), user.getAniversario(), user.getEmail()))

  def listarNome(agendaTelefonica, nome):
    cont = 0
    for user in agendaTelefonica:
      if user.getNome() == nome:
        print('Nome: {} | Endereço: {} | Telefone 1: {} | Telefone 2: {} | Aniversário: {} | Email: {}'.format(user.getNome(), user.getEndereco(), user.getTelefone1(), user.getTelefone2(), user.getAniversario(), user.getEmail()))
        break
      cont += 1
    print('Nome não encontrado na Agenda!')

  def listarEmail(agendaTelefonica, email):
    cont = 0
    for user in agendaTelefonica:
      if user.getEmail() == email:
        print('Nome: {} | Endereço: {} | Telefone 1: {} | Telefone 2: {} | Aniversário: {} | Email: {}'.format(user.getNome(), user.getEndereco(), user.getTelefone1(), user.getTelefone2(), user.getAniversario(), user.getEmail()))
        break
      cont += 1
    print('Email não encontrado na Agenda!')

  def deletarAll(agendaTelefonica):
    if len(agendaTelefonica) != 0:
      agendaTelefonica.clear()
      return 'Todos os contatos foram removidos!'
    else:
      return 'A Agenda telefonica está vazia!'

  def deletarNome(agendaTelefonica, nome):
    if len(agendaTelefonica) != 0:
      cont = 0
      for user in agendaTelefonica:
        if user.getNome() == nome:
          agendaTelefonica.pop(cont)
          return 'Contado {} removido com sucesso!'.format(nome)
        else:
          return 'Nome não encontrado na Agenda!'
    else:
      return 'Agenda está vazia!'

  def nomeDuplicado(agendaTelefonica, nome):
    for user in agendaTelefonica:
        if nome == user.getNome():
            return True
    return False

  def salvarArquivo(agendaTelefonica):
    arquivo = open('agendaTelefonica.txt','w+')
    if len(agendaTelefonica) != 0:
      for user in agendaTelefonica:
        arquivo.writelines('Nome: {} | Endereço: {} | Telefone 1: {} | Telefone 2:{} | Aniversário: {} | Email: {}\n'.format(user.getNome(), user.getEndereco(), user.getTelefone1(), user.getTelefone2(), user.getAniversario(), user.getEmail()))
        return 'Agenda salva com sucesso!'
    else:
      return 'Não há nada para salvar, sou agenda está vazia!'

  def lerArquivo():
    arquivo = open('agendaTelefonica.txt','r')
    for line in arquivo:
      print(line)
 
  def sort(agenda):
    agenda.sort(key=lambda x: x.name)
    return 'Agenda Organizada com Sucesso!'