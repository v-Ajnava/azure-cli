# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.command_modules.servicebus._utils import skunameconverter, skutireconverter, accessrights_converter
from azure.mgmt.servicebus.models import ErrorResponseException

from azure.cli.core.commands.client_factory import get_subscription_id
from azure.mgmt.servicebus.models import (
    SBNamespace, SBSku, SBAuthorizationRule, SBQueue, SBTopic, SBSubscription)

from azure.mgmt.servicebus.models.service_bus_management_client_enums import SkuName, SkuTier, AccessRights, KeyType


# Namespace Region
def cli_namespace_create(client, resource_group_name, namespace_name, location, tags=None, sku='Standard', skutier=None):
    test11 = SBNamespace(location, tags, sku)
    result = client.create_or_update(resource_group_name, namespace_name, SBNamespace(location, tags,
                                                                                      SBSku(skunameconverter(sku),
                                                                                            skutireconverter(skutier)))).result()
    return result

def cli_namespace_list(client, resource_group_name=None, namespace_name=None):

    if(resource_group_name and namespace_name):
        result = client.get(resource_group_name, namespace_name)
        return result

    if(resource_group_name and not namespace_name):
        result = list(client.list_by_resource_group(resource_group_name, namespace_name))
        return result

    if (not resource_group_name and not namespace_name):
        result = list(client.list(resource_group_name, namespace_name))
        return result

def cli_namespace_delete(client, resource_group_name, namespace_name):
    try:
        client.delete(resource_group_name, namespace_name).result()
    except: ErrorResponseException


# Namespace Authorization rule:

def cli_namespaceautho_create(client, resource_group_name, namespace_name, name, accessrights=None):
    temp1 = ['Send', 'Listen']
    result = client.create_or_update_authorization_rule(resource_group_name, namespace_name, name,
                                                        accessrights_converter(temp1))
    return result

def cli_namespaceautho_get(client, resource_group_name, namespace_name, name):
    result = client.get_authorization_rule(resource_group_name, namespace_name, name)
    return result

def cli_namespaceautho_list(client, resource_group_name, name):
    result = client.list_authorization_rules(resource_group_name, name)
    return result

def cli_namespaceautho_listkeys(client, resource_group_name, namespace_name, name):
    result = client.list_keys(resource_group_name, namespace_name, name)
    return result

def cli_namespaceautho_regeneratekey(client, resource_group_name, namespace_name, name, regeneratekey):
    result = client.regenerate_keys(resource_group_name, namespace_name, name, regeneratekey)
    return result

def cli_namespaceautho_delete(client, resource_group_name, namespace_name, name):
    result = client.delete_authorization_rule(resource_group_name, namespace_name, name)
    return result


# Queue Region
def cli_sbqueue_create(client, resource_group_name, namespace_name, name, queue_params=None):
    if (not queue_params):
        queue_params = SBQueue()
        result = client.create_or_update(resource_group_name, namespace_name, name, queue_params)
        return result

def cli_sbbqueue_list(client, resource_group_name, namespace_name, name=None):
    if (name):
        result = client.get(resource_group_name, namespace_name, name)
        return result

    if (not name):
        result = list(client.list_by_namespace(resource_group_name, namespace_name))
        return result

def cli_sbqueue_get(client, resource_group_name, namespace_name, name):
    result = client.get(resource_group_name, namespace_name, name)
    return result

def cli_sbqueueautho_create(client, resource_group_name, namespace_name, queue_name, name, accessrights=None):
    temp1 = ['Send', 'Listen']
    result = client.create_or_update_authorization_rule(resource_group_name, namespace_name, queue_name, name,
                                                            accessrights_converter(temp1))
    return result

def cli_sbqueueautho_get(client, resource_group_name, namespace_name, queue_name, name):
    result = client.get_authorization_rule(resource_group_name, namespace_name, queue_name, name)
    return result

def cli_sbqueueautho_list(client, resource_group_name, namespace_name):
    result = client.list_authorization_rules(resource_group_name, namespace_name)
    return result

def cli_sbqueueautho_listkeys(client, resource_group_name, namespace_name, queue_name, name):
    result = client.list_keys(resource_group_name, namespace_name, queue_name, name)
    return result

def cli_sbqueueautho_regeneratekey(client, resource_group_name, namespace_name, queue_name, name, regeneratekey):
    result = client.regenerate_keys(resource_group_name, namespace_name, queue_name, name, regeneratekey)
    return result

def cli_sbqueueautho_delete(client, resource_group_name, namespace_name, queue_name, name):
    result = client.delete_authorization_rule(resource_group_name, namespace_name, queue_name, name)
    return result

def cli_sbqueue_delete(client, resource_group_name, namespace_name, name):
    result = client.delete(resource_group_name, namespace_name, name)
    return result


# Topic Region
def cli_sbtopic_create(client, resource_group_name, namespace_name, name, topic_params=None):
    if (not topic_params):
        topic_params = SBTopic()
        result = client.create_or_update(resource_group_name, namespace_name, name, topic_params)
        return result

def cli_sbtopic_list(client, resource_group_name, namespace_name, name=None):
    if (name):
        result = client.get(resource_group_name, namespace_name, name)
        return result

    if (not name):
        result = list(client.list_by_namespace(resource_group_name, namespace_name))
        return result

def cli_sbtopic_get(client, resource_group_name, namespace_name, name):
    result = client.get(resource_group_name, namespace_name, name)
    return result

def cli_sbtopicautho_create(client, resource_group_name, namespace_name, topic_name, name, accessrights=None):
    temp1 = ['Send', 'Listen']
    result = client.create_or_update_authorization_rule(resource_group_name, namespace_name, topic_name, name,
                                                            accessrights_converter(temp1))
    return result

def cli_sbtopicautho_get(client, resource_group_name, namespace_name, topic_name, name):
    result = client.get_authorization_rule(resource_group_name, namespace_name, topic_name, name)
    return result

def cli_sbtopicautho_list(client, resource_group_name, namespace_name):
    result = client.list_authorization_rules(resource_group_name, namespace_name)
    return result

def cli_sbtopicautho_listkeys(client, resource_group_name, namespace_name, topic_name, name):
    result = client.list_keys(resource_group_name, namespace_name, topic_name, name)
    return result

def cli_sbtopicautho_regeneratekey(client, resource_group_name, namespace_name, topic_name, name, regeneratekey):
    result = client.regenerate_keys(resource_group_name, namespace_name, topic_name, name, regeneratekey)
    return result

def cli_sbtopicautho_delete(client, resource_group_name, namespace_name, topic_name, name):
    result = client.delete_authorization_rule(resource_group_name, namespace_name, topic_name, name)
    return result

def cli_sbtopic_delete(client, resource_group_name, namespace_name, name):
    result = client.delete(resource_group_name, namespace_name, name)
    return result


# Subscription Region
def cli_sbsubscription_create(client, resource_group_name, namespace_name, topic_name, name, lock_duration=None, requires_session=None, default_message_time_to_live=None, dead_lettering_on_message_expiration=None, duplicate_detection_history_time_window=None, max_delivery_count=None, status=None, enable_batched_operations=None, auto_delete_on_idle=None, forward_to=None, forward_dead_lettered_messages_to=None):
        subscription_params = SBSubscription(
            lock_duration=lock_duration,
            requires_session=requires_session,
            default_message_time_to_live=default_message_time_to_live,
            dead_lettering_on_message_expiration=dead_lettering_on_message_expiration,
            duplicate_detection_history_time_window=duplicate_detection_history_time_window,
            max_delivery_count=max_delivery_count,
            status=status,
            enable_batched_operations=enable_batched_operations,
            auto_delete_on_idle=auto_delete_on_idle,
            forward_to=forward_to,
            forward_dead_lettered_messages_to=forward_dead_lettered_messages_to
        )
        result = client.create_or_update(resource_group_name, namespace_name, topic_name, name, subscription_params)
        return result

def cli_sbsubscription_list(client, resource_group_name, namespace_name, topic_name, name=None):
    if (name):
        result = client.get(resource_group_name, namespace_name, topic_name, name)
        return result

    if (not name):
        result = list(client.list_by_topic(resource_group_name, namespace_name, topic_name))
        return result

def cli_sbsubscription_get(client, resource_group_name, namespace_name, topic_name, name):
    result = client.get(resource_group_name, namespace_name, topic_name, name)
    return result

def cli_sbsubscription_delete(client, resource_group_name, namespace_name, topic_name, name):
    result = client.delete(resource_group_name, namespace_name, topic_name, name)
    return result
