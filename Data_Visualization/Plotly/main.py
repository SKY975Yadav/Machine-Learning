import plotly.express as px

# Sample data
df = px.data.iris()
df
# # Create scatter plot
# fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title='Sepal Width vs Sepal Length')


fig = px.scatter(df, x='sepal_width', y='sepal_length', size='sepal_length')
fig.show()