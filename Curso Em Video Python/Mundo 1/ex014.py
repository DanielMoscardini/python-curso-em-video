"""
Faça um software que converta a temperatura digitada em Cº para Fº
Nota: °C = (°F − 32) ÷ 1, 8
"""
Celsius = float(input('Digite a temperatura: '))
Fahrenheit = 1.8 * Celsius + 32
print(f'Temperatura em: \nCelsius: {Celsius} \nFahrenheit: {Fahrenheit:.2f}')