op = 17
saldo = 0
while(True):
  print("Sistema Bancario")
  print("\nBem vindo Eduardo Antunes")
  print("\n 1- Deposito")
  print("\n 2- Saque")
  print("\n 3- Extrato")
  print("\n 0- Sair")
  op = int(input())
  if(op == 1):
    print("\nQual valor deseja depositar ?")
    dep = float(input())
    if(dep > 0):
      saldo+=dep
      print("\nDeposito realizado com sucesso")
    else:
      print("\nValor de deposito incorreto")
  elif(op == 2):
    print("\nQual valor deseja sacar ?")
    saq = float(input())
    if(saldo >= saq):
      saldo-=saq
      print("\nSaque realizado com sucesso")
    else:
      print("\nSaldo insuficiente")
  elif(op == 3):
    print(f'\nSaldo: {saldo:,.2f}')
  elif(op == 0):
    break
  else:
    print("opcao invalida")

