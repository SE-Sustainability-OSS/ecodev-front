"""
Module implementing segmented control
"""
import dash_mantine_components as dmc


def segmented_control(id: str,
                      label: str,
                      value: str | None = None,
                      data: list[str] | None = []) -> dmc.SegmentedControl:
    """
    Renders a dmc.SegmentedControl that allows to toggle between different values
    """
    return dmc.SegmentedControl(
        id=id,
        label=label,
        value=value,
        data=data
    )


def segmented_control_label(id: str,
                            label: str,
                            value: str | None = None,
                            data: list[str] | None = [],
                            size: str = 'md',
                            c: str = '#A0AEC0') -> dmc.Stack:
    """
    Renders a segmented control with a stylized label
    """

    return dmc.Stack([
        dmc.Text(label, c=c),
        dmc.SegmentedControl(
            id=id,
            value=value,
            data=data,
            size=size,
        )
    ], gap='xs', w='100%')
