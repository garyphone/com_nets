# Copyright 2013 Hewlett-Packard Development Company, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

# default setting, if you want to load some information in the end, 
# you will interact them by using these django structure setting.
# In my situation, the visualization part only shows the data in the website.
# But the structure I should keep them, so I use the identity.roles as a default setting,
# it does not play any roles.

from horizon import exceptions 
from horizon import forms      
from horizon import messages
from horizon import tables
from horizon.utils import memoized

from openstack_dashboard import api
from openstack_dashboard import policy

from openstack_dashboard.dashboards.identity.roles \
    import forms as project_forms
from openstack_dashboard.dashboards.identity.roles \
    import tables as project_tables


class IndexView(tables.DataTableView):
    table_class = project_tables.RolesTable
    template_name = 'project/visualization/index.html'
    page_title = _("Visualization")
