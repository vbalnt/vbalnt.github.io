+++
date = "2017-09-20"
draft = true
tags = ["vision"]
title = "Hubel and Wiesel and perception"
math = true
summary = """
Hubel and Wiesel
"""
+++

# Hubel and Wiesel and perception

<!-- Use your [favourite editor](https://www.gnu.org/software/emacs/) to -->
<!-- write a file with the following contents: -->

<!-- ```bash -->
<!-- #!/bin/sh -->
<!-- dmode_DP="$(cat /sys/class/drm/card0-DP-1/status)" -->
<!-- dmode_HDMI="$(cat /sys/class/drm/card0-HDMI-A-1/status)" -->
<!-- export DISPLAY=:0 -->
<!-- export XAUTHORITY=~/.Xauthority -->

<!-- if [ "${dmode_DP}" = connected ];then -->
<!-- 	/usr/bin/xrandr --output DP-1 --auto --right-of eDP-1 -->
<!-- elif [ "${dmode_HDMI}" = connected ];then -->
<!-- 	/usr/bin/xrandr --output HDMI-1 --auto --right-of eDP-1 -->
<!-- else /usr/bin/xrandr --auto -->
<!-- fi -->
<!-- ``` -->

<!-- where `eDP-1` is the main laptop screen, and `DP-1` and `HDMI-1` are -->
<!-- the laptop inputs (you probably have to rename the input names to your -->
<!-- config - you can find out the names by running `xrandr`). -->

<!-- Save the above file somewhere e.g. `~/.local/bin/screens.sh`. -->

<!-- Then in your `~/.config/i3/config` write somewhere the following line -->

<!-- ```bash -->
<!-- bindsym XF86Display exec --no-startup-id ~/.local/bin/screens.sh -->
<!-- ``` -->

<!-- to bind the above script to the `projector` key (in case your laptop -->
<!-- has a key like that). You can also set your own key binding. -->
