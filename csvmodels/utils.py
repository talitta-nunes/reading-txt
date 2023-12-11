def convert_string_to_number(input_string):
    try:
        numeric_value = int(input_string)

        formatted_value = float(numeric_value) / 1000

        return formatted_value
    except ValueError:
        print("Error: Input is not a valid integer.")
        return None
    
def normalize_type(t):
    if t =="1":
        return "Débito"
    elif t=="2":
        return "Boleto"
    elif t =="3":
        return "Financiamento"
    elif t=="4":
        return "Crédito"
    elif t =="5":
        return "Recebimento Empréstimo"
    elif t=="6":
        return "Vendas"
    elif t=="7":
        return "Recebimento TED"
    elif t =="8":
        return "Recebimento DOC"
    elif t=="9":
        return "Aluguel"
    else:
        None
