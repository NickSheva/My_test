import pandas as pd
pd.options.plotting.backend = 'plotly'
df = pd.DataFrame(dict(a =[1,3,2], b=[3,2,1]))
fig1 = df.plot.bar()
fig1.show()

# using Plotly Express directly
import plotly.express as px
fig2 = px.bar(df)
fig2.show()