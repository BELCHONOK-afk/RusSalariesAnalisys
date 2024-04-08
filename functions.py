import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

"""
Этот файл содержит все функции, которые будут испольльзоваться в проекте
"""

@st.cache_data
def load_html_data(url, num_table= 0):
    """
    Функция, которая возвращает датафрейм, хранящийся по HTML адресу

    Parameters:
        url - html adress
        num_table - number of table keeping in web_page

    Return:
        pd.DataFrame
    """
    df = pd.read_html(url)
    return pd.DataFrame(df[num_table])


@st.cache_data
def load_excel_data(path):
    """
    Загрузка данных из Excel файла с выбором всех страниц в документе

    """
    return pd.read_excel(path, sheet_name=None, skiprows=2)# выбрали все страницы в документе
    
    
def choose_areas_and_concat(df_1, df_2, areas):
    df_1 = df_1[df_1['Area'].isin(areas)].copy().reset_index(drop = True)
    df_2 = df_2[df_2['Area'].isin(areas)].copy().reset_index(drop = True)

    return pd.concat([df_1, df_2.drop(columns=['Area'])], axis=1)


def real_wage(df,years,area,inflation):
    nominal_wage = df[df['Area']==area]
    real_wage = []
    for year in years:
        salary = nominal_wage[year].values[0]
        prev_infl = inflation[inflation['Год']==year-1].values[0][1]
        recalc_salary = salary/(1+(prev_infl*0.01))
        real_wage.append(recalc_salary)
    return real_wage


def plot_xy(values, years, title, ylabel, xlabel):
    """
    Функция строит линейный график зависимости с сеткой

    """
    fig, ax = plt.subplots()
    fig.set_size_inches(10,5)
    sns.lineplot(x= years, y= values, color= '#FACFCE', ax=ax)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(years,rotation = 'vertical')
    plt.grid(True)
    return fig


def bar_plot(years, values, title, ylabel, xlabel):
    """
    Функция строит столбчатую диаграмму, с надписями значений над столбцами

    """
    fig, ax = plt.subplots()
    fig.set_size_inches(15,7)
    sns.barplot(x=years, y=values, color= '#99C274', ax=ax)
    # Добавление значений над столбцами
    for i, value in enumerate(values):
        plt.text(i, value, f'{value:.2f}%', ha='center', va='bottom')

    # Дополнительные настройки
    plt.grid(axis= 'y')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=90)
    return fig

def plot_2graphs(years, values_1, values_2, title, xlabel, ylabel, label_1, label_2):
    fig, ax= plt.subplots()
    sns.lineplot(x= years, y= values_1, label= label_1, color= '#40E0D0', marker= 'o', ax= ax)
    sns.lineplot(x= years, y= values_2, label= label_2, color='#FFC0CB', marker= 'o',ax=ax)
    plt.title(title)
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(years, rotation= 'vertical')
    plt.grid(True)
    return fig


def show_df(df_1, subhed_1,df_2, subhead_2):
    st.subheader(subhed_1)
    st.dataframe(df_1)
    st.subheader(subhead_2)
    st.dataframe(df_2)
    return None

