"""
Generic fixer for playing with and learning about creating lib2to3 fixers
"""

from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import Node, Leaf


class FixFixerGeneric(BaseFix):

    def match(self, node):
        print repr(node)
        print node.type
        print
        # Return True if you want to apply transformations
        return False

    def transform(self, node, results):
        # Make transformations to the node here. If a transformation happened, call node.changed
        pass
