# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


from bar import top_bars, widget_default, status_bars

mod = "mod4"
terminal = guess_terminal()
FILE_MANAGER = "pcmanfm -n"
WEB_BROWSER = "firefox"
TOR_BROWSER = "tor-browser"
TEXT_EDITOR = "code --no-sandbox"
CHAT = "discord"
# MUSIC = "alacritty -e spt"
MUSIC = "spotify"


keys = [
    # NEEDED
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle Floating"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # USER
    # power menu
    Key([], "XF86PowerOff", lazy.spawn('rofi -show p -modi p:\'rofi-power-menu --symbols-font "Symbols Nerd Font Mono"\' -theme-str \'window {width: 10em;} listview {lines: 6;}\' -font "MesloLGS NF 16"')),
    # audio
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("/home/artur/.config/qtile/change-volume toggle"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("/home/artur/.config/qtile/change-volume up"),
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("/home/artur/.config/qtile/change-volume down"),
    ),
    # brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    # media
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause ")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    # run
    Key(
        [mod, "control"],
        "Return",
        lazy.spawn("rofi -show run -show-icons"),
        desc="Spawn a command using a prompt widget",
    ),
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn("rofi -show drun -show-icons"),
        desc="Spawn an app using a prompt widget",
    ),
    Key(
        [mod, "shift"],
        "e",
        lazy.spawn("rofimoji"),
        desc="Spawn an emoji using a prompt widget",
    ),
    Key([mod], "l", lazy.spawn("betterlockscreen -l blur"), desc="Lock screen"),
    Key([mod, "control"], "delete", lazy.spawn("xkill"), desc="Kill a window"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Launch Flameshot in gui mode."),
    # apps
    Key([mod], "v", lazy.spawn(TEXT_EDITOR), desc="Launch Visual Studio Code"),
    Key([mod], "f", lazy.spawn(FILE_MANAGER), desc="Launch File Manager"),
    Key([mod], "b", lazy.spawn(WEB_BROWSER), desc="Launch Web Browser"),
    Key([mod, "control"], "b", lazy.spawn(TOR_BROWSER), desc="Launch Tor Browser"),
    Key([mod], "d", lazy.spawn(CHAT), desc="Launch Chat Application"),
    Key([mod], "s", lazy.spawn(MUSIC), desc="Launch Music Player"),
    Key([mod], "o", lazy.spawn("obs"), desc="Launch OBS"),
    Key(
        [mod, "shift"],
        "o",
        lazy.spawn("obs --startrecording"),
        desc="Launch OBS and auto record",
    ),
    # chords
    # EasyEffects preset changer
    KeyChord(
        [mod],
        "e",
        [
            Key(
                [],
                "d",
                lazy.spawn(  # send notification
                    "notify-send -t 3000 -u low -a EasyEffects 'Preset: default' 'EasyEffects preset changed to default'"
                ),
                lazy.spawn("easyeffects -l default"),  # set preset
                desc="Set EasyEffects to default preset",
            ),
            Key(
                [],
                "r",
                lazy.spawn(  # send notification
                    "notify-send -t 3000 -u low -a EasyEffects 'Preset: default_reverb' 'EasyEffects preset changed to default_reverb'"
                ),
                lazy.spawn("easyeffects -l default_reverb"),  # set preset
                desc="Set EasyEffects to default_reverb preset",
            ),
            Key(
                [],
                "l",
                lazy.spawn(  # send notification
                    "notify-send -t 3000 -u low -a EasyEffects 'Preset: low_bass' 'EasyEffects preset changed to low_bass'"
                ),
                lazy.spawn("easyeffects -l low_bass"),  # set preset
                desc="Set EasyEffects to low_bass preset",
            ),
        ],
    ),
]


def match_class(*names: str | list):
    ret_list = []
    if isinstance(names, str):
        return [Match(wm_class=names), Match(title=names)]
    for app in names:
        ret_list.append(Match(wm_class=app))
        ret_list.append(Match(title=app))
    return ret_list


groups = [
    Group("1", label="WEB", matches=match_class("firefox", "chromium")),
    Group("2", label="DEV", matches=match_class("code")),
    Group("3", label="GAME", matches=match_class("steam", "RobloxPlayerBeta.exe")),
    Group("4", label="MUS", matches=match_class("spotify")),
    Group("5", label="CHAT", matches=match_class("discord")),
    Group("6", label="DOC", matches=match_class("libreoffice", "soffice.bin")),
    Group("7", label="VM", matches=match_class("vmplayer", "vmware", "virt-manager")),
    Group("8", label="GFX", matches=match_class("gimp-2.10")),
    Group("9", label="SYS", spawn=["pavucontrol", "easyeffects"]),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # Key([mod], i.name, lazy.function(go_to_group(i.name))),
            # Or, use below if you prefer not to switch to that group.
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="Move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        margin=16,
        border_width=6,
        border_focus="#88c0d0",
        border_normal="#3b4252",
    ),
    layout.MonadWide(
        margin=16,
        border_width=6,
        border_focus="#88c0d0",
        border_normal="#3b4252",
    ),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = widget_default()
extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=top_bars(0), bottom=status_bars()),
    Screen(top=top_bars(1), bottom=status_bars()),
    # Screen(top=top_bars(2), bottom=status_bars()),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="Origin"),  # Origin launcher
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="gpg"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart/global.sh")
    subprocess.Popen([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
