# Стандартное импортирование plotly
import plotly.plotly as pl
import plotly.graph_objs as go
from plotly.offline import iplot

# Использование cufflinks в офлайн-режиме
import cufflinks
cufflinks.go_offline()

# Настройка глобальной темы cufflinks
cufflinks.set_config_file(world_readable=True, theme='pearl', offline=True)

# При помощи plotly легко сделать интерактивное представление гистограмм и прочих распределений.
# Для тех, кто использовал ранее matplotlib, нужно вместо команды plot просто использовать iplot:
df['claps'].iplot(kind='hist', xTitle='claps',
                  yTitle='count', title='Claps Distribution')

# Если мы хотим сравнить распределение двух переменных, можем наложить две гистограммы друг на друга:
df[['time_started', 'time_published']].iplot(
    kind='hist',
    histnorm='percent',
    barmode='overlay',
    xTitle='Time of Day',
    yTitle='(%) of Articles',
    title='Time Started and Time Published')