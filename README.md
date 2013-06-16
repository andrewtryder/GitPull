Supybot-GitPull
===============

Supybot plugin to keep other plugins updated and in-sync via Git.

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
