class Contatos():
  def __init__(self, nome, endereco, telefone1, telefone2, aniversario, email):
    self.nome = nome
    self.endereco = endereco
    self.telefone1 = telefone1
    self.telefone2 = telefone2
    self.aniversario = aniversario
    self.email = email

  def getNome(self):
    return self.nome

  def getEndereco(self):
    return self.endereco
  
  def getTelefone1(self):
    return self.telefone1

  def getTelefone2(self):
    return self.telefone2

  def getAniversario(self):
    return self.aniversario

  def getEmail(self):
    return self.email
  