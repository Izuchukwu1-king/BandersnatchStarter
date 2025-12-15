from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df, x, y, target) -> Chart:
    """
    df: DataFrame
    #data to  graph
    X:str
    #column to go on X-axis
    y:str 
    #column to go on y-axis
    target:str
    #column to be shwon in color
    #return
    """
    vis = Chart(
       df,
       title=f"{y} by {x} for {target}" 
    ).mark_circle(size=90).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    ).properties(
        width=400,
        height=400,
        padding=50,
        background="#222222"
    ).configure(
        legend={
            "titleColor":"#666666",
            "labelColor":"#00000000",
            "padding":10
        },
        title={
            "color": "#000000",
            "fontSize":25,
            "offset":30
        },
        # axis={
        #     #"x":"x",
        #     "y":"y",
        #     "title":"title",
        #     #"color":"target"
        #}
    )

    return vis
