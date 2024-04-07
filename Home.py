import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 
from functions import *
import numpy as np
from PIL import Image
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

st.set_page_config(page_title="Home", page_icon="🗿")

st.title('Проект по курсу "Старт в DataScience"')
st.write('Здесь я привел небольшой и не особо умелый анализ российской экономики в период с 2000 года по 2023')
st.error("Пока это делал расстроился")

image = Image.open('data/stonks.jpeg')
st.image(image)

st.subheader('А зачем вообще нам о них знать?')
st.markdown("""
### 1. Оценка покупательной способности:

* Реальная ЗП показывает, сколько товаров и услуг человек может купить на свою ЗП, учитывая инфляцию.
            
* Сравнивая реальную ЗП с прошлыми периодами, можно оценить, насколько изменился уровень жизни.

### 2. Мониторинг экономической ситуации:

* Рост реальной ЗП говорит о росте благосостояния населения и экономики.
* Снижение реальной ЗП может сигнализировать о проблемах в экономике, например, о стагнации или спаде.

### 3. Помощь в принятии решений:

Значение реальной ЗП может помочь людям:
* При принятии решений о работе: сравнить предложения о работе с учетом инфляции.
* При ведении переговоров о ЗП: обосновать желаемый уровень ЗП с учетом инфляции.
* При планировании расходов: оценить, насколько хватит ЗП с учетом инфляции.
""")