def interactive_eda(data):

    """The function interactive_eda(data) is used to create a 
        Exploratory Data Analysis using plotly with the local server
        using Dash library. It consist of basic EDA process as html page.
        
        We can now focus most on data not on code.
        
        The function interactive_eda(data) takes one argument,
        which can be a pandas dataframe.
        
        E.G -->  interactive_eda(data=data_frame)"""
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly.express as px
    import plotly.graph_objects as go
    import dash
    from dash import html, dcc, Input, Output
    import warnings
    warnings.filterwarnings('ignore')
    
    if type(data) == pd.core.frame.DataFrame:
        continuous_data = list(data.select_dtypes(exclude=['object', 'category']))
        category_data = list(data.select_dtypes(include=['object', 'category']))
        
        if len(continuous_data) > 0 and len(category_data) > 0:
            entire_eda(data = data, continuous_data=continuous_data, category_data=category_data)
        
        elif len(continuous_data) > 0 and len(category_data) == 0:
            continuous_eda(data = data, continuous_data=continuous_data)
            
        elif len(category_data) > 0 and len(continuous_data) == 0:
            categorical_eda(data = data, category_data = category_data)
        
        
    else:
        print("Please provide the pandas dataframe.")

def entire_eda(data, continuous_data, category_data):
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly.express as px
    import plotly.graph_objects as go
    import dash
    from dash import html, dcc, Input, Output
    import warnings
    warnings.filterwarnings('ignore')
    
    app = dash.Dash(__name__)
    app.layout = html.Div([
    
        html.Div([html.H1('Exploratory Data Analysis')],
                 style = {
                     'text-align':'center',
                     'font-size':'20px',
                     'color':'blue',
                 }),
    
        html.Br(),
    
        html.Div([html.H3('Univariate continuous data analysis')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
    
        html.P('Select a column name for analysis'),
    
        html.Div([dcc.Dropdown(
            id='first_dropdown',
            placeholder='Select a column name for analysis',
            options=[
                {'label': i, 'value' : i}
                for i in continuous_data
            ]),
        
        html.Br(),
                  
        html.P('Select a plot type for visualization'),
                  
        dcc.Dropdown(
            id='second_dropdown',
            placeholder='Select a plot type',
            options=[{'label':'histogram', 'value':'histogram'}, {'label':'box', 'value':'box'},
                     {'label':'violin', 'value':'violin'}, {'label':'strip', 'value':'strip'},
                     {'label':'scatter', 'value':'scatter'}],
            value='histogram'
        ),
    
        dcc.Graph(id='first_output')]),
    
        html.Br(),
    
        html.Div([html.H3('Univariate Category data analysis')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
    
        html.P('Select a column name for analysis'),
    
        html.Div([dcc.Dropdown(
            id='third_dropdown',
            placeholder='Select a column name for analysis',
            options=[
                {'label': i, 'value' : i}
                for i in category_data
            ]),
        
        html.Br(),
                  
        html.P('Select a plot type for visualization'),
                  
        dcc.Dropdown(
            id='fourth_dropdown',
            placeholder='Select a plot type',
            options=[{'label':'bar', 'value':'bar'}],
            value='bar'
        ),
    
        dcc.Graph(id='second_output')]),
    
    
        html.Br(),
    
        html.Div([html.H3('Univariate data analysis')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
    
        html.P('Select a continuous column name for analysis'),
    
        html.Div([dcc.Dropdown(
            id='fifth_dropdown',
            placeholder='Select a column name for analysis',
            options=[
                {'label': i, 'value' : i}
                for i in continuous_data
            ]),
        
        html.Br(),
                  
        html.P('Select a category column name for analysis'),
                  
        dcc.Dropdown(
            id='sixth_dropdown',
            placeholder='Select a column name for analysis',
            options=[{'label': i, 'value': i}
                    for i in category_data]),
                  
        html.Br(),
                  
        html.P('Select a plot type for visualization'),
                  
        dcc.Dropdown(
            id='seventh_dropdown',
            placeholder='Select a plot to visualize',
            options=[{'label': 'pie', 'value': 'pie'}, {'label': 'scatter', 'value': 'scatter'},
                    {'label': 'box', 'value': 'box'}, {'label':'strip', 'value':'strip'}],
            value='pie'),
    
        dcc.Graph(id='third_output')]),
    
        html.Br(),
    
        html.Div([html.H3('Bivariate continuous data analysis')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
    
        html.P('Select a continuous column name for analysis'),
    
        html.Div([dcc.Dropdown(
            id='eighth_dropdown',
            placeholder='Select a column name for analysis',
            options=[
                {'label': i, 'value' : i}
                for i in continuous_data
            ]),
        
        html.Br(),
                  
        html.P('Select a continuous column name for analysis'),
                  
        dcc.Dropdown(
            id='nineth_dropdown',
            placeholder='Select a column name for analysis',
            options=[{'label': i, 'value': i}
                    for i in continuous_data]),
                  
        html.Br(),
                  
        html.P('Select a plot type for visualization'),
                  
        dcc.Dropdown(
            id='tenth_dropdown',
            placeholder='Select a plot to visualize',
            options=[{'label': 'line', 'value': 'line'}, {'label': 'scatter', 'value': 'scatter'}],
            value='scatter'),
    
        dcc.Graph(id='fourth_output')]),
    
        html.Br(),
    
        html.Div([html.H3('Bivariate categorical data analysis')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
    
        html.P('Select a categorical column name for analysis'),
    
        html.Div([dcc.Dropdown(
            id='eleventh_dropdown',
            placeholder='Select a column name for analysis',
            options=[
                {'label': i, 'value' : i}
                for i in category_data
            ]),
        
        html.Br(),
                  
        html.P('Select a categorical column name for analysis'),
                  
        dcc.Dropdown(
            id='twelvefth_dropdown',
            placeholder='Select a column name for analysis',
            options=[{'label': i, 'value': i}
                    for i in category_data]),
                  
        html.Br(),
    
        dcc.Graph(id='fifth_output')]),
    
        html.Br(),
    
        html.Div([html.H3('Bivariate data analysis')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
    
        html.P('Select a continuous column name for analysis'),
    
        html.Div([dcc.Dropdown(
            id='thirteenth_dropdown',
            placeholder='Select a column name for analysis',
            options=[
                {'label': i, 'value' : i}
                for i in continuous_data
            ]),
        
        html.Br(),
                  
        html.P('Select a continuous column name for analysis'),
                  
        dcc.Dropdown(
            id='fourteenth_dropdown',
            placeholder='Select a column name for analysis',
            options=[{'label': i, 'value': i}
                    for i in continuous_data]),
                  
        html.Br(),
                  
        html.P('Select a Category column name for analysis'),
                  
        dcc.Dropdown(
            id='fifteenth_dropdown',
            placeholder='Select a column name for analysis',
            options=[{'label': i, 'value': i}
                    for i in category_data]),
                  
        html.Br(),
                  
        html.P('Select a plot type for visualization'),
                  
        dcc.Dropdown(
            id='sixteenth_dropdown',
            placeholder='Select a plot to visualize',
            options=[{'label': 'line', 'value': 'line'}, {'label': 'scatter', 'value': 'scatter'}],
            value='scatter'),
            dcc.Graph('sixth_output')
        ]),
        
        html.Br(),
        
        html.Div([html.H3('Heatmap')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
        
        dcc.Graph(figure=go.Figure(go.Heatmap(x=continuous_data, y=continuous_data, z=data[continuous_data].corr())))   
        
    ])


    @app.callback(Output('first_output', 'figure'), [Input('first_dropdown', 'value'), Input('second_dropdown', 'value')])

    def univariate_continuous_analysis(input_first_dropdown, input_second_dropdown):
        if len(continuous_data) > 0:
            if input_second_dropdown == 'histogram':
                fig = px.histogram(data[input_first_dropdown])
                return fig
            elif input_second_dropdown == 'box':
                fig = px.box(data[input_first_dropdown])
                return fig
            elif input_second_dropdown == 'violin':
                fig = px.violin(data[input_first_dropdown])
                return fig
            elif input_second_dropdown == 'strip':
                fig = px.strip(data[input_first_dropdown])
                return fig
            elif input_second_dropdown == 'scatter':
                fig = px.scatter(x=data.index, y=data[input_first_dropdown])
                return fig
        
    @app.callback(Output('second_output', 'figure'), [Input('third_dropdown', 'value'), Input('fourth_dropdown', 'value')])

    def univariate_category_analysis(input_third_dropdown, input_fourth_dropdown):
        if len(category_data) > 0:
            if input_fourth_dropdown == 'bar':
                fig = px.bar(data[input_third_dropdown])
                return fig

    @app.callback(Output('third_output', 'figure'), [Input('fifth_dropdown', 'value'), Input('sixth_dropdown', 'value'), Input('seventh_dropdown', 'value')])

    def univariate_analysis(input_fifth_dropdown, input_sixth_dropdown, input_seventh_dropdown):
        if len(continuous_data) > 0 and len(category_data) > 0:
            if input_seventh_dropdown == 'pie':
                fig = px.pie(values=data[input_fifth_dropdown], names=data[input_sixth_dropdown])
                return fig
            elif input_seventh_dropdown == 'scatter':
                fig = px.scatter(x=data.index, y=data[input_fifth_dropdown], color=data[input_sixth_dropdown])
                return fig
            elif input_seventh_dropdown == 'box':
                fig = px.box(x=data[input_fifth_dropdown], color=data[input_sixth_dropdown])
                return fig
            elif input_seventh_dropdown == 'strip':
                fig = px.strip(x=data[input_fifth_dropdown], color=data[input_sixth_dropdown])
                return fig

    @app.callback(Output('fourth_output', 'figure'), [Input('eighth_dropdown', 'value'), Input('nineth_dropdown', 'value'), Input('tenth_dropdown', 'value')])

    def bivariate_continuous_analysis(input_eighth_dropdown, input_nineth_dropdown, input_tenth_dropdown):
        if len(continuous_data) > 0:
            if input_tenth_dropdown == 'line':
                fig = px.line(x=data[input_eighth_dropdown], y=data[input_nineth_dropdown])
                return fig
            elif input_tenth_dropdown == 'scatter':
                fig = px.scatter(x=data[input_eighth_dropdown], y=data[input_nineth_dropdown])
                return fig

    @app.callback(Output('fifth_output', 'figure'), [Input('eleventh_dropdown', 'value'), Input('twelvefth_dropdown', 'value')])

    def bivariate_categorical_analysis(input_eleventh_dropdown, input_twelvefth_dropdown):
        if len(category_data) > 0:
            mat = pd.crosstab(data[input_eleventh_dropdown], data[input_twelvefth_dropdown])
            fig = go.Figure(go.Heatmap(x=mat.columns, y=mat.index, z=mat))
            return fig

    @app.callback(Output('sixth_output', 'figure'), [Input('thirteenth_dropdown', 'value'), Input('fourteenth_dropdown', 'value'), Input('fifteenth_dropdown', 'value'), Input('sixteenth_dropdown', 'value')])

    def bivariate_analysis(input_thirteenth_dropdown, input_fourteenth_dropdown, input_fifteenth_dropdown, input_sixteenth_dropdown):
         if len(continuous_data) > 0 and len(category_data) > 0:
            if input_sixteenth_dropdown == 'line':
                fig = px.line(x=data[input_thirteenth_dropdown], y=data[input_fourteenth_dropdown], color=data[input_fifteenth_dropdown])
                return fig
            elif input_sixteenth_dropdown == 'scatter':
                fig = px.scatter(x=data[input_thirteenth_dropdown], y=data[input_fourteenth_dropdown], color=data[input_fifteenth_dropdown])
                return fig
            
    if __name__ == '__main__':
        app.run(port=4000)

def continuous_eda(data, continuous_data):
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly.express as px
    import plotly.graph_objects as go
    import dash
    from dash import html, dcc, Input, Output
    import warnings
    warnings.filterwarnings('ignore')
    
    app = dash.Dash(__name__)
    app.layout = html.Div([
    
        html.Div([html.H1('Exploratory Data Analysis')],
                 style = {
                     'text-align':'center',
                     'font-size':'20px',
                     'color':'blue',
                 }),
    
        html.Br(),
    
        html.Div([html.H3('Univariate continuous data analysis')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
    
        html.P('Select a column name for analysis'),
    
        html.Div([dcc.Dropdown(
            id='first_dropdown',
            placeholder='Select a column name for analysis',
            options=[
                {'label': i, 'value' : i}
                for i in continuous_data
            ]),
        
        html.Br(),
                  
        html.P('Select a plot type for visualization'),
                  
        dcc.Dropdown(
            id='second_dropdown',
            placeholder='Select a plot type',
            options=[{'label':'histogram', 'value':'histogram'}, {'label':'box', 'value':'box'},
                     {'label':'violin', 'value':'violin'}, {'label':'strip', 'value':'strip'},
                     {'label':'scatter', 'value':'scatter'}],
            value='histogram'
        ),
    
        dcc.Graph(id='first_output')]),
    
        html.Br(), 
    
        html.Div([html.H3('Bivariate continuous data analysis')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
    
        html.P('Select a continuous column name for analysis'),
    
        html.Div([dcc.Dropdown(
            id='eighth_dropdown',
            placeholder='Select a column name for analysis',
            options=[
                {'label': i, 'value' : i}
                for i in continuous_data
            ]),
        
        html.Br(),
                  
        html.P('Select a continuous column name for analysis'),
                  
        dcc.Dropdown(
            id='nineth_dropdown',
            placeholder='Select a column name for analysis',
            options=[{'label': i, 'value': i}
                    for i in continuous_data]),
                  
        html.Br(),
                  
        html.P('Select a plot type for visualization'),
                  
        dcc.Dropdown(
            id='tenth_dropdown',
            placeholder='Select a plot to visualize',
            options=[{'label': 'line', 'value': 'line'}, {'label': 'scatter', 'value': 'scatter'}],
            value='scatter'),
    
        dcc.Graph(id='fourth_output')]),
        
        html.Br(),
        
        html.Div([html.H3('Heatmap')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
        
        dcc.Graph(figure=go.Figure(go.Heatmap(x=continuous_data, y=continuous_data, z=data[continuous_data].corr())))   
    
        ])


    @app.callback(Output('first_output', 'figure'), [Input('first_dropdown', 'value'), Input('second_dropdown', 'value')])

    def univariate_continuous_analysis(input_first_dropdown, input_second_dropdown):
        if len(continuous_data) > 0:
            if input_second_dropdown == 'histogram':
                fig = px.histogram(data[input_first_dropdown])
                return fig
            elif input_second_dropdown == 'box':
                fig = px.box(data[input_first_dropdown])
                return fig
            elif input_second_dropdown == 'violin':
                fig = px.violin(data[input_first_dropdown])
                return fig
            elif input_second_dropdown == 'strip':
                fig = px.strip(data[input_first_dropdown])
                return fig
            elif input_second_dropdown == 'scatter':
                fig = px.scatter(x=data.index, y=data[input_first_dropdown])
                return fig

    @app.callback(Output('fourth_output', 'figure'), [Input('eighth_dropdown', 'value'), Input('nineth_dropdown', 'value'), Input('tenth_dropdown', 'value')])

    def bivariate_continuous_analysis(input_eighth_dropdown, input_nineth_dropdown, input_tenth_dropdown):
        if len(continuous_data) > 0:
            if input_tenth_dropdown == 'line':
                fig = px.line(x=data[input_eighth_dropdown], y=data[input_nineth_dropdown])
                return fig
            elif input_tenth_dropdown == 'scatter':
                fig = px.scatter(x=data[input_eighth_dropdown], y=data[input_nineth_dropdown])
                return fig
            
    if __name__ == '__main__':
        app.run(port=4000)

def categorical_eda(data, category_data):
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly.express as px
    import plotly.graph_objects as go
    import dash
    from dash import html, dcc, Input, Output
    import warnings
    warnings.filterwarnings('ignore')
    
    app = dash.Dash(__name__)
    app.layout = html.Div([
    
        html.Div([html.H1('Exploratory Data Analysis')],
                 style = {
                     'text-align':'center',
                     'font-size':'20px',
                     'color':'blue',
                 }),
    
        html.Br(),
    
        html.Div([html.H3('Univariate Category data analysis')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
    
        html.P('Select a column name for analysis'),
    
        html.Div([dcc.Dropdown(
            id='third_dropdown',
            placeholder='Select a column name for analysis',
            options=[
                {'label': i, 'value' : i}
                for i in category_data
            ]),
        
        html.Br(),
                  
        html.P('Select a plot type for visualization'),
                  
        dcc.Dropdown(
            id='fourth_dropdown',
            placeholder='Select a plot type',
            options=[{'label':'bar', 'value':'bar'}],
            value='bar'
        ),
    
        dcc.Graph(id='second_output')]),
    
    
        html.Br(),
    
        html.Div([html.H3('Bivariate categorical data analysis')],
                 style = {
                     'text-align':'center'
                 }),
    
        html.Br(),
    
        html.P('Select a categorical column name for analysis'),
    
        html.Div([dcc.Dropdown(
            id='eleventh_dropdown',
            placeholder='Select a column name for analysis',
            options=[
                {'label': i, 'value' : i}
                for i in category_data
            ]),
        
        html.Br(),
                  
        html.P('Select a categorical column name for analysis'),
                  
        dcc.Dropdown(
            id='twelvefth_dropdown',
            placeholder='Select a column name for analysis',
            options=[{'label': i, 'value': i}
                    for i in category_data]),
                  
        html.Br(),
    
        dcc.Graph(id='fifth_output')]),
    
        html.Br(),
        
    ])

        
    @app.callback(Output('second_output', 'figure'), [Input('third_dropdown', 'value'), Input('fourth_dropdown', 'value')])

    def univariate_category_analysis(input_third_dropdown, input_fourth_dropdown):
        if len(category_data) > 0:
            if input_fourth_dropdown == 'bar':
                fig = px.bar(data[input_third_dropdown])
                return fig

    @app.callback(Output('fifth_output', 'figure'), [Input('eleventh_dropdown', 'value'), Input('twelvefth_dropdown', 'value')])

    def bivariate_categorical_analysis(input_eleventh_dropdown, input_twelvefth_dropdown):
        if len(category_data) > 0:
            mat = pd.crosstab(data[input_eleventh_dropdown], data[input_twelvefth_dropdown])
            fig = go.Figure(go.Heatmap(x=mat.columns, y=mat.index, z=mat))
            return fig
            
    if __name__ == '__main__':
        app.run(port=4000)