"""
Functions to interact with plotly graph objects
"""
from plotly import graph_objs as go


def hide_duplicate_legends(fig: go.Figure):
    """
    Hides duplicates legend
    """

    names = set()
    fig.for_each_trace(
        lambda trace:
        trace.update(showlegend=False)
        if (trace.name in names) else names.add(trace.name))

    return fig
