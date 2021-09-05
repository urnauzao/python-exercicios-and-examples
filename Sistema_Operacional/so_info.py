import platform
import getpass
from datetime import datetime

print('\n     INFORMAÇÕES DO SISTEMA OPERACIONAL')
print("Nome da Maquina:.................", platform.node())
print("Arquitetura:.....................", platform.architecture())
print("Sistema Operacional:.............", platform.system())
print("Versao do SO:....................", platform.release())
print("Processador:.....................", platform.processor())
print("Versao do Python:................", platform.python_version())

print('\n\n\n     INFORMAÇÕES DE DATA')
print('Data:...', datetime.now())
print('Horas:..', datetime.now().time())
print('Dia:....', datetime.now().day)
print('Mês:....', datetime.now().month)
print('Ano:....', datetime.now().year)

print('\n\n\n     INFORMAÇÕES DE USUÁRIO')
print(getpass.getuser())
# para opção abaixo, edite a opção de run(Execução), e habilite "Emulate terminal in output console"
print(getpass.getpass("Digite sua senha:..."))

print('\n\n\n     SIMULANDO LOGIN')
usuario=getpass.getuser()
senha=getpass.getpass("Digite sua senha:...")

if(usuario.upper() == 'URNAUZAO' and senha == '12345678'):
    print("Bem-vindo ao sistema!")
else:
    print("Você não tem permissão!")


