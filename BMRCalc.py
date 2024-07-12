def BmrCalc(unit, weight, height, age, gender):
        if unit == 'metric':
            if gender == 'male':
                bmr_result = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
            else:
                bmr_result = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        else:
            weight_kg = weight * 0.453592
            height_cm = height * 2.54
            if gender == 'male':
                bmr_result = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
            else:
                bmr_result = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
        
        return bmr_result