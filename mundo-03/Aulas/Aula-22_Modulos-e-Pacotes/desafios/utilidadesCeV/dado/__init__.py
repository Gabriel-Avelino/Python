def leiadinheiro(msg):
    while True:
        value = str(input(msg))
        value_cleaned = value.replace(",", "").replace(".", "")
        if value_cleaned.isdigit():
            if ',' in value:
                value = value.replace(',', '.')
            value = float(value)
            return value
        else:
            print(f'\033[31mERRO:\"{value}\" é um preço inválido!\033[m')
