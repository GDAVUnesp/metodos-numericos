def timer(): #exclusivamente para cálculo do tempo de execução
    from time import time
    return time()


#função para cálculo da regra dos trapezios
def regra_trapezios(fx, a, b, n): 
    def f(x): #define uma função f (usada para calcular y)
        return eval(fx)  #função nativa do python que transforma uma string em expressão (precisa de um x definido)

    h = (b - a) / n #cálculo do passo
    resultado_RT = f(a) + f(b) #somando os intervalos limites, y0 e yn por estarem fora da somatória

    for i in range(1, n): #somatória de yi com i indo de 1 até n - 1
        x = a + i * h #calcula o x com base no limite inferior do intervalo, o indice i multiplicado pelo passo
        resultado_RT += 2 * f(x) #resultado de y multiplicado por 2

    resultado_RT *= h / 2 #a soma de todas os pontos multiplicado por h/2
    return resultado_RT #retorna o resultado


#função para cálculo de 1/3 de Simpson
def um_terco_simpson(fx, a, b, n):
    def f(x): #define uma função f (usada para calcular y)
        return eval(fx) #função nativa do python que transforma uma string em expressão (precisa de um x definido)

    if n % 2 != 0: #verifica se o número de subintervalos é par, requisito para aplicação do método, se não for, define como não aplicável
        print("1/3 de Simpson: NAO APLICAVEL - A regra de 1/3 de Simpson precisa de um numero par de intervalos.")
        resultado_UTS = "NAO APLICAVEL"
        return resultado_UTS
    else:
        h = (b - a) / n #cálculo do passo
        resultado_UTS = f(a) + f(b) #somando os intervalos limites, y0 e yn por estarem fora da somatória

        for i in range(1, n): #somatória de yi com i indo de 1 até n - 1
            x = a + i * h  #calcula o x com base no limite inferior do intervalo, o indice i multiplicado pelo passo
            if i % 2 == 0: #se o indice for par, multiplica por 2, caso contrário, multiplica por 4 
                resultado_UTS += 2 * f(x) 
            else:
                resultado_UTS += 4 * f(x) #resultado incrementado pelo valor de y 

        resultado_UTS *= h / 3 #multiplica o resultado 
        return resultado_UTS #retorna o resultado


#função para cálculo de 3/8 de Simpson
def tres_oitavos_simpson(fx, a, b, n):
    def f(x): #define uma função f (usada para calcular y)
        return eval(fx) #função nativa do python que transforma uma string em expressão (precisa de um x definido)

    if n % 3 != 0: #Verifica se o número de subintervalos é múltiplo de 3, requisito para aplicação do método, se não for, define como não aplicável
        print("1/3 de Simpson: NAO APLICAVEL - A regra de 3/8 de Simpson precisa de um intervalo múltiplo de 3.")
        resultado_TOS = "NAO APLICAVEL"
        return resultado_TOS
    else:
        h = (b - a) / n #calculo do passo
        resultado_TOS = f(a) + f(b) #somando os intervalos limites, y0 e yn por estarem fora da somatória

        for i in range(1, n):
            x = a + i * h #calcula o x com base no limite inferior do intervalo, o indice i multiplicado pelo passo
            if i % 3 == 0: #se for múltiplo de 3, yi é multiplicado por 2, se não for, é multiplicado por 3
                resultado_TOS += 2 * f(x)
            else:
                resultado_TOS += 3 * f(x) 

        return resultado_TOS * (3 * h / 8) #retorna o resultado
    

#função para calculo de erros
def calculo_de_erros(valor_exato,valor_aproximado):

    erro_absoluto = abs(valor_exato-valor_aproximado) #o erro absoluto é o valor exato - valor aprocimado em módulo
    erro_relativo = abs(erro_absoluto/valor_exato) #o erro relativo é o erro absoluto/valor exato

    return erro_absoluto, erro_relativo #retorna os erros



funcao = input("Digite a função f(x) utilizando sempre 'x' como variavel: ") 
funcao = funcao.replace("^", "**")  #transforma ^ em ** para simbolizar o expoente e deixa em caixa baixa
a = float(input("Digite o valor de a no intervalo: ")) #limite inferior do intervalo
b = float(input("Digite o valor de b no intervalo: ")) #limite superior do intervalo
n = int(input("Numero de subintervalos n: ")) #número de subintervalos
valor_exato = float(input("Valor exato: ")) #O valor exato da função


start = timer() #começa a contar o tempo de execução 
resultado_trapezios = regra_trapezios(funcao, a, b, n) #executa a função de cálculo da regra dos trapézios
end = timer() #finaliza tempo de execução
erro_absoluto, erro_relativo = calculo_de_erros(valor_exato,resultado_trapezios) #calcula os erros
print("\n\nValor aproximado pela regra dos trapézios:", resultado_trapezios) #apresenta resultados
print("Erro absoluto:", erro_absoluto)
print("Erro relativo:", erro_relativo)
print("Numero de subintervalos:", n)
print("Tempo de execução:", end - start)


start = timer() #começa a contar o tempo de execução 
resultado_terco_simpson = um_terco_simpson(funcao, a, b, n) #executa a função de cálculo da regra dos trapézios
end = timer() #finaliza tempo de execução
erro_absoluto, erro_relativo = calculo_de_erros(valor_exato,resultado_terco_simpson) #calcula os erros
print("\n\nValor aproximado pela regra 1/3 de Simpson:", resultado_terco_simpson) #apresenta resultados
print("Erro absoluto:", erro_absoluto)
print("Erro relativo:", erro_relativo)
print("Numero de subintervalos:", n)
print("Tempo de execução:", end - start)


start = timer() #começa a contar o tempo de execução 
resultado_oitavo_simpson = tres_oitavos_simpson(funcao, a, b, n) #executa a função de cálculo da regra dos trapézios
end = timer() #finaliza tempo de execução
erro_absoluto, erro_relativo = calculo_de_erros(valor_exato,resultado_oitavo_simpson) #calcula os erros
print("\n\nValor aproximado pela regra 3/8 de Simpson:", resultado_oitavo_simpson) #apresenta resultados
print("Erro absoluto:", erro_absoluto)
print("Erro relativo:", erro_relativo)
print("Numero de subintervalos:", n)
print("Tempo de execução:", end - start)



