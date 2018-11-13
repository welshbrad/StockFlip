import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
from datetime import datetime
import Utils


def make_chart(symbol):
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
        div = offline.plot(data, include_plotlyjs=False, output_type='div')
        return div

def make_html(symbol):
        html = '<html><head><meta charset="utf-8" />'
        html += '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
        html += '<body>'
        html += make_chart(symbol)
        html += '</body></html>'
        return html