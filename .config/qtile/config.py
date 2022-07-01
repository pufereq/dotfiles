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

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()
browser = 'firefox-nightly'
file_manager = 'pcmanfm'

### Key Functions
def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)
keys = [
    ### Essentials
    Key([mod], 'Return', lazy.spawn(terminal), desc = 'Launch the Terminal'),
    Key([mod, 'shift'], 'Return', lazy.spawn('rofi -show run'), desc = 'Run Launcher'),
    Key([mod], 'Tab', lazy.next_layout(), desc = 'Toggle through layouts'),
    Key([mod, 'shift'], 'c', lazy.window.kill(), desc = 'Kill active window',),
    Key([mod, "control"], "r", lazy.restart(), desc="Reload the config"),
    Key([mod, 'control'], 'q', lazy.shutdown(), desc = 'Shutdown Qtile'),
    ### Switch focus of monitors
    Key([mod], 'period', lazy.next_screen(), desc = 'Move focus to next monitor'),
    Key([mod], 'comma', lazy.prev_screen(), desc = 'Move focus to prev monitor'),
    Key([mod,'shift'],  'comma',  lazy.function(window_to_next_screen), desc = 'Move active window to next screen'),
    Key([mod,'shift'],  'period', lazy.function(window_to_previous_screen), desc = 'Move active window to previous screen'),
    ### Window controls
    Key([mod], 'j', lazy.layout.down(), desc = 'Move focus down'),
    Key([mod], 'k', lazy.layout.up(), desc = 'Move focus up'),
    Key([mod], 'h', lazy.layout.left(), desc = 'Move focus left'),
    Key([mod], 'l', lazy.layout.right(), desc = 'Move focus right'),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    ### Applications
    Key([mod], 'b', lazy.spawn(browser), desc = 'Launch web browser'),
    Key([mod, 'shift'], 'v', lazy.spawn('code'), desc = 'Launch code'),
    Key([mod], 'f', lazy.spawn(file_manager), desc = 'Launch file manager'),
    Key([mod], 'l', lazy.spawn('i3lock --color 4d4d4d --show-failed-attempts')),
    Key([mod, 'shift'], 's', lazy.spawn('gnome-screenshot -a'))
    ]

group_names = 'WEB DEV GAMES MUSIC VM DOC CHAT GFX'.split()
groups = [Group(name, layout='MonadTall') for name in group_names]

for i, name in enumerate(group_names):
    indx = str(i + 1)
    keys += [
        Key([mod], indx, lazy.group[name].toscreen()),
        Key([mod, 'shift'], indx, lazy.window.togroup(name))]

color = [
            ['#6600cc', '#6600cc'], # 0 active group this monitor
            ['#6666ff', '#6666ff'], # 1 inactive group this monitor
            ['#9966ff', '#9966ff'], # 2 active group other monitor
            ['#9999ff', '#9999ff'], # 3 inactive group other monitor
            ['#ff4000', '#ff4000'], # 4 critical temp
            ['#ffa31a', '#ffa31a'], # 5 high temp
            ['#9900ff', '#9900ff'], # 6 active window
            ['#5d5dd5', '#5d5dd5'], # 7 inactive window
        ]
layout_theme = {
        'margin': 8,
        'border_focus': color[6],
        'border_normal': color[7],
        'border_width': 4
}

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
	#layout.Floating(**layout_theme)
]

widget_defaults = dict(
    font="Ubuntu",
    fontsize=11,
    padding=3,
    )
extension_defaults = widget_defaults.copy()

sep_defaults = dict(
    line_width = 0,
    padding = 6
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                    ),
                widget.GroupBox(
                    disable_drag = True,
                    highlight_method = 'block',
                    this_current_screen_border = color[0],
                    this_screen_border = color[1],
                    other_current_screen_border = color[0],
                    other_screen_border = color[1]
                    ),
				widget.WindowName(
                    for_current_screen = True
                    ),

				widget.CPU(
                    format = 'CPU: {load_percent}%',
                    mouse_callbacks = {'Button1': lazy.spawn(terminal + ' -e htop')}
                    ),
                widget.ThermalZone(
                    high = 50,
                    crit = 70,
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.NvidiaSensors(
                    threshold = 60,
                    foreground_alert = 'ff6000',
                    fmt = 'GPU: {}',
                    format = '{temp}°C',
                    mouse_callbacks = {'Button1': lazy.spawn(terminal + ' -e nvtop')}
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.Memory(
                    format = 'RAM: {MemUsed:.0f}{mm} /{MemTotal: .0f}{mm}',
                    mouse_callbacks = {'Button1': lazy.spawn(terminal + ' -e htop')}
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0	
					),
                widget.Memory(
                    format = 'Swap: {SwapUsed:.0f}{mm} /{SwapTotal: .0f}{mm}',
                    mouse_callbacks = {'Button1': lazy.spawn(terminal + ' -e htop')}
                    ),
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                        ),
                widget.DF(
                    visible_on_warn = False,
                    partition = '/',
                    format = '💾 {p} - {r:.0f}%'
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.DF(
                    visible_on_warn = False,
                    partition = '/home',
                    format = '💾 {p} - {r:.0f}%'
                    ), 
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.Net(
                    interface = 'wlan0',
                    format = '🌐{down} ↓↑ {up}',
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0				
					),
                widget.CheckUpdates(
                    update_interval = 10,
                    fmt = '↻ {}',
                    display_format = '{updates}',
                    no_update_string = 'none',
                    execute = f'{terminal} -e yay -Syu'
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.PulseVolume(
                    fmt = '🔊 {}',
                    update_interval = 0.1,
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
						),
                widget.CapsNumLockIndicator(),
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                        ),
                widget.KeyboardLayout(
                    configured_keyboards = ['pl', 'us']
                        ),
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                        ),
                widget.Systray(),
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                        ),
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                        ),
                widget.Wttr(
                    location = {'Plock': 'Płock'},
                    mouse_callbacks = {'Button1': lazy.spawn(f'{terminal} -e /home/artur/.config/qtile/wttr.sh')}
                        ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.Clock(
                    format = '🕒 %A, %d %B %Y; %I:%M:%S %p',
                    ),
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                        ),
                widget.TextBox(
                    text = '[exit]',
                    mouse_callbacks = {'Button1': lazy.spawn('i3lock --color 4d4d4d --show-failed-attempts'), 
                        'Button2': lazy.spawn('reboot'),
                        'Button3': lazy.spawn('shutdown now')}
                        ),
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                    ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),

Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                    ),
                widget.GroupBox(
                    disable_drag = True,
                    highlight_method = 'block',
                    this_current_screen_border = color[0],
                    this_screen_border = color[1],
                    other_current_screen_border = color[0],
                    other_screen_border = color[1]
                    ),
				widget.WindowName(
                    for_current_screen = True
                    ),

				widget.CPU(
                    format = 'CPU: {load_percent}%',
                    mouse_callbacks = {'Button1': lazy.spawn(terminal + ' -e htop')}
                    ),
                widget.ThermalZone(
                    high = 50,
                    crit = 70,
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.NvidiaSensors(
                    threshold = 60,
                    foreground_alert = 'ff6000',
                    fmt = 'GPU: {}',
                    format = '{temp}°C',
                    mouse_callbacks = {'Button1': lazy.spawn(terminal + ' -e nvtop')}
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.Memory(
                    format = 'RAM: {MemUsed:.0f}{mm} /{MemTotal: .0f}{mm}',
                    mouse_callbacks = {'Button1': lazy.spawn(terminal + ' -e htop')}
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0	
					),
                widget.Memory(
                    format = 'Swap: {SwapUsed:.0f}{mm} /{SwapTotal: .0f}{mm}',
                    mouse_callbacks = {'Button1': lazy.spawn(terminal + ' -e htop')}
                    ),
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                        ),
                widget.DF(
                    visible_on_warn = True,
                    partition = '/',
                    format = '💾 {p} - {r:.0f}%'
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.DF(
                    visible_on_warn = True,
                    partition = '/home',
                    format = '💾 {p} - {r:.0f}%'
                    ), 
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.Net(
                    interface = 'wlan0',
                    format = '🌐{down} ↓↑ {up}',
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0				
					),
                widget.CheckUpdates(
                    update_interval = 10,
                    fmt = '↻ {}',
                    display_format = '{updates}',
                    no_update_string = 'none',
                    execute = f'{terminal} -e yay -Syu'
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.PulseVolume(
                    fmt = '🔊 {}',
                    update_interval = 0.1,
                    ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
						),
                widget.KeyboardLayout(
                    configured_keyboards = ['pl', 'us']
                        ),
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                        ),
                widget.Wttr(
                    location = {'Plock': 'Płock'},
                    mouse_callbacks = {'Button1': lazy.spawn(f'{terminal} -e /home/artur/.config/qtile/wttr.sh')}
                        ),
                widget.Sep(
					padding = 6,
                    linewidth = 0
					),
                widget.Clock(
                    format = '🕒 %A, %d %B %Y; %I:%M:%S %p',
                    ),
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                        ),
                widget.TextBox(
                    text = '[exit]',
                    mouse_callbacks = {'Button1': lazy.spawn('i3lock --color 4d4d4d --show-failed-attempts'), 
                        'Button2': lazy.spawn('reboot'),
                        'Button3': lazy.spawn('shutdown now')}
                        ),
                widget.Sep(
                    padding = 6,
                    linewidth = 0
                    ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Origin")
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
