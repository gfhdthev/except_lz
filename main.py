from files import Exceptions

def main():
    # Столбцы, которые должны быть в файле
    file_columns = [
        "Участники гражданского оборота",
        "Тип операции",
        "Сумма операции",
        "Вид расчета",
        "Место оплаты",
        "Терминал оплаты",
        "Дата оплаты",
        "Время оплаты",
        "Результат операции",
        "Cash-back",
        "Сумма cash-back"
    ]

    # Ожидаемые типы данных для каждого столбца
    file_types = {
        "Участники гражданского оборота": "object", 
        "Тип операции": "object", 
        "Сумма операции": "float64", 
        "Вид расчета": "object", 
        "Место оплаты": "object", 
        "Терминал оплаты": "object", 
        "Дата оплаты": "object", 
        "Время оплаты": "object",
        "Результат операции": "object",
        "Cash-back": "object",
        "Сумма cash-back": "float64"
    }

    # Файл с данными
    file_name = "var11.csv"

    processor = Exceptions(file_name, file_columns, file_types)
    try:
        processor.processing()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
