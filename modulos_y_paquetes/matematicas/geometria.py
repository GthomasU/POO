import math

def calcular_area_circulo(radio: float)-> float:
    return math.pow(radio,2 )*math.pi

def calcular_area_rectangulo(lado1: float, lado2: float)-> float:
    return lado1*lado2

def calcular_area_cuadrado(lado: float)-> float:
    return math.pow(lado,2)  
