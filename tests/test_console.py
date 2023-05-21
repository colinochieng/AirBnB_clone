#!/usr/bin/python3
"""
Test console
"""
import unittest
import sys
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class ConsoleTestCase(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        self.console.onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)  # Assuming the ID is a UUID

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        self.console.onecmd('show BaseModel 1234-1234-1234')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        self.console.onecmd('destroy BaseModel 1234-1234-1234')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        self.console.onecmd('create BaseModel')
        self.console.onecmd('update BaseModel 1234-1234-1234 name "New Name"')
        output = mock_stdout.getvalue().strip()
        self.assertIn("** no instance found **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        self.console.onecmd('create BaseModel')
        self.console.onecmd('create User')
        self.console.onecmd('all')
        output = mock_stdout.getvalue().strip()
        self.assertTrue('BaseModel' in output)
        self.assertTrue('User' in output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        self.console.onecmd('count User')
        output = mock_stdout.getvalue().strip()
        output = int(output)
        self.assertTrue(type(output))


if __name__ == '__main__':
    unittest.main()
