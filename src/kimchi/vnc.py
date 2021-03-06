#!/usr/bin/python
#
# Project Kimchi
#
# Copyright IBM, Corp. 2013
#
# Authors:
#  Adam Litke <agl@linux.vnet.ibm.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import errno
import os
import subprocess


from kimchi.config import config


WS_TOKENS_DIR = '/var/lib/kimchi/vnc-tokens'


def new_ws_proxy():
    try:
        os.makedirs(WS_TOKENS_DIR, mode=0755)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass

    cmd = os.path.join(os.path.dirname(__file__), 'websockify.py')
    args = ['python', cmd, config.get('display', 'display_proxy_port'),
            '--target-config', WS_TOKENS_DIR]
    p = subprocess.Popen(args, close_fds=True)
    return p


def add_proxy_token(name, port):
    with open(os.path.join(WS_TOKENS_DIR, name), 'w') as f:
        f.write('%s: localhost:%s' % (name.encode('utf-8'), port))


def remove_proxy_token(name):
    try:
        os.unlink(os.path.join(WS_TOKENS_DIR, name))
    except OSError:
        pass
