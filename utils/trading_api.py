import plotly.graph_objects as go
import yfinance as yf


def plot_ticker(ticker: yf.ticker.Ticker, mode: str = "png"):
    mini_data = ticker.history(
        period="1d",
        interval="1m",
        start=None,
        end=None,
        actions=True,
        auto_adjust=True,
        back_adjust=False,
    )
    fig = go.Figure(
        data=go.Ohlc(
            x=mini_data.index,
            open=mini_data.Open,
            high=mini_data.High,
            low=mini_data.Low,
            close=mini_data.Close,
        )
    )
    fig.update(layout_xaxis_rangeslider_visible=False)
    if mode == "png":
        fig.show("png")
    else:
        fig.show()
