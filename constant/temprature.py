from scipy.constants import convert_temperature

if __name__ == '__main__':
    temperature_in_fareninte = 106
    convert_temp_in_c = convert_temperature(temperature_in_fareninte, 'F', 'C')
    print(convert_temp_in_c)
