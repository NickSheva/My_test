import plotly.figure_factory as ff
import pandas as pd
# Стандартное импортирование plotly
import plotly  as pl
import plotly.graph_objs as go
from plotly.offline import iplot

# Использование cufflinks в офлайн-режиме
import cufflinks
cufflinks.go_offline()


figure = ff.create_scatterplotmatrix(
    df[['claps', 'publication', 'views',
        'read_ratio','word_count']],
    diag='histogram',
    index='publication')