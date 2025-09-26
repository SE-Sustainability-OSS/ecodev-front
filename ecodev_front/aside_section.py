"""
File containing an aside section component, in the form of an accordion item with a label.
"""

import dash_mantine_components as dmc


def aside_section(title: str, children: list) -> dmc.AccordionItem:
    """
    Renders an aside section as an accordion item
    """
    return dmc.AccordionItem([
        dmc.AccordionControl(
            dmc.Divider(w='95%', label=title), className='aside'),
        dmc.AccordionPanel(
            dmc.Stack(children, gap='sm', mt=0)),
    ], value=title.lower().replace(' ', '-'))
