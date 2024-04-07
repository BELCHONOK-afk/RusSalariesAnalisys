import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 
from functions import *
import numpy as np
"""
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.set_style({'axes.facecolor':'23606E',
               'figure.facecolor': '23606E', 
               'axes.labelcolor': 'F5F5F5',
               'axes.axisbelow': True,
               'axes.edgecolor': '327E8F',
               'text.color':'F5F5F5',
               'xtick.color': 'F5F5F5',
              'ytick.color': 'F5F5F5',
              'grid.color': '327E8F'})
#sns.set_facecolor("#23606E")

"""
st.set_page_config(page_title="Анализ зарплат", page_icon="💀")


url = "https://xn----ctbjnaatncev9av3a8f8b.xn--p1ai/%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D1%8B-%D0%B8%D0%BD%D1%84%D0%BB%D1%8F%D1%86%D0%B8%D0%B8"

#load all datas
salaries =  load_excel_data('data/Rosstat Labor Market 2023.xlsx')
inflation = load_html_data(url)
inflation = inflation[['Год','Всего']][:26] #from 1999
areas = ['Рыболовство, рыбоводство', 'Строительство', 'Добыча полезных ископаемых','Гостиницы и рестораны','Образование','Здравоохранение и предоставление социальных услуг']
years = np.arange(2000, 2024, 1)

salary_df_1 = pd.DataFrame(salaries['sheet1'])# до 2016
salary_df_2 = pd.DataFrame(salaries['sheet2'])# c 2017
salary_df_1 = salary_df_1.rename(columns={'год':'Area'})
salary_df_2 = salary_df_2.rename(columns={'год':'Area'})
interested_areas = choose_areas_and_concat(salary_df_1, salary_df_2, areas)

del salary_df_1
del salary_df_2


st.title("Анализ зарплат в России в период с 2000 по 2023 годы")
st.text("Представляю анализ реальных зарплат в России с учетом инфляции")


st.sidebar.title('About')

area = st.sidebar.selectbox("Сферы деятельности", areas)
radio = st.sidebar.radio('Вывести график', 
    options=['Номинальная зарплата','Реальная зарплата VS Номинальная','Инфляция', 'Разность в зарплатах'])

if radio == 'Номинальная зарплата':
    values = interested_areas[interested_areas['Area']==area].values[0][1:]
    title=f'Номинальная зарплата в сфере {area}'
    ylabel='рублей'
    xlabel = None
    fig = plot_xy(values, years, title=title, ylabel= ylabel, xlabel=xlabel)
    st.pyplot(fig)
    st.info("""
            Из данных графиков можно сделать вывод о том, что ежегодно зарплаты в данных сферах растут.
            Причной может быть выход страны на мировой рынок.
            Также в среднем уровень жизни в стране с 2000-го года поднялся, из чего может следовать рост спроса и внутри страны тоже.
            Также не стоит забывать о нескольких пережитых кризисах. Рост зарплат может быть связан с инфляцией. Поскольку уровень инфляции увеличивает цены на товары и услуги, работники могут требовать повышения зарплаты, чтобы компенсировать ухудшение покупательной способности своих доходов.                       
            """)

elif radio == 'Реальная зарплата VS Номинальная':
    nominal_wage = interested_areas[interested_areas['Area']==area].values[0][1:]
    real_wage = real_wage(interested_areas,years,area,inflation)
    title= f"Зарплата в сфере {area} с учетом инфляции по отношению к прошлому году"
    ylabel= 'рублей'
    xlabel=None
    real_label = "Реальная зарплата"
    nominal_label = "Номинальная зарплата"
    fig = plot_2graphs(years, nominal_wage, real_wage, title, xlabel, ylabel,label_2=real_label, label_1=nominal_label)
    st.pyplot(fig, use_container_width=True)
    st.info("""
Из графиков выше можно сделать несколько выводов:

Номинальная зарплата росла весь период
Реальная зарплата росла весь период, но инфляция давала о себе знать, и рост номинальной зарплаты не сглаживает роста инфляции
В период 2014-2015 годов, реальная зарплата в сфере "Строительство" снизилась. Причиной могло стать наложение санкций и следующее за ними снижение покупательской способности
Покупательская способность падает, как результат расхождения реальной и номинальной зарплаты
Причинами могут быть:

Глобальный мировой кризис
Снижение цен на сырье
Рост инфляции
            """)


elif radio == 'Инфляция':
    values= [val for val in inflation['Всего'][::-1]]
    title= "Значение инфляции"
    ylabel= "%"
    fig = plot_xy(values[1:25],years, title= title, ylabel=ylabel, xlabel=None)
    st.pyplot(fig)
    st.info("""Наблюдается рост инфляции. Она растет скачкообразно, что негативно сказывается на экономике,
            так как довольно сложно сгладить ее""")

elif radio == 'Разность в зарплатах':
    nominal_wage = interested_areas[interested_areas['Area']==area].values[0][1:]
    real_wage = real_wage(interested_areas,years,area,inflation)
    values = (1-real_wage/nominal_wage)*100
    title= f'Разница между реальной и номинальной заработной платой в сфере: {area}'
    ylabel="%"
    fig = bar_plot(years, values,title,ylabel, xlabel=None )
    st.pyplot(fig)
    st.info("""Из графиков выше мы видим, что в период с 2000 по 2018 разница между реальной и номинальной заработной платой уменьшалась с некоторыми выбросами, обусловленными частными экономическими проблемами, что говорит о том, что страна развивалась и был реальный рост доходов.

Начиная с 2019 года, рост доходов прекратился.""")

