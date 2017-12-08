# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# AZURE CLI VM TEST DEFINITIONS
import json
import os
import platform
import tempfile
import time
import unittest
import mock
import uuid

import six

from knack.util import CLIError

from azure.cli.core.profiles import ResourceType
from azure.cli.testsdk import (
    ScenarioTest, ResourceGroupPreparer, LiveScenarioTest, api_version_constraint, StorageAccountPreparer)

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))

# pylint: disable=line-too-long
# pylint: disable=too-many-lines


class SBNamespaceCURDScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_sb_namespace')
    def test_sb_namespace(self, resource_group):

        self.kwargs.update({
            'loc': 'westus2',
            'namespacename': self.create_random_name(prefix='sb-nscli', length=20),
            'tags': {'tag1: value1', 'tag2: value2'},
            'sku': 'Standard',
            'tier': 'Standard',
            'authoname': self.create_random_name(prefix='cliAutho', length=20),
            'defaultauthorizationrule': 'RootManageSharedAccessKey',
            'accessrights': 'Send, Listen',
            'primary': 'PrimaryKey',
            'secondary': 'SecondaryKey'
        })

        # Create Namespace
        createnamespaceresult = self.cmd('servicebus namespace create --resource-group {rg} --namespace-name {namespacename} '
                          '--location {loc} --tags {tags} --sku-name {sku} --skutier {tier}',
                          checks=[self.check('sku.name', self.kwargs['sku'])]).output

        # Get Created Namespace
        getnamespaceresult = self.cmd('servicebus namespace get --resource-group {rg} --namespace-name {namespacename}',
                          checks=[self.check('sku.name', self.kwargs['sku'])]).output

        # Get Created Namespace list by ResourceGroup
        listnamespaceresult = self.cmd('servicebus namespace list').output
        self.assertGreater(len(listnamespaceresult), 0)

        # Create Authoriazation Rule
        # createauthorizationruleresult = self.cmd('servicebus namespace authorizationrule create --resource-group {rg} --namespace-name {namespacename} --name {authoname} --access-rights {accessrights}',
        createauthorizationruleresult = self.cmd('servicebus namespace authorizationrule create --resource-group {rg} --namespace-name {namespacename} --name {authoname}',
                          checks=[self.check('name', self.kwargs['authoname'])]).output

        # Get Create Authorization Rule
        getauthorizationruleresult = self.cmd(
            'servicebus namespace authorizationrule get --resource-group {rg} --namespace-name {namespacename} --name {authoname}',
            checks=[self.check('name', self.kwargs['authoname'])]).output

        # Get Default Authorization Rule
        getdefaultauthorizationruleresult = self.cmd(
            'servicebus namespace authorizationrule get --resource-group {rg} --namespace-name {namespacename} --name {defaultauthorizationrule}',
            checks=[self.check('name', self.kwargs['defaultauthorizationrule'])]).output

        # Get Authorization Rule Listkeys
        authorizationrulelistkeysresult = self.cmd(
            'servicebus namespace authorizationrule listkeys --resource-group {rg} --namespace-name {namespacename} --name {authoname}').output

        # Regeneratekeys - Primary
        regenrateprimarykeyresult = self.cmd(
            'servicebus namespace authorizationrule regeneratekeys --resource-group {rg} --namespace-name {namespacename} --name {authoname} --regeneratekey {primary}').output
        self.assertIsNotNone(regenrateprimarykeyresult)

        # Regeneratekeys - Secondary
        regenratesecondarykeyresult = self.cmd(
            'servicebus namespace authorizationrule regeneratekeys --resource-group {rg} --namespace-name {namespacename} --name {authoname} --regeneratekey {secondary}').output
        self.assertIsNotNone(regenratesecondarykeyresult)

        # Delete AuthorizationRule
        deleteauthorizationruleresult = self.cmd(
            'servicebus namespace authorizationrule delete --resource-group {rg} --namespace-name {namespacename} --name {authoname}').output

        # Delete Namespace list by ResourceGroup
        self.cmd('servicebus namespace delete --resource-group {rg} --namespace-name {namespacename}')



