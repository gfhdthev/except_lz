#Gfhdthev
#Лабораторная работа номер 5, вариант 11


#импорт библиотек
import os
import pandas as pd



import os
import pandas as pd

class Exceptions:
    def __init__(self, file, columns, types):
        self.file = file
        self.columns = columns    # список обязательных столбцов
        self.types = types        # словарь с ожидаемыми типами для каждого столбца

    def processing(self):
        try:
            # Проверяем наличие файла
            if not os.path.exists(self.file):
                raise FileNotFoundError(f"Файл '{self.file}' не найден в указанной директории.")

            # Чтение CSV с использованием параметра low_memory=False для корректного определения типов
            df = pd.read_csv(self.file, low_memory=False)

            # Проверяем наличие всех обязательных столбцов
            missing_columns = [col for col in self.columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Несоответствие структуры данных. Отсутствуют столбцы: {missing_columns}")

            # Проверяем, что датасет не пустой
            if df.empty:
                raise ValueError("Датасет пуст.")

            # Проверка типа данных для каждого столбца, согласно file_types
            for col, expected_type in self.types.items():
                actual_type = str(df[col].dtype)
                if actual_type != expected_type:
                    raise TypeError(
                        f"Ошибка: Столбец '{col}' — ожидался {expected_type}, получен {actual_type}"
                    )

            print("Датасет успешно загружен и соответствует ожидаемой структуре.")
            return df

        except FileNotFoundError as e:
            print(f"Ошибка: {e}")
        except pd.errors.ParserError:
            print("Ошибка. Проверьте формат файла.")
