def timer():
    from time import time
    return time()

def regra_trapezios(fx, a, b, n):
    def f(x):
        return eval(fx)

    h = (b - a) / n
    resultado_RT = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        resultado_RT += 2 * f(x)

    resultado_RT *= h / 2
    return resultado_RT

   
def um_terco_simpson(fx, a, b, n):
    def f(x):
        return eval(fx)

    if n % 2 != 0:
        print("1/3 de Simpson: NAO APLICAVEL - A regra de 1/3 de Simpson precisa de um numero par de intervalos.")
        resultado_UTS = "NAO APLICAVEL"
        return resultado_UTS
    else:
        h = (b - a) / n
        resultado_UTS = f(a) + f(b)

        for i in range(1, n):
            x = a + i * h
            if i % 2 == 0:
                resultado_UTS += 2 * f(x)
            else:
                resultado_UTS += 4 * f(x)

        resultado_UTS *= h / 3
        return resultado_UTS
    
def tres_oitavos_simpson(fx, a, b, n):
    def f(x):
        return eval(fx)

    if n % 3 != 0:
        print("1/3 de Simpson: NAO APLICAVEL - A regra de 3/8 de Simpson precisa de um intervalo múltiplo de 3.")
        resultado_TOS = "NAO APLICAVEL"
        return resultado_TOS
    else:
        h = (b - a) / n
        resultado_TOS = f(a) + f(b)

        for i in range(1, n):
            x = a + i * h
            if i % 3 == 0:
                resultado_TOS += 2 * f(x)
            else:
                resultado_TOS += 3 * f(x)

        return resultado_TOS * (3 * h / 8)
    
def calculo_de_erros(valor_exato,valor_aproximado):

    erro_absoluto = abs(valor_exato-valor_aproximado)
    erro_relativo = abs(erro_absoluto/valor_exato)

    return erro_absoluto, erro_relativo



funcao = input("Digite a função f(x) utilizando sempre 'x' como variavel: ") 
funcao = funcao.replace("^", "**")  #transforma ^ em ** para simbolizar o expoente e deixa em caixa baixa
a = float(input("Digite o valor de a no intervalo: "))
b = float(input("Digite o valor de b no intervalo: "))
n = int(input("Numero de subintervalos n: "))
valor_exato = float(input("Valor exato: "))

start = timer()
resultado_trapezios = regra_trapezios(funcao, a, b, n)
erro_absoluto, erro_relativo = calculo_de_erros(valor_exato,resultado_trapezios)
end = timer()
print("Valor aproximado pela regra dos trapézios:", resultado_trapezios)
print("Erro absoluto:", erro_absoluto)
print("Erro relativo:", erro_relativo)
print("Numero de subintervalos:", n)
print("Tempo de execução:", end - start)


start = timer()
resultado_terco_simpson = um_terco_simpson(funcao, a, b, n)
erro_absoluto, erro_relativo = calculo_de_erros(valor_exato,resultado_terco_simpson)
end = timer()
print("Valor aproximado pela regra 1/3 de Simpson:", resultado_terco_simpson)
print("Erro absoluto:", erro_absoluto)
print("Erro relativo:", erro_relativo)
print("Numero de subintervalos:", n)
print("Tempo de execução:", end - start)


start = timer()
resultado_oitavo_simpson = tres_oitavos_simpson(funcao, a, b, n)
erro_absoluto, erro_relativo = calculo_de_erros(valor_exato,resultado_oitavo_simpson)
end = timer()
print("Valor aproximado pela regra 3/8 de Simpson:", resultado_oitavo_simpson)
print("Erro absoluto:", erro_absoluto)
print("Erro relativo:", erro_relativo)
print("Numero de subintervalos:", n)
print("Tempo de execução:", end - start)



