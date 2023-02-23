menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
""";

saldoConta = 0;
limiteRetirada = 500;
numero_saques = 0;
LIMITE_SAQUES = 3;
extrato = "";

while True:

    opcaoEscolhida = input(menu);

    if opcaoEscolhida == "d" :
        valorParaDeposito = input("Digite o valor para deposito: ");

        if valorParaDeposito.isnumeric() :
            valorParaDeposito = float(valorParaDeposito);
            if valorParaDeposito > 0 :
                saldoConta += valorParaDeposito;
                valorParaExibirExtrato = format(valorParaDeposito, '.2f');
                extrato += "Valor Depositado: R$ " + valorParaExibirExtrato + "\n";
            else:
                print("O valor digitado é inválido. Apenas valores maiores que zero e positivos.");
        else:
            print("O valor digitado é inválido. Apenas valores maiores que zero e positivos.");

    elif opcaoEscolhida == "s" :
        valorParaSaque = input("Digite o valor para saque: ");

        if valorParaSaque.isnumeric() :
            valorParaSaque = float(valorParaSaque);
            if(valorParaSaque > saldoConta):
                print("O valor para saque é menor do que o disponivel em conta.");
            else:
                if(numero_saques >= LIMITE_SAQUES):
                    print("Você atingiu o limite maximo de tentativas de saque diarios.");
                else:
                    if valorParaSaque > 500.00:
                        print("O limite para cada saque é de R$500,00");
                    else:
                        saldoConta += valorParaSaque;
                        valorParaExibirExtrato = format(valorParaSaque, '.2f');
                        extrato += "Valor Retirado: R$ " + valorParaExibirExtrato + "\n";
                        numero_saques += 1;

        else:
            print("O valor digitado é inválido. Apenas valores maiores que zero e positivos.");
    elif opcaoEscolhida == "e" :
        if len(extrato) > 0 :
            print(extrato);
        else:
            print("Não foram realizadas movimentações");
    elif opcaoEscolhida == "q" :
        raise SystemExit;

