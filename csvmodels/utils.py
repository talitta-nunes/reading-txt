def convert_string_to_number(input_string):
    try:
        numeric_value = int(input_string)

        formatted_value = float(numeric_value) / 1000

        return formatted_value
    except ValueError:
        print("Error: Input is not a valid integer.")
        return None
    
def normalize_desc(t):
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


def normalize_nature(t):
    if t =="1":
        return "Entrada"
    elif t=="2":
        return "Saída"
    elif t =="3":
        return "Saída"
    elif t=="4":
        return "Entrada"
    elif t =="5":
        return "Entrada"
    elif t=="6":
        return "Entrada"
    elif t=="7":
        return "Entrada"
    elif t =="8":
        return "Entrada"
    elif t=="9":
        return "Saída"
    else:
        None


def normalize_signal(t):
    if t =="1":
        return "+"
    elif t=="2":
        return "-"
    elif t =="3":
        return "-"
    elif t=="4":
        return "+"
    elif t =="5":
        return "+"
    elif t=="6":
        return "+"
    elif t=="7":
        return "+"
    elif t =="8":
        return "+"
    elif t=="9":
        return "-"
    else:
        None


