# Calcular IMC
# IMC = Peso ÷ (Altura × Altura)
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# Entre 25 até 30: Sobrepeso
# Entre 30 até 40: Obsidade
# Acima de 40: Obsidade mórbida

# vars
peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual é a sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é: {:.2f}. Você está abaixo do peso!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é: {:.2f}. Você está no peso ideal!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é: {:.2f}. Você está com sobrepeso!'.format(imc))
elif 30 <= imc <= 40:
    print('Seu IMC é: {:.2f}. Você está obeso!'.format(imc))
elif imc > 40:
    print('Seu IMC é: {:.2f}. Você está com obesidade mórbida!'.format(imc))
else:
    print('Seu IMC é: {:.2f}. Valor não identificado!'.format(imc))