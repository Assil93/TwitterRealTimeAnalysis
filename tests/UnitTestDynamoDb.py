import unittest
from TwitterAPI import TwitterAPI
import boto3
import json
import ast
import decimal
import base64
import time
from sys import getsizeof


"""Test case utilisé pour tester les fonctions du module 'random'."""
# Helper class to convert a DynamoDB item to JSON.

def test_hashtags():
    """Test le fonctionnement de la table hashtags."""
    dynamodbA = boto3.resource(service_name='dynamodb', region_name='us-west-2')
    tableA = dynamodbA.Table('hashtags')
    responseA = tableA.scan()
    for recordA in responseA['dada']:
        testTableA = recordA['hashtag']
    assert (getsizeof(testTableA) > 0)

def test_fullName():
    """Test le fonctionnement de la table fullName."""
    dynamodbB = boto3.resource(service_name='dynamodb', region_name='us-west-2')
    tableB = dynamodbB.Table('bb')
    responseB = tableB.scan()
    for recordB in responseB['Items']:
        testTableB = recordB['full_name']
    assert (getsizeof(testTableB) > 0)