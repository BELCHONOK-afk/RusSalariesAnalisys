import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 
from functions import *
import numpy as np

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

st.set_page_config(page_title="Анализ ВВП", page_icon="🤡")

GDPs = load_excel_data('data/Rosstat National Accounts 1995.xlsx')
years = np.arange(2000, 2024, 1)

GDP = pd.DataFrame(GDPs['1'])
GDP = pd.concat([GDP, pd.DataFrame(GDPs['2']).drop(columns=2011)], axis=1)
GDP = GDP.iloc[:, 5:]

deflation = pd.DataFrame(GDPs['9'])
deflation = pd.concat([deflation, pd.DataFrame(GDPs['10'])], axis=1)
deflation = deflation.iloc[:,4:]

real_GDP = GDP*100/deflation


st.title("Анализ ВВП в России в период с 2000 по 2023 годы")
st.text("Представляю анализ ВВП России с учетом дефлятора")

#from PIL import Image
#image = Image.open("data/money.jpeg")
#st.image(image)

st.sidebar.title('About')

radio = st.sidebar.radio('Вывести график', 
    options=['Номинальный ВВП',
             'Реальный ВВП',
             'Реальный VS Номинальный ВВП', 
             'Разность между рельным и номинальным ВВП'])

if radio == 'Номинальный ВВП':
    values = GDP.values.flatten()
    title = 'Номинальный ВВП в период с 2000 по 2023 год'
    ylabel = 'млрд. рублей'
    fig = plot_xy(values, years, title, ylabel=ylabel, xlabel= None )
    st.pyplot(fig)
    st.info('Можно наблюдать рост номинального ВВП, но это мало о чем говорит')
elif radio == 'Реальный ВВП':
    values = real_GDP.values.flatten()
    title = 'Реальный ВВП в период с 2000 по 2023 год'
    ylabel = 'млрд. рублей'
    fig = plot_xy(values, years, title, ylabel=ylabel, xlabel= None )
    st.pyplot(fig)
    st.info('Реальный ВВП тоже растет, что говорит об улучшении экономики России') 
elif radio == 'Реальный VS Номинальный ВВП':
    title = 'Сравнение реального и номинального ВВП'
    ylabel =  'млрд. рублей'
    label_1 = 'Номинальный ВВП'
    label_2 = 'Реальный ВВП'
    fig = plot_2graphs(years, 
                 GDP.values.flatten(), 
                 real_GDP.values.flatten(),
                 title,
                 xlabel= None, 
                 ylabel= ylabel, 
                 label_1 = label_1,
                 label_2= label_2)
    st.pyplot(fig)
    st.info('Сравнивая два графика, мы видим лишь то, что дефляция все-таки есть (куда без нее)')

elif radio == 'Разность между рельным и номинальным ВВП':
    values = ((1 - real_GDP.values.flatten() / GDP.values.flatten()) * 100)
    title= 'Разница между номинальным и реальным ВВП'
    fig = bar_plot(years, values, title, ylabel= '%', xlabel=None)
    st.pyplot(fig)
    st.info('Разница довольно сильная, сложно спрогнозировать будущее')
    