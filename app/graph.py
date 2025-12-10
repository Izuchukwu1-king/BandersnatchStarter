from altair import Chart
from altair import Chart, Tooltip
from pandas import DataFrame

def chart(df, x, y, target) -> Chart:
    """
    Creates and returns a Chart object from a DataFrame
    with the specified x, y, and target configuration.
    """
    chart_obj = Chart(df)
    chart_obj.config = {
        "x": x,
        "y": y,
        "target": target
    }
    return chart_obj

    c = chart(df, x="strength", y="speed", target="type")

    c.info()

result = c("strength")   # calls __call__

c.save("chart.pkl")

