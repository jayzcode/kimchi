#
# Project Kimchi
#
# Copyright IBM, Corp. 2013
#
# Authors:
#  Aline Manera <alinefm@linux.vnet.ibm.com>
#  Shu Ming <shuming@linux.vnet.ibm.com>
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

from kimchi.control.base import Collection, Resource
from kimchi.control.utils import UrlSubNode


@UrlSubNode("tasks", True)
class Tasks(Collection):
    def __init__(self, model):
        super(Tasks, self).__init__(model)
        self.resource = Task


class Task(Resource):
    def __init__(self, model, id):
        super(Task, self).__init__(model, id)

    @property
    def data(self):
        return {'id': self.ident,
                'status': self.info['status'],
                'message': self.info['message']}
