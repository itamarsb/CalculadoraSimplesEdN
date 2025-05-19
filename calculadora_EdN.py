# Função responsável por realizar a operação matemática
def calcular(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            raise ZeroDivisionError   # Lança erro específico para divisão por zero
        return num1 / num2
    else:
        raise Exception  # Se a operação não for reconhecida, será tratado como "Operação Inválida"

# Função principal que orquestra a interação com o usuário
def main():
    # Mensagens de introdução e instruções
    print("Calculadora Simples - Escola da Nuvem - Turma BRSAO182 - Itamar")
    print("Operações válidas: + (adição), - (subtração), * (multiplicação), / (divisão)")
    print("Não digite zero para divisões")
    print("Operações simples, utilizando apenas números e inteiros - Não inventa moda...")

    while True:
        try:
            # Solicita o primeiro número
            entrada1 = input("Digite o primeiro número: ")
            try:
                num1 = float(entrada1) # Tenta converter para número
            except ValueError:
                # Mensagem personalizada se a entrada não for numérica
                raise ValueError("Entrada Inválida - Apenas números e inteiros - Te falei pra não inventar moda...")

            # Solicita o segundo número
            entrada2 = input("Digite o segundo número: ")
            try:
                num2 = float(entrada2) # Tenta converter para número
            except ValueError:
                # Mesma validação para o segundo número
                raise ValueError("Entrada Inválida - Apenas números e inteiros - Te falei pra não inventar moda...")
            
            # Solicita a operação desejada
            operacao = input("Digite a operação (+, -, *, /): ").strip()

            # Chama a função de cálculo com os dados fornecidos
            resultado = calcular(num1, num2, operacao)

        # Captura e exibe erro de entrada inválida (não numérica)
        except ValueError as ve:
            print(f"Erro: {ve}. Tente novamente.\n")
            continue
        # Captura erro específico de divisão por zero
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida. Tente novamente.\n")
            continue
        # Captura qualquer outro erro (ex: operação inválida)
        except:
            print("Erro: Operação Inválida. Tente novamente.\n")
            continue
        else:
            # Se tudo ocorreu corretamente, mostra o resultado e encerra
            print(f"\nResultado: {num1} {operacao} {num2} = {resultado}\n")
            print("Operação finalizada com sucesso.")
            break

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
