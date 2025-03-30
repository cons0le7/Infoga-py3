#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Infoga: Email Information Gathering
#
# @url: https://github.com/m4ll0k/Infoga
# @author: Momo Outaadi (M4ll0k)
#
# Infoga is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation version 3 of the License.
#
# Infoga is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Infoga; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import http.client
import requests
import urllib.request

class http:
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"
    
    def httplib(self, server, query, cookie=None):
        try:
            con = http.client.HTTPConnection(server)
            con.request('GET', query, headers={
                "Host": server,
                "User-agent": self.user_agent,
                "Cookie": cookie
            } if cookie else {
                "Host": server,
                "User-agent": self.user_agent
            })

            response = con.getresponse()
            return response.read()
        except Exception as error:
            return error

    def request(self, url):
        try:
            req = requests.get(url)
            return req.content
        except Exception as error:
            return error

    def urllib(self, url, payload, headers={"User-agent": user_agent}):
        try:
            con = urllib.request.Request(url, payload.encode('utf-8'), headers)
            return urllib.request.urlopen(con).read()
        except Exception as error:
            return error