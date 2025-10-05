import socket

from libqtile import widget, bar
from libqtile.lazy import lazy

from colors import ColorPalette


HOSTNAME = socket.gethostname()

EMPTY = widget.Sep(
    linewidth=0,
    padding=0,
)


def widget_default():
    widget_defaults = dict(
        font="MesloLGS Nerd Font",
        # font="MonaspiceNe Nerd Font",
        fontsize=14,
        padding=4,
        # background=colors[0],
        foreground=ColorPalette.FOREGROUND,
    )
    return widget_defaults


def status_bars():
    status_bar = bar.Bar(
        [
            # widget.Sep(padding=6, linewidth=0),
            # widget.Sep(),
            # Spotify(format="{icon} | {artist} -"),
            # Spotify(format="[{album}] - {track}", scroll=True, width=600),
            widget.Mpris2(
                name="YoutubeMusic",
                paused_text=" | {track}",
                playing_text=" | {track}",
                format="{xesam:artist} - [{xesam:album}] - {xesam:title}",
            ),
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
            widget.CPU(format="cpu: {load_percent}% {freq_current}GHz"),
            widget.ThermalSensor(
                tag_sensor="Tctl" if HOSTNAME != "chonkyboi" else "CPU",
                format="{temp:.1f}{unit}",
                update_interval=1,
            ),
            widget.GenPollCommand(
                cmd=["bash", "/home/artur/.config/qtile/tp_get_fan_rpm.sh"],
                fmt="{} RPM",
                update_interval=1,
            )
            if HOSTNAME == "chonkyboi"
            else EMPTY,
            # widget.ThermalSensor(tag_sensor="k10temp-pci-00c3"),
            widget.Sep(),
            widget.ThermalSensor(
                tag_sensor="amdgpu-pci-0300-temp1",
                format="{tag}: {temp:.1f}{unit}",
                fmt="gpu: {}",
                update_interval=1,
            )
            if HOSTNAME == "quartzium"
            else EMPTY,
            widget.Sep() if HOSTNAME != "chonkyboi" else EMPTY,
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
            widget.Sep() if HOSTNAME == "chonkyboi" else EMPTY,
            widget.Battery(battery="BAT0", update_interval=1, fmt="I: {}")
            if HOSTNAME == "chonkyboi"
            else EMPTY,
            widget.Sep() if HOSTNAME == "chonkyboi" else EMPTY,
            widget.Battery(battery="BAT1", update_interval=1, fmt="E: {}")
            if HOSTNAME == "chonkyboi"
            else EMPTY,
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
        border_color=ColorPalette.BOTTOM_BAR_BORDER,
        background=ColorPalette.BOTTOM_BAR_BACKGROUND,
    )
    return status_bar


def top_bars(screen: int):
    top_bar1 = bar.Bar(
        [
            # first half of bar
            widget.GroupBox(
                disable_drag=True,
                highlight_method="block",
                this_current_screen_border=ColorPalette.GROUPBOX_THIS_CURRENT_SCREEN,
                this_screen_border=ColorPalette.GROUPBOX_THIS_SCREEN,
                other_current_screen_border=ColorPalette.GROUPBOX_OTHER_CURRENT_SCREEN,
                other_screen_border=ColorPalette.GROUPBOX_OTHER_SCREEN,
                active=ColorPalette.FOREGROUND,
                inactive=ColorPalette.BACKGROUND,
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
        border_color=ColorPalette.TOP_BAR_BORDER,
        background=ColorPalette.TOP_BAR_BACKGROUND,
    )
    return top_bar1
