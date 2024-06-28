"""
Module containing various page layouts
"""
from typing import Any
from typing import Optional

import dash_mantine_components as dmc
from dash import html

from ecodev_front.ids import LEFT_ASIDE_ID
from ecodev_front.ids import MAIN_CONTENT_ID
from ecodev_front.ids import RIGHT_ASIDE_ID


def simple_layout(main_content: html.Div) -> dmc.Stack:
    """
    Generates a simple page layout
    """
    return dmc.Stack([
        html.Div(main_content, style={'width': '95vw', 'height': '82vh'}),
        dmc.Space(h=50)
    ])


def page_left_aside(aside_content: html.Div, main_content: html.Div) -> html.Div:
    """
    Generates a page layout with a left aside.
    """
    left_aside = dmc.AppShellNavbar(
        id=LEFT_ASIDE_ID,
        children=aside_content,
        zIndex=100,
        style={'padding-inline': '0px', 'width': '16vw', 'padding': '20px'},
        withBorder=True, visibleFrom='md')

    main_content = dmc.Stack([
        dmc.Group([
            dmc.Space(visibleFrom='md', style={'margin-left': '15vw'}),
            html.Div(id=MAIN_CONTENT_ID, children=main_content,
                     style={'width': '80vw', 'height': '82vh'})
        ]), dmc.Space(h=50)])

    return html.Div([left_aside, main_content])


def page_right_aside(aside_content: html.Div, main_content: html.Div) -> html.Div:
    """
    Generates a page layout with a right aside.
    """
    right_aside = dmc.AppShellAside(
        id=RIGHT_ASIDE_ID,
        children=aside_content,
        zIndex=100,
        style={'padding-inline': '0px', 'width': '16vw', 'padding': '20px'},
        withBorder=True, visibleFrom='md')

    main_content = dmc.Stack([
        dmc.Group([
            html.Div(id=MAIN_CONTENT_ID, children=main_content,
                     style={'width': '80vw', 'height': '82vh'}),
            dmc.Space(visibleFrom='md', style={'margin-right': '15vw'}),
        ]), dmc.Space(h=50)])

    return html.Div([right_aside, main_content])


def page_left_right_asides(left_aside: Optional[dmc.Stack] = None,
                           main_content: Optional[Any] = None,
                           right_aside: Optional[Any] = None) -> html.Div:
    """
    Generates a page layout with both a left and right aside.
    """
    left_aside = dmc.AppShellNavbar(
        id=LEFT_ASIDE_ID,
        children=left_aside,
        zIndex=100,
        style={'padding-inline': '0px', 'width': '16vw', 'padding': '20px'},
        withBorder=True, visibleFrom='md')

    right_aside = dmc.AppShellAside(
        id=RIGHT_ASIDE_ID,
        children=right_aside,
        zIndex=100,
        style={'padding-inline': '0px', 'width': '16vw', 'padding': '20px'},
        withBorder=True, visibleFrom='md')

    main_content = dmc.Stack([
        dmc.Group([
            dmc.Space(visibleFrom='md', style={'margin-left': '16vw'}),
            html.Div(id=MAIN_CONTENT_ID, children=main_content,
                     style={'width': '65vw', 'height': '82vh', 'justifyContent': 'center',
                            'display': 'flex'}),
            dmc.Space(visibleFrom='md', style={'margin-right': '16vw'}),
        ]), dmc.Space(h=50)], style={'backgroundColor': '#f2f2f2'})

    return html.Div([left_aside, main_content, right_aside])
