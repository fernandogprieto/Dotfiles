#
#  ________    ______  _______    
# |_   __  | .' ___  ||_   __ \   𝘍𝘦𝘳𝘯𝘢𝘯𝘥𝘰 𝘎. 𝘗𝘳𝘪𝘦𝘵𝘰
#   | |_ \_|/ .'   \_|  | |__) |  𝘩𝘵𝘵𝘱𝘴://𝘨𝘪𝘵𝘩𝘶𝘣.𝘤𝘰𝘮/𝘧𝘦𝘳𝘯𝘢𝘯𝘥𝘰𝘨𝘱𝘳𝘪𝘦𝘵𝘰/
#   |  _|   | |   ____  |  ___/   𝘩𝘵𝘵𝘱𝘴://𝘵𝘸𝘪𝘵𝘵𝘦𝘳.𝘤𝘰𝘮/𝘧𝘦𝘳𝘯𝘢𝘯𝘥𝘰𝘨𝘱𝘳𝘪𝘦𝘵𝘰
#  _| |_    \ `.___]  |_| |_      
# |_____|    `._____.'|_____| 
#
# 𝘔𝘺 𝘲𝘵𝘪𝘭𝘦.𝘤𝘰𝘯𝘧𝘪𝘨 𝘫𝘶𝘴𝘵 𝘴𝘰𝘮𝘦 𝘴𝘵𝘢𝘯𝘥𝘢𝘳𝘥 𝘴𝘵𝘶𝘧𝘧!

# coding: utf-8
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile import bar, layout, widget, extension, hook
from libqtile.config import KeyChord, Click, Drag, Group, ScratchPad, DropDown, Key, Match, Screen  
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401

mod = "mod4"                  # Sets mod key to SUPER/WINDOWS
terminal = "alacritty"        # My terminal
browser = "google-chrome"     # My browser choice

keys = [
    ## Principles
    Key([mod], "Return",lazy.spawn(terminal+" -e fish"),desc='launch terminal'),
    Key([mod], "b", lazy.spawn(browser),desc='google-chrome'),
    Key([mod], "r", lazy.spawn("dmenu_run -p 'Run: '"), desc='run Launcher '),
    Key([mod], "w", lazy.window.kill(), desc='kill focused window'),
    Key([mod, "control"], "r", lazy.reload_config(), desc='reload the config'),
    Key([mod, "control"], "q", lazy.shutdown(), desc='shutdown qtile'),
    
    ## Windows controls
    Key([mod], "h", lazy.layout.left(), desc='move focus to left'),
    Key([mod], "l", lazy.layout.right(), desc='move focus to right'),
    Key([mod], "j", lazy.layout.down(), desc='move focus down'),
    Key([mod], "k", lazy.layout.up(), desc='move focus up'),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc='move window to the left'),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc='move window to the right'),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc='move window down'),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc='move window up'),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc='grow window to the left'),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc='grow window to the righ'),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc='grow window down'),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc='grow window up'),
    Key([mod], "n", lazy.layout.normalize(), desc='reset all window sizes'),
    Key([mod], "m", lazy.layout.maximize(), desc='toggle window between minimum and maximum sizes'),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    
    ## Stack panel controls
    Key([mod], "Tab", lazy.next_layout(), desc='toggle between layouts'),
    Key([mod, "shift"], "Tab", lazy.layout.rotate(), lazy.layout.flip(), desc='Switch which side main pane occupies (XmonadTall)'),
    Key([mod], "space", lazy.layout.next(), desc='move window focus to other window'),
    Key([mod, "shift"], "space", lazy.layout.toggle_split(), desc='toggle between split and unsplit sides of stack'),
    
    #Dmenu integration
     Key(['mod4'], 'r', lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="Run: ",
        dmenu_font="sans-12",
        background="#1d1f21",
        foreground="#7BC0F5",
        selected_background="#E270A4",
        selected_foreground="#1d1f21",
        dmenu_botton= False,
        dmenu_lines= 10,
    ))),  
]

groups = [
    Group("1", label="SYS", layout='ratiotile'),
    Group("2", label="IT", layout='monadtall'),
    Group("3", label="SYS", layout='monadtall'),
    Group("4", label="DEV", layout='monadtall'),
    Group("5", label="WWW", layout='monadtall'),
    Group("6", label="DOC", layout='monadtall'),
    Group("7", label="CLOUD", layout='monadtall'),
    Group("8", label="CHAT", layout='monadtall'),
    Group("9", label="VID", layout='monadtall'),
        ]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
            # mod1 + shift + letter of group = switch to & move focused window to group
            #Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
            # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc="move focused window to group {}".format(i.name)),
            #Extend key list keybinding with scratchpad
            #Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
        ]
    )

#Scratchpad config
#groups.append(ScratchPad("scratchpad", [
#    DropDown("term", "kitty", opacity=0.8 x=0.03, y=0.2),
#]))

layout_theme = {"border_width": 2,
                "margin": 2,
                "border_focus": "d75f5f",
                "border_normal": "1D2330",
                "font": "FiraCode-Regular",
                "grow_amount": 2,
                }

layouts = [
    layout.RatioTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Stack(num_stacks=2, **layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
    layout.TreeTab(
         font = "FiraCode-Regular",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "c678dd",
         active_fg = "000000",
         inactive_bg = "a9a1e1",
         inactive_fg = "1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200,
         ),
]

#Colors for the bar
colors = [
        ["#282c34", "#282c34"],  # Active Workspace
        ["#686f9a", "#686f9a"],  # Inactive Workspace
        ["#16172d", "#16172d"],  # background lighter 2
        ["#e33400", "#e33400"],  # red 3
        ["#5ccc96", "#5ccc96"],  # green 4
        ["#b3a1e6", "#b3a1e6"],  # yellow 5
        ["#00a3cc", "#00a3cc"],  # blue 6
        ["#f2ce00", "#f2ce00"],  # magenta 7
        ["#7a5ccc", "#7a5ccc"],  # cyan 8
        ]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    font="Ubuntu Mono derivative Powerline Bold",
    fontsize=12,
    padding=6,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = colors[8],
                    background = colors[8],
                    ),
                widget.Image(
                       filename = "~/.config/qtile/icons/python-white.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)}
                       ),
                widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 10,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[7],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
                widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
                widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                       ),
                widget.CurrentLayout(
                       foreground = colors[5],
                       background = colors[0],
                       padding = 5
                       ),
                widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
                widget.WindowName(
                       foreground = colors[4],
                       background = colors[0],
                       padding = 0
                       ),
                widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = colors[8],
                    background = colors[8],
                    ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = colors[3],
                       padding = 0,
                       fontsize = 30
                       ),
                widget.ThermalSensor(
                       foreground = colors[1],
                       background = colors[4],
                       threshold = 90,
                       fmt = 'Temp: {}',
                       padding = 5
                       ),
                widget.Volume(
                       foreground = colors[1],
                       background = colors[7],
                       fmt = 'Vol: {}',
                       padding = 5
                       ),
                widget.Clock(
                       foreground = colors[0],
                       background = colors[6],
                       format = "%A, %B %d,%Y %H:%M"
                       ),
                widget.QuickExit(),
            ],
            24,
            opacity=1.0,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
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
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
