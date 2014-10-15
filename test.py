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
    
    def testGitPullError(self):
        self.assertRegex('updateplugin HELLO2U', "ERROR: \'HELLO\' is an invalid plugin")
    


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
