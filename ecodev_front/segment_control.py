"""
Module implementing segmented control
"""
import dash_mantine_components as dmc

from ecodev_front import theme_config


def segmented_control(id: str,
                      label: str | None = None,
                      value: str | None = None,
                      data: list[str] | None = None,
                      size: str = 'md',
                      c: str | None = None,
                      width: int | str = '100%') -> dmc.SegmentedControl | dmc.Stack:
    """
    Renders a segmented control with a stylized label
    """
    content = [dmc.SegmentedControl(id=id, value=value, data=data or [], size=size)]

    if not label:
        return content[0]

    content = [dmc.Text(label, c=c or theme_config.GRAY_COLOR)] + content
    return dmc.Stack(content, gap='xs', w=width)
