#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `TwitterRealTimeAnalysis` package."""
import unittest
from TwitterAPI import TwitterAPI
import boto3
import json
import ast
import decimal
import base64
import time
from sys import getsizeof
import pytest

from click.testing import CliRunner

from TwitterRealTimeAnalysis import TwitterRealTimeAnalysis
from TwitterRealTimeAnalysis import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'TwitterRealTimeAnalysis.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

def test_table_hashtags():
    """Test le fonctionnement de la table hashtags."""
    dynamodbA = boto3.resource(service_name='dynamodb', region_name='us-west-2')
    tableA = dynamodbA.Table('hashtags')
    responseA = tableA.scan()
    for recordA in responseA['Items']:
        testTableA = recordA['hashtag']
    assert (getsizeof(testTableA) > 0)

def test_table_fullName():
    """Test le fonctionnement de la table fullName."""
    dynamodbB = boto3.resource(service_name='dynamodb', region_name='us-west-2')
    tableB = dynamodbB.Table('full_name')
    responseB = tableB.scan()
    for recordB in responseB['Items']:
        testTableB = recordB['full_name']
    assert (getsizeof(testTableB) > 0)