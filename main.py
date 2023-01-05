
def es_año_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

print(es_año_bisiesto(2020))
print(es_año_bisiesto(2022))