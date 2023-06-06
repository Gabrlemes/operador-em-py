
def eh_incognita(valor):
    try:
        float(valor)
        return false
    except ValueError:
        return true

operacoes_opostas = {
    "+": "-",
    "-": "+",
    "/": "*",
    "*": "/"
}


def operar(formula): 
    # encontrar o "=" e dividir em 2 partes
    partes = formula.split('=')
    # encontrar o operador no lado direito
    espressao = partes[1]
    operacoes_validas = ['+', '-', '/', '*']
    for op in operacoes_validas:
        valores = espressao.split(op)
        if len(valores) > 1:
            operador = op
            break 
    valores = [v.strip() for v in valores]
    valore = partes[0].strip()    
    # decidir q operação sera feita
    if eh_incognita(valore):
        res = valores[0] op-valores[1]
        A = float(valores[0])
        B = float(valores[1])
       # trocar
        op 
    elif eh_incognita(valores[0]):
        A = float(valore)
        B = float(valores[1])
        op = operacoes_opostas[op] 
    elif eh_incognita(valores[1]):
        if op == '/' or op == '-':
            A = float(valores[0])
            B = float(valore)
        else: 
            op = operacoes_opostas[op]
            A = float(valore)
            B = float(valores[0])

        # retornar o valor
    if op == "+":
        return A + B
    elif op == "-":
        return A - B
    elif op == "*":
        return A * B
    else:
        return A / B

if __name__ == "__main__":
    print(operar("8 = 4 + t")) 