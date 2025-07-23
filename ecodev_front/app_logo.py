"""
File containing method to display the application's logo with a specific aspect ratio.
"""
import dash_mantine_components as dmc


def app_logo(logo_path: str = '/assets/logo.png',
             ratio: float = 570 / 128,
             width: int | str = 60,
             style: dict[str, str | int] | None = None
             ) -> dmc.AspectRatio:
    """
    Application logo component.
    """
    style = style or {'margin-left': '10px', 'width': width}
    return dmc.AspectRatio(dmc.Image(src=logo_path), ratio=ratio, style=style,
                           mt=12.5)
