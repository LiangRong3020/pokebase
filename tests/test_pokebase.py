#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

import pokebase as pb


class TestNamedAPIResource(unittest.TestCase):

    def setUp(self):
        self.berry = pb.berry('cheri')
        self.evolution_chain = pb.evolution_chain(7)

    def testResourceType(self):
        self.assertEqual(self.berry.resource_type, 'berry')
        self.assertEqual(self.evolution_chain.resource_type, 'evolution-chain')

    def testSimpleAttr(self):
        self.assertEqual(self.berry.name, 'cheri')
        self.assertEqual(self.berry.size, 20)
        self.assertFalse(self.evolution_chain.chain.is_baby)
        self.assertIsInstance(self.berry.flavors, list)

    def testComplexAttr(self):
        self.assertIsInstance(self.berry.item, pb.NamedAPIResource)

    def testMetadataAttr(self):
        self.assertIsInstance(self.berry.flavors[0], pb.APIMetadata)

    def testNoneAttr(self):
        self.assertIsNone(self.evolution_chain.baby_trigger_item)


class TestAPIResourceList(unittest.TestCase):

    def setUp(self):
        self.berries = pb.APIResourceList('berry')
        self.contestEffects = pb.APIResourceList('contest-effect')

    def testCount(self):
        self.assertEqual(len(self.berries), 64)
        self.assertEqual(len(self.contestEffects), 33)

    def testIDConversion(self):
        self.assertEqual(self.berries.id_to_name(8), 'persim')
        self.assertEqual(self.contestEffects.id_to_name(3), '3')


class TestAPIMetadata(unittest.TestCase):

    def setUp(self):
        b = pb.berry_firmness('very-soft')
        self.name = b.names[0]

    def testSimpleAttr(self):
        self.assertEqual(self.name.name, 'Très tendre')


if __name__ == '__main__':
    unittest.main()
