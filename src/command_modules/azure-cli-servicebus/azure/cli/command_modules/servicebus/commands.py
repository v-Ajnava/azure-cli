# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.sdk.util import CliCommandType
from azure.cli.command_modules.servicebus._client_factory import (namespaces_mgmt_client_factory, queues_mgmt_client_factory, topics_mgmt_client_factory, subscriptions_mgmt_client_factory, rules_mgmt_client_factory, regions_mgmt_client_factory, premium_messaging_mgmt_client_factory, disaster_recovery_mgmt_client_factory, event_subscriptions_mgmt_client_factory, event_hubs_mgmt_client_factory)
# from ._exception_handler import billing_exception_handler


def load_command_table(self, _):
    sb_namespace_util = CliCommandType(
        operations_tmpl='azure.mgmt.servicebus.operations.namespaces_operations#NamespacesOperations.{}',
        client_factory=namespaces_mgmt_client_factory
    )

    sb_queue_util = CliCommandType(
        operations_tmpl='azure.mgmt.servicebus.operations.queues_operations#QueuesOperations.{}',
        client_factory=queues_mgmt_client_factory
    )

    sb_topic_util = CliCommandType(
        operations_tmpl='azure.mgmt.servicebus.operations.topics_operations#TopicsOperations.{}',
        client_factory=topics_mgmt_client_factory
    )

    sb_subscriptions_util = CliCommandType(
        operations_tmpl='azure.mgmt.servicebus.operations.subscriptions_operations#SubscriptionsOperations.{}',
        client_factory=subscriptions_mgmt_client_factory
    )

# Namespace Region
    with self.command_group('servicebus namespace', sb_namespace_util) as g:
        g.custom_command('create', 'cli_namespace_create')
        g.command('get', 'get')
        g.custom_command('list', 'cli_namespace_list')
        g.command('delete', 'delete')


    with self.command_group('servicebus namespace authorizationrule', sb_namespace_util) as g:
        g.custom_command('create', 'cli_namespaceautho_create')
        g.command('get', 'get_authorization_rule')
        g.command('list', 'list_authorization_rules')
        g.command('listkeys', 'list_keys')
        g.custom_command('regeneratekeys', 'cli_namespaceautho_regeneratekey')
        g.command('delete', 'delete_authorization_rule')

# Queue Region

    with self.command_group('servicebus queue', sb_queue_util) as g:
        g.custom_command('create', 'cli_sbqueue_create')
        g.command('get', 'get')
        g.command('list', 'list_by_namespace')
        g.command('delete', 'delete')


    with self.command_group('servicebus queue authorizationrule', sb_queue_util) as g:
        g.custom_command('create', 'cli_sbqueueautho_create')
        g.command('get', 'get_authorization_rule')
        g.command('list', 'list_authorization_rules')
        g.command('listkeys', 'list_keys')
        g.custom_command('regeneratekeys', 'cli_sbqueueautho_regeneratekey')
        g.command('delete', 'delete_authorization_rule')


# Topic Region

    with self.command_group('servicebus topic', sb_topic_util) as g:
        g.custom_command('create', 'cli_sbtopic_create')
        g.command('get', 'get')
        g.command('list', 'list_by_namespace')
        g.command('delete', 'delete')


    with self.command_group('servicebus topic authorizationrule', sb_topic_util) as g:
        g.custom_command('create', 'cli_sbtopicautho_create')
        g.command('get', 'get_authorization_rule')
        g.command('list', 'list_authorization_rules')
        g.command('listkeys', 'list_keys')
        g.custom_command('regeneratekeys', 'cli_sbtopicautho_regeneratekey')
        g.command('delete', 'delete_authorization_rule')


# Subscription Region

    with self.command_group('servicebus subscription', sb_subscriptions_util) as g:
        g.custom_command('create', 'cli_sbsubscription_create')
        g.command('get', 'get')
        g.command('list', 'list_by_topic')
        g.command('delete', 'delete')
