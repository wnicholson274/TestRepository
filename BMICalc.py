def BmiCalc(weight, height, unit):
    if unit == 'metric':
        bmi_result = weight / (height / 100) ** 2

    else:
        bmi_result = (weight / height ** 2) * 703
    
    return bmi_result

