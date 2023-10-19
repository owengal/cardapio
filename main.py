print('Bem-vindo a lanchonete da Galdina Silva de Souza RU: 4370444')
print('-------------------CARDÁPIO-------------------')
print('|Código   |       Descrição       |  Valor R$|')
print('|   100   |    Cachorro-quente    |  9,00    |')
print('|   101   | Cachorro-quente duplo |  11,00   |')
print('|   102   |        X-egg          |  12,00   |')
print('|   103   |        X-salada       |  13,00   |')
print('|   104   |        X-bacon        |  14,00   |')
print('|   105   |        X-tudo         |  17,00   |')
print('|   200   |   Refrigerante lata   |  5,00    |')
print('|   201   |      Chá gelado       |  4,00    |')
print('----------------------------------------------')
acumulador = 0 #criei uma variável chamada acumulador para acumular os valores dos pedidos e retornar o total no fim
while True: #criei um loop com o while para repetir as opções até ser encerrado pelo cliente
    codigo = input('Digite o código do pedido desejado:') #variavel criada pro cliente digitar o código do pedido
    if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201':
        #criei uma condição para que se a pessoa digitar um código diferente desses citados retorne a opção inválida
        print('Opção inválida')
        continue #coloquei o continue caso continue no erro fique voltando ao começo
    if codigo == '100':
        #digitei a condição para mostrar na tela o pedido referente ao código digitado para cada item do cardápio
        print('Você pediu um cachorro-quente no valor de 9,00')
        acumulador = acumulador + 9
        #variável acumulador colocada para ir somando o total do pedido
    elif codigo == '101':
        print('Você pediu um cachorro-quente duplo no valor de 11,00')
        acumulador = acumulador + 11
    elif codigo == '102':
        print('Você pediu um x-egg no valor de 12,00')
        acumulador = acumulador + 12
    elif codigo == '103':
        print('Você pediu um x-salada no valor de 13,00')
        acumulador = acumulador + 13
    elif codigo == '104':
        print('Você pediu um x-bacon no valor de 14,00')
        acumulador = acumulador + 14
    elif codigo == '105':
        print('Você pediu um x-tudo no valor de 17,00')
        acumulador = acumulador + 17
    elif codigo == '200':
        print('Você pediu um refrigerante lata no valor de 5,00')
        acumulador = acumulador + 5
    elif codigo == '201':
        print('Você pediu um chá gelado no valor de 4,00')
        acumulador = acumulador + 4

    mais_pedido = input('Deseja pedir mais alguma coisa?'
                        '\n1 - Sim'
                        '\n2 - Não')
    #variável criada para quando o cliente digitar um pedido, perguntar novamente se deseja mais alguma coisa ou se deseja encerrar o pedido
    if mais_pedido == '1':
        #condição criada para que se o cliente digitar 1 querendo continuar a operação, irá retornar para o primeiro passo seguido do 'continue' abaixo desse código
        continue
    else:
        #caso a escolha seja finalizar irá aparecer na tela o valor total do pedido que foi somado na variável 'acumulador'
        print('O total a ser pago é: R${:.2f}'.format(acumulador))
        #break utilizado para finalizar o loop do while e finalizar a operação
        break
