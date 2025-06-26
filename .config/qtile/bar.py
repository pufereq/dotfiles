import random as rn
import subprocess
from math import floor
import socket

from libqtile import widget, bar
from libqtile.lazy import lazy

from spotify import Spotify


COLORS = {
    "red": "#BF616A",
    "orange": "#D08770",
    "yellow": "#EBCB8B",
    "green": "#A3BE8C",
    "purple": "#B48EAD",
}

HOSTNAME = socket.gethostname()

EMPTY = widget.Sep(
    linewidth=0,
    padding=0,
)


def random_colors(brightness: str):
    """Returns random colors with said brightness.

    Args:
        brightness (str): types: panel, fg, bg
    """
    # panel = {
    #     'navy': ["#08142b", "#1e42fa"],
    #     'green': ["#06260f", "#2bea45"],
    #     'orange': ["#2b1d10", "#9a8e37"],
    #     'maroon': ["#210808", "#d33636"],
    #     'violet': ["#250d2b", "#d335c6"]
    # }
    # rn.
    return ["#2e344088", "#eceff4"]


def widget_default():
    colors = random_colors("panel")

    widget_defaults = dict(
        font="MesloLGS NF",
        fontsize=14,
        padding=4,
        # background=colors[0],
        foreground=colors[1],
    )
    return widget_defaults


def status_bars():
    status_bar = bar.Bar(
        [
            # widget.Sep(padding=6, linewidth=0),
            # widget.Sep(),
            Spotify(format="{icon} | {artist} -"),
            Spotify(format="[{album}] - {track}", scroll=True, width=600),
            widget.Sep(linewidth=0, padding=6),
            # widget.GenPollText(
            #    func=media_data,
            #    update_interval=0.5,
            #    mouse_callbacks={"Button1": lazy.spawn("playerctl-wrapper-mine play-pause")}
            # ),
            # widget.Notify(parse_text=lambda t: t.replace("\n", " | ")),
            # widget.Clipboard(width=200, scroll=True),
            # widget.Prompt(),
            # widget.Moc(),
            widget.Spacer(),
            widget.Sep(),
            widget.CPU(format="cpu: {load_percent}% {freq_current}GHz"),
            widget.ThermalSensor(
                tag_sensor="Tctl", format="{temp:.1f}{unit}", update_interval=1
            ),
            # widget.ThermalSensor(tag_sensor="k10temp-pci-00c3"),
            widget.Sep(),
            widget.ThermalZone(
                zone="/sys/class/hwmon/hwmon2/temp1_input",
                fmt="gpu: {}",
                update_interval=1,
            ),
            widget.Sep(),
            widget.Memory(
                measure_mem="M",
                format="mem|swap: {MemUsed:.0f} {mm}B/{MemTotal:.0f} {mm}B ({MemPercent:.0f}%|{SwapPercent:.0f}%) {SwapUsed:.0f} {mm}B / {SwapTotal:.0f} {mm}B",
            ),
            widget.Sep(),
            widget.Net(
                format="{interface}: {down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}"
            ),
            widget.Sep(),
            widget.Wlan(format="wifu: {essid} {percent:2.1%}"),
            widget.Sep(),
            widget.PulseVolume(
                mouse_callbacks={"Button3": lazy.spawn("pavucontrol")},
                fmt="vol: {}",
                update_interval=0.5,
            ),
            widget.Sep(),
            widget.CapsNumLockIndicator(),
            widget.Sep(),
            widget.GenPollText(  # Updates label
                func=lambda: "Updates:",
                update_interval=60,
            ),
            widget.CheckUpdates(  # pacman
                display_format="{updates} (pacman),",
                distro="Arch_checkupdates",
                no_update_string="0 (pacman),",
            ),
            widget.CheckUpdates(  # AUR
                display_format="{updates} (AUR)",
                distro="Arch_yay",
                no_update_string="0 (AUR)",
            ),
            widget.Sep() if HOSTNAME == "pyrite" else EMPTY,
            widget.Battery(update_interval=1) if HOSTNAME == "pyrite" else EMPTY,
            # widget.Sep(),
            # widget.Battery(
            #     update_interval=2,
            #     notify_below=0.2,
            #     foreground=nth("gold")
            # ),
            # widget.Sep(linewidth=0, padding=6),
        ],
        size=24,
        margin=[0, 16, 16, 16],
        border_width=4,
        border_color="#00000000",
        background="#00000000",
    )
    return status_bar


def top_bars(screen: int):
    top_bar1 = bar.Bar(
        [
            # first half of bar
            widget.GroupBox(
                disable_drag=True,
                highlight_method="block",
                this_current_screen_border="#8fbcbb",
                this_screen_border="#81a1c1",
                other_current_screen_border="#4c566a",
                other_screen_border="#434c5e",
                active="#eceff4",
                inactive="#4c566a",
                # fontsize=40,
            ),
            widget.Sep(),
            widget.WindowName(for_current_screen=True),
            # widget.Spacer(),
            # second half of bar
            widget.Systray(padding=10) if screen == 0 else EMPTY,
            widget.Sep(),
            widget.KeyboardLayout(configured_keyboards=["pl", "us"]),
            widget.Sep(),
            widget.Clock(format="%A, %d %B %Y | %I:%M:%S %p"),
            widget.Sep(),
            widget.Wttr(location={"~53,20": "płock"}, format="%t (%f)"),
            widget.Wttr(location={"Płock": "płock"}, format="%c", fontsize=24),
            widget.Sep(),
            widget.CurrentLayout(),
            # widget.Sep(linewidth=0, padding=6)
        ],
        size=32,
        margin=[16, 16, 0, 16],
        border_width=4,
        # border_color="#5e81ac",
        # border_color="#2e344080",
        # background="#2e344080",
        border_color="#00000000",
        background="#00000000",
    )
    return top_bar1
