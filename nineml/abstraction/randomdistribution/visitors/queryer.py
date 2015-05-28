"""
Definitions for the ComponentQuery Class

:copyright: Copyright 2010-2013 by the Python lib9ML team, see AUTHORS.
:license: BSD-3, see LICENSE for details.
"""

from itertools import chain
from ...componentclass.visitors.queryer import ComponentQueryer


class RandomDistributionQueryer(ComponentQueryer):

    """
    RandomDistributionQueryer provides a way of adding methods to query a
    ComponentClass object, without polluting the class
    """

    def __init__(self, component_class):
        """Constructor for the RandomDistributionQueryer"""
        self.component_class = component_class

    @property
    def ports(self):
        """Return an iterator over all the port (Event & Analog) in the
        component_class"""
        # TODO: RandomDistribution-specific ports to go here
        return chain(super(RandomDistributionQueryer, self).ports, [])
