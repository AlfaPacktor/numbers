import streamlit as st
import pandas as pd
import os

FILE_NAME = "data.csv"

st.title("Ввод данных клиентов")

# Создание файла если его нет
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["ФИО", "Номер счета"])
    df.to_csv(FILE_NAME, index=False)

# Поля ввода
name = st.text_input("ФИО")
account = st.text_input("№ счета")

# Кнопка ввода
if st.button("Ввести"):
    if name and account:
        df = pd.read_csv(FILE_NAME)
        new_row = pd.DataFrame([[name, account]], columns=["ФИО", "Номер счета"])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(FILE_NAME, index=False)
        st.success("Данные добавлены")
    else:
        st.error("Введите ФИО и номер")

# Показ таблицы
st.subheader("Таблица данных")
df = pd.read_csv(FILE_NAME)
st.dataframe(df)

# Скачать Excel
excel_file = "data.xlsx"
df.to_excel(excel_file, index=False)

with open(excel_file, "rb") as file:
    st.download_button(
        label="Скачать Excel",
        data=file,
        file_name="clients.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Кнопка сброса
if st.button("Сбросить"):
    df = pd.DataFrame(columns=["ФИО", "Номер счета"])
    df.to_csv(FILE_NAME, index=False)
    st.warning("Таблица очищена")
