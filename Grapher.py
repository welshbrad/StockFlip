import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
from datetime import datetime
import Utils

"""
This will format and return the HTML div element that represents the chart for a given symbol. Data reaches 1y maximum.
"""
def make_chart(symbol):
        buttons = list([dict(count=1,label='1m',step='month',stepmode='backward'),dict(count=6,label='6m',step='month',stepmode='backward'),dict(count=1,label='YTD',step='year',stepmode='todate'),dict(count=1,label='1y',step='year',stepmode='backward'),dict(step='all')])
        xaxis=dict(rangeselector=dict(buttons=buttons), rangeslider=dict(visible = True), type='date', title='Date',titlefont=dict(family='Courier New, monospace',size=12,color='#7f7f7f'))
        yaxis=dict(title='Price',titlefont=dict(family='Courier New, monospace',size=12,color='#7f7f7f'))
        layout = go.Layout(xaxis=xaxis, yaxis=yaxis)


        config = {'showLink': False, 'scrollZoom': True}

        data = Utils.get_chart_data(symbol)

        open_data = [day["open"] for day in data]
        high_data = [day["high"] for day in data]
        low_data = [day["low"] for day in data]
        close_data = [day["close"] for day in data]
        dates = [day["date"] for day in data]

        trace = go.Candlestick(x=dates,
                        open=open_data,
                        high=high_data,
                        low=low_data,
                        close=close_data)
        data = [trace]
        figure=go.Figure(data=data,layout=layout)
        div = offline.plot(figure, include_plotlyjs=False, output_type='div', config=config)
        return div

"""
This will build the HTML that will be embedded into the QWebEngineView widget
"""
def make_html(symbol):
        html = '<html><head><meta charset="utf-8" />'
        html += '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
        html += '<body>'
        html += make_chart(symbol)
        html += '</body></html>'
        return html
