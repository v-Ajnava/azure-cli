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
        g.custom_command('delete', 'cli_namespace_delete')


    with self.command_group('servicebus namespace authorizationrule', sb_namespace_util) as g:
        g.custom_command('create', 'cli_namespaceautho_create')
        g.custom_command('get', 'cli_namespaceautho_get')
        g.custom_command('list', 'cli_namespaceautho_list')
        g.custom_command('listkeys', 'cli_namespaceautho_listkeys')
        g.custom_command('regeneratekeys', 'cli_namespaceautho_regeneratekey')
        g.custom_command('delete', 'cli_namespaceautho_delete')

# Queue Region

    with self.command_group('servicebus queue', sb_queue_util) as g:
        g.custom_command('create', 'cli_sbqueue_create')
        g.custom_command('get', 'cli_sbqueue_get')
        g.custom_command('list', 'cli_sbbqueue_list')
        g.custom_command('delete', 'cli_sbqueue_delete')


    with self.command_group('servicebus queue authorizationrule', sb_queue_util) as g:
        g.custom_command('create', 'cli_sbqueueautho_create')
        g.custom_command('get', 'cli_sbqueueautho_get')
        g.custom_command('list', 'cli_sbqueueautho_list')
        g.custom_command('listkeys', 'cli_sbqueueautho_listkeys')
        g.custom_command('regeneratekeys', 'cli_sbqueueautho_regeneratekey')
        g.custom_command('delete', 'cli_sbqueueautho_delete')


# Topic Region

    with self.command_group('servicebus topic', sb_topic_util) as g:
        g.custom_command('create', 'cli_sbtopic_create')
        g.custom_command('get', 'cli_sbtopic_get')
        g.custom_command('list', 'cli_sbtopic_list')
        g.custom_command('delete', 'cli_sbtopic_delete')


    with self.command_group('servicebus topic authorizationrule', sb_topic_util) as g:
        g.custom_command('create', 'cli_sbtopicautho_create')
        g.custom_command('get', 'cli_sbtopicautho_get')
        g.custom_command('list', 'cli_sbtopicautho_list')
        g.custom_command('listkeys', 'cli_sbtopicautho_listkeys')
        g.custom_command('regeneratekeys', 'cli_sbtopicautho_regeneratekey')
        g.custom_command('delete', 'cli_sbtopicautho_delete')


# Subscription Region

    with self.command_group('servicebus subscription', sb_subscriptions_util) as g:
        g.custom_command('create', 'cli_sbsubscription_create')
        g.custom_command('get', 'cli_sbsubscription_get')
        g.custom_command('list', 'cli_sbsubscription_list')
        g.custom_command('delete', 'cli_sbsubscription_delete')
