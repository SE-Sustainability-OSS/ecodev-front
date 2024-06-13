"""
Module containing various page layouts
"""
import dash_mantine_components as dmc
from dash import html


def simple_layout(main_content: html.Div) -> html.Div:
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
        id='left-aside',
        children=aside_content,
        zIndex=100,
        style={'padding-inline': '0px', 'width': '16vw', 'padding': '20px'},
        withBorder=True, visibleFrom='md')

    main_content = dmc.Stack([
        dmc.Group([
            dmc.Space(visibleFrom='md', style={'margin-left': '15vw'}),
            html.Div(main_content, style={'width': '80vw', 'height': '82vh'})
        ]), dmc.Space(h=50)])

    return html.Div([left_aside, main_content])


def page_right_aside(aside_content: html.Div, main_content: html.Div) -> html.Div:
    """
    Generates a page layout with a right aside.
    """
    right_aside = dmc.AppShellAside(
        id='right-aside',
        children=aside_content,
        zIndex=100,
        style={'padding-inline': '0px', 'width': '16vw', 'padding': '20px'},
        withBorder=True, visibleFrom='md')

    main_content = dmc.Stack([
        dmc.Group([
            html.Div(main_content, style={'width': '80vw', 'height': '82vh'}),
            dmc.Space(visibleFrom='md', style={'margin-right': '15vw'}),
        ]), dmc.Space(h=50)])

    return html.Div([right_aside, main_content])


def page_left_right_asides(left_aside: html.Div,
                           main_content: html.Div,
                           right_aside: html.Div) -> html.Div:
    """
    Generates a page layout with both a left and right aside.
    """
    left_aside = dmc.AppShellNavbar(
        id='left-aside',
        children=left_aside,
        zIndex=100,
        style={'padding-inline': '0px', 'width': '16vw', 'padding': '20px'},
        withBorder=True, visibleFrom='md')

    right_aside = dmc.AppShellAside(
        id='right-aside',
        children=right_aside,
        zIndex=100,
        style={'padding-inline': '0px', 'width': '16vw', 'padding': '20px'},
        withBorder=True, visibleFrom='md')

    main_content = dmc.Stack([
        dmc.Group([
            dmc.Space(visibleFrom='md', style={'margin-left': '15vw'}),
            html.Div(main_content, style={'width': '65vw', 'height': '82vh'}),
            dmc.Space(visibleFrom='md', style={'margin-right': '15vw'}),
        ]), dmc.Space(h=50)], style={'backgroundColor': '#f2f2f2'})

    return html.Div([left_aside, main_content, right_aside])
