###
# Copyright (c) 2013-2014, spline
# All rights reserved.
#
#
###

from supybot.test import *

class GitPullTestCase(PluginTestCase):
    plugins = ('GitPull',)
    
    def testGitPull(self):
        self.assertResponse('updateplugin GitPull', 'GitPull :: Already up-to-date.')
    


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
