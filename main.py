from files import Exception

def main():

        # Ожидаемые столбцы из вашего датасета
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

    # Путь к файлу
    file_name = "var11.csv"

    # Создание экземпляра класса и обработка датасета

    processor = Exception(file_name, file_columns)  
    processor.processing()  

if __name__ == "__main__":
    main() 