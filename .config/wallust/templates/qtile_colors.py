from typing import Final


class ColorPalette:
    BACKGROUND: Final[str] = "{{background}}"
    FOREGROUND: Final[str] = "{{foreground}}"

    BORDER_NORMAL: Final[str] = "{{background | lighten(0.2)}}"
    BORDER_FOCUS: Final[str] = "{{color14}}"

    TOP_BAR_BACKGROUND: Final[str] = "{{color0}}00"
    TOP_BAR_FOREGROUND: Final[str] = "{{foreground}}"
    TOP_BAR_BORDER: Final[str] = "{{color0}}00"

    BOTTOM_BAR_BACKGROUND: Final[str] = "{{color0}}80"
    BOTTOM_BAR_FOREGROUND: Final[str] = "{{foreground}}"
    BOTTOM_BAR_BORDER: Final[str] = "{{color0}}80"

    GROUPBOX_THIS_CURRENT_SCREEN: Final[str] = "{{color6}}"
    GROUPBOX_THIS_SCREEN: Final[str] = "{{color5}}"
    GROUPBOX_OTHER_CURRENT_SCREEN: Final[str] = "{{color6 | lighten(0.2)}}"
    GROUPBOX_OTHER_SCREEN: Final[str] = "{{color5 | lighten(0.2)}}"
