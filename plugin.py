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

    def updateplugin(self, irc, msg, args, repodir):
        """[<plugin name>|<all>]

        Do a git pull on a plugin directory. Specify plugin name or all for each.
        Ex: updateplugin GitPull OR updateplugin all
        """

        # make our "dict" of valid plugins/dictionaries
        plugindirs = conf.supybot.directories.plugins()[:]  # list of valid dirs.
        dirdict = {}  # dict for our output. key = PluginName, value = directory.
        for plugindir in plugindirs:  # for each "plugin" dir.
            dirfiles = os.listdir(plugindir)  # get a list of files in each dir.
            for dirfile in dirfiles:  # iterate over each dir.
                if os.path.isdir(os.path.join(plugindir, dirfile, '.git')):  # if they're directories
                    dirdict[dirfile] = os.path.join(plugindir, dirfile)  # add into the dict.
        # validate input.
        if repodir == "all":
            workdirs = [f for (f, v) in dirdict.items()]  # copy all keys
        elif repodir not in dirdict:
            irc.reply("ERROR: '{0}' is an invalid plugin. Valid: {1}".format(repodir, " | ".join(sorted(dirdict.keys()))))
            return
        else:  # this means its not all but repodir is in dirdict.
            workdirs = [repodir]  # we inject the single key into the list.
        # we're valid from here on.
        for workdir in workdirs:
            # we're valid from here on.
            cwd = dirdict[workdir]  # cwd has to be the dir (in the value)
            command = ["git", "pull"]
            # run the command.
            pipe = subprocess.Popen(command, shell=False, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (out, error) = pipe.communicate()
            return_code = pipe.wait()
            # check if command worked or not.
            if return_code == 0:  # command worked.
                outlines = out.split('\n')  # split on newlines into list.
                if len(outlines) > 6:  # more than six lines.
                    output = " ".join([i.strip() for i in outlines])  # make it all one line, separated by a space.
                    output = utils.str.normalizeWhitespace(output)  # have no doublespaces.
                    irc.reply("{0} :: {1}".format(workdir, output))
                else:  # less than six lines.
                    for outline in outlines:  # output each line.
                        if outline != '':  # don't output blank lines:
                            irc.reply("{0} :: {1}".format(workdir, outline.strip()))
            else:  # error.
                error = error.replace('\n', ' ')  # replace newlines to spaces.
                error = utils.str.normalizeWhitespace(error)  # make sure no doublespaces.
                irc.reply("ERROR :: {0} :: {1}".format(repodir, error))

    updateplugin = wrap(updateplugin, [('checkCapability', 'owner'), ('somethingWithoutSpaces')])

Class = GitPull


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
