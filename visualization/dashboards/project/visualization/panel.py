# based on django structure in the OpenStack dashboard 
from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.api import keystone


class Visualization(horizon.Panel): #change the name
    name = _("Visualization") #required, name shows the panel name in dashboard
    slug = 'visualization' #required
