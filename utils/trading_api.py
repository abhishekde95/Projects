import plotly.graph_objects as go
import yfinance as yf


def plot_ticker(
    ticker: yf.ticker.Ticker,
    period: str = "1d",
    interval: str = "1m",
    mode: str = "png",
):
    mini_data = ticker.history(
        period=period,
        interval=interval,
        start=None,
        end=None,
        actions=True,
        auto_adjust=True,
        back_adjust=False,
    )

    expected_columns = ["Open", "High", "Low", "Close"]
    if not set(expected_columns).issubset(set(mini_data.columns)):
        raise ValueError(
            f"Expected columns: {expected_columns}, but got {mini_data.columns}"
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
