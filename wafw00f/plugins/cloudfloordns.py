#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloudfloor Application Firewall (Cloudfloor DNS)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'CloudfloorDNS(.WAF)?')),
        self.matchContent(r'<title>CloudfloorDNS.+?Web.Application.Firewall.Error'),
        self.matchContent(r'www\.cloudfloordns\.com/contact')
    ]
    if any(i for i in schemes):
        return True
    return False