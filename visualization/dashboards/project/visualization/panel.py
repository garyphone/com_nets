from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.api import keystone


class Visualization(horizon.Panel): #change the name
    name = _("Visualization") #required
    slug = 'visualization' #required
