#Gfhdthev
#Лабораторная работа номер 5, вариант 11


#импорт библиотек
import os
import pandas as pd


class Exception:
    #инициализация объектов
    def __init__(self, file, columns):
        self.file = file
        self.columns = columns

    def processing(self):
        try:
            #проверяем наличия файла
            if not os.path.exists(self.file):
                raise FileNotFoundError(f"Файл '{self.file}' не найден в указанной директории.")

            df = pd.read_csv(self.file)

            #проверяем структуры данных
            if not all(col in df.columns for col in self.columns):
                missing_columns = [col for col in self.columns if col not in df.columns] #выписываем недостоющие столбцы
                raise ValueError(f"Несоответствие структуры данных. Отсутствуют столбцы: {missing_columns}")

            #проверяем на пустой датасет
            if df.empty:
                raise ValueError("Датасет пуст.")

            print("Датасет успешно загружен и соответствует ожидаемой структуре.")
            return df

        #выписываем остальные ошибки
        except FileNotFoundError as e:
            print(f"Ошибка: {e}")
        except pd.errors.ParserError:
            print("Ошибка. Проверьте формат файла.")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")