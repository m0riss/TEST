import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Assuming you have a DataFrame named 'df' containing your data
# Replace 'df' with the actual variable name you are using.

# Sample DataFrame for testing
data = {
    'StartDate': ['2023-01-01', '2023-02-01', '2023-03-01'],
    'Duration': [10, 15, 12],
}

df = pd.DataFrame(data)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Simple Dash Application"),
    dcc.Graph(id='scatter-plot'),
    dcc.Slider(
        id='duration-slider',
        min=df['Duration'].min(),
        max=df['Duration'].max(),
        step=1,
        value=df['Duration'].min(),
        marks={i: str(i) for i in range(df['Duration'].min(), df['Duration'].max() + 1)}
    ),
])


@app.callback(
    Output('scatter-plot', 'figure'),
    Input('duration-slider', 'value')
)
def update_graph(selected_duration):
    filtered_df = df[df['Duration'] == selected_duration]

    fig = px.scatter(filtered_df, x='StartDate', y='Duration', title='Scatter Plot')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
