[![Build Status](https://travis-ci.org/reticulatingspline/GitPull.svg?branch=master)](https://travis-ci.org/reticulatingspline/GitPull)

# Limnoria plugin for updating my plugins

## Introduction

For the great plugin, PluginDownloader, many people keep all plugins in their GitHub "Supybot-Plugins" repo. I
spread mine out individually so people have no problem running n+1. Updating is also easy as I push to each
individual repo, so you're not grabbing 12 plugins when you only want one.

However, I run two other bots to my main one and I hate to SSH in when I push a simple upgrade, once tested, to
other production bots. I can /msg <bot> reload Plugin, but it must be updated already via a 'git pull' on the shell.

This solves that issue.

The plugin is restricted to being run by the owner. Obviously, 'git pull' can be destructive because you are overwriting
files. If any of this is a problem, don't run it.

Otherwise, it solves the need to login via the 'upgradeplugin' command. It checks the "directories" of plugins and then
does the equivilent of `cd ~/supybot/plugins/PluginName; git pull` and outputs the result. The same command could be run
on this plugin via /msg <bot> upgradeplugin GitPull

NOTE: If you "download" plugins, where the .git directory inside is removed, this will obviously not work. You must have
a structure like I have, one repo per plugin, for this plugin to be of any use and work.

## Install

You will need a working Limnoria bot on Python 2.7 for this to work.

Go into your Limnoria plugin dir, usually ~/supybot/plugins and run:

```
git clone https://github.com/reticulatingspline/GitPull
```

To install additional requirements, run:

```
pip install -r requirements.txt 
```

or if you don't have or don't want to use root, 

```
pip install -r requirements.txt --user
```

Next, load the plugin:

```
/msg bot load GitPull
```

You must be an owner on the bot to run the updateplugin command.

## Example Usage

```
<spline> @updateplugin all
<spline> @updateplugin Git Pull
```

## About

All of my plugins are free and open source. When I first started out, one of the main reasons I was
able to learn was due to other code out there. If you find a bug or would like an improvement, feel
free to give me a message on IRC or fork and submit a pull request. Many hours do go into each plugin,
so, if you're feeling generous, I do accept donations via Amazon or browse my [wish list](http://amzn.com/w/380JKXY7P5IKE).

I'm always looking for work, so if you are in need of a custom feature, plugin or something bigger, contact me via GitHub or IRC.