from files import Exception

def main():

        #столбцы, которые должны быть в файле
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

    #файл
    file_name = "var11.csv"
    
    processor = Exception(file_name, file_columns)  
    processor.processing()  

if __name__ == "__main__":
    main() 