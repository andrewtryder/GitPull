###
# Copyright (c) 2013, spline
# All rights reserved.
#
#
###
# my libs.
import subprocess
import os
# extra supybot libs.
import supybot.conf as conf
# supybot libs.
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('GitPull')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

class GitPull(callbacks.Plugin):
    """Add the help for "@plugin help GitPull" here
    This should describe *how* to use this plugin."""
    threaded = True

    def gitpull(self, irc, msg, args, repodir):
        """<plugin>

        Do a git pull on a plugin directory.
        """

        plugindirs = conf.supybot.directories.plugins()[:]
        dirdict = {}
        for plugindir in plugindirs:
            dirfiles = os.listdir(plugindir)
            for dirfile in dirfiles:
                if os.path.isdir(os.path.join(plugindir, dirfile)):
                    dirdict[dirfile] = os.path.join(plugindir, dirfile)

        # validate.
        if repodir not in dirdict:
            irc.reply("ERROR: '{0}' is an invalid plugin. Valid: {1}".format(repodir, " | ".join(sorted(dirdict.keys()))))
            return
        # we're valid from here on.
        pipe = subprocess.Popen(['git', 'pull'], shell=True, cwd=dirdict[repodir], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        (out, error) = pipe.communicate()
        return_code = pipe.wait()
        irc.reply("{0} :: {1}".format(out, error))

    gitpull = wrap(gitpull, [('checkCapability', 'admin'), ('somethingWithoutSpaces')])

Class = GitPull


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
