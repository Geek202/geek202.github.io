+++
title = "server-launcher and server-restarter"
description = "A rust program that wraps a Minecraft server and automatically restarts it if it crashes."
slug = "server-launcher"
date = 2021-01-21

[extra]
links = [
    { type = "github", url = "https://github.com/Geek202/server-launcher" },
    { type = "github", url = "https://github.com/Geek202/server-restarter" },
]
tags = [ "Minecraft", "Fabric", "Mods", "Java", "Rust" ]
+++

When my Minecraft server kept crashing (tip: Raspberry Pi is not the best for running one), I decided to create a wrapper that could automatically restart the server for me.
The concept originally included support for Discord webhooks and a small mod that adds a command to safely restart the server, but I then expanded the mod to add support for things such as restarting based on a cron schedule, and adding a command to restart when there is no players online.
