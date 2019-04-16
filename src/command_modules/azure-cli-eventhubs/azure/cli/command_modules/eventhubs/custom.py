# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=inconsistent-return-statements


# Namespace Region
def cli_namespace_create(client, resource_group_name, namespace_name, location=None, tags=None, sku='Standard', capacity=None, is_auto_inflate_enabled=None, maximum_throughput_units=None, is_kafka_enabled=None):
    from azure.mgmt.eventhub.models import EHNamespace, Sku
    return client.create_or_update(
        resource_group_name=resource_group_name,
        namespace_name=namespace_name,
        parameters=EHNamespace(
            location=location,
            tags=tags,
            sku=Sku(name=sku, tier=sku, capacity=capacity),
            is_auto_inflate_enabled=is_auto_inflate_enabled,
            maximum_throughput_units=maximum_throughput_units,
            kafka_enabled=is_kafka_enabled))


def cli_namespace_update(instance, tags=None, sku=None, capacity=None, is_auto_inflate_enabled=None, maximum_throughput_units=None, is_kafka_enabled=None):

    if tags:
        instance.tags = tags

    if sku:
        instance.sku.name = sku
        instance.sku.tier = sku

    if capacity:
        instance.sku.capacity = capacity

    if is_auto_inflate_enabled:
        instance.is_auto_inflate_enabled = is_auto_inflate_enabled

    if maximum_throughput_units:
        instance.maximum_throughput_units = maximum_throughput_units

    if is_kafka_enabled:
        instance.kafka_enabled = is_kafka_enabled

    return instance


def cli_namespace_list(client, resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)

    return client.list()


# Namespace Authorization rule:
def cli_autho_update(instance, rights):
    from azure.cli.command_modules.eventhubs._utils import accessrights_converter
    instance.rights = accessrights_converter(rights)
    return instance


# Eventhub Region
def cli_eheventhub_create(client, resource_group_name, namespace_name, event_hub_name, message_retention_in_days=None, partition_count=None, status=None,
                          enabled=None, skip_empty_archives=None, capture_interval_seconds=None, capture_size_limit_bytes=None, destination_name=None, storage_account_resource_id=None, blob_container=None, archive_name_format=None):
    from azure.mgmt.eventhub.models import Eventhub, CaptureDescription, Destination, EncodingCaptureDescription
    eventhubparameter1 = Eventhub()
    if message_retention_in_days:
        eventhubparameter1.message_retention_in_days = message_retention_in_days

    if partition_count:
        eventhubparameter1.partition_count = partition_count

    if status:
        eventhubparameter1.status = status

    if enabled and enabled is True:
        eventhubparameter1.capture_description = CaptureDescription(
            enabled=enabled,
            skip_empty_archives=skip_empty_archives,
            encoding=EncodingCaptureDescription.avro,
            interval_in_seconds=capture_interval_seconds,
            size_limit_in_bytes=capture_size_limit_bytes,
            destination=Destination(
                name=destination_name,
                storage_account_resource_id=storage_account_resource_id,
                blob_container=blob_container,
                archive_name_format=archive_name_format)
        )
    return client.create_or_update(
        resource_group_name=resource_group_name,
        namespace_name=namespace_name,
        event_hub_name=event_hub_name,
        parameters=eventhubparameter1)


def cli_eheventhub_update(instance, message_retention_in_days=None, partition_count=None, status=None,
                          enabled=None, skip_empty_archives=None, capture_interval_seconds=None,
                          capture_size_limit_bytes=None, destination_name=None, storage_account_resource_id=None,
                          blob_container=None, archive_name_format=None):
    from azure.mgmt.eventhub.models import CaptureDescription, Destination, EncodingCaptureDescription

    if message_retention_in_days:
        instance.message_retention_in_days = message_retention_in_days

    if partition_count:
        instance.partition_count = partition_count

    if status:
        instance.status = status

    if enabled and not instance.capture_description:
        instance.capture_description = CaptureDescription()
        instance.capture_description.destination = Destination()
        instance.capture_description.encoding = EncodingCaptureDescription.avro
        instance.capture_description.enabled = enabled

    if enabled and instance.capture_description:
        instance.capture_description.enabled = enabled
        if capture_interval_seconds:
            instance.interval_in_seconds = capture_interval_seconds
        if capture_size_limit_bytes:
            instance.size_limit_in_bytes = capture_size_limit_bytes
        if destination_name:
            instance.capture_description.destination.name = destination_name
        if storage_account_resource_id:
            instance.capture_description.destination.storage_account_resource_id = storage_account_resource_id
        if blob_container:
            instance.capture_description.destination.blob_container = blob_container
        if archive_name_format:
            instance.capture_description.destination.archive_name_format = archive_name_format
        if skip_empty_archives:
            instance.capture_description.skip_empty_archives = skip_empty_archives

    return instance


# NetwrokRuleSet Region
def cli_networkruleset_createupdate(client, resource_group_name, namespace_name, default_action="Deny"):
    netwrokruleset = client.get_network_rule_set(resource_group_name, namespace_name)
    netwrokruleset.default_action = default_action
    client.create_or_update_network_rule_set(resource_group_name, namespace_name, netwrokruleset)


def cli_networkruleset_delete(client, resource_group_name, namespace_name):
    from azure.mgmt.eventhub.v2017_04_01.models import NWRuleSetVirtualNetworkRules, NWRuleSetIpRules, NetworkRuleSet
    netwrokruleset = NetworkRuleSet()
    netwrokruleset.ip_rules = [NWRuleSetIpRules]
    netwrokruleset.virtual_network_rules = [NWRuleSetVirtualNetworkRules]
    client.create_or_update_network_rule_set(resource_group_name, namespace_name, netwrokruleset)


def cli_virtualnetwrokrule_add(client, resource_group_name, namespace_name, subnet, ignore_missing_vnet_service_endpoint=None):
    from azure.mgmt.eventhub.v2017_04_01.models import NWRuleSetVirtualNetworkRules, NetworkRuleSet, Subnet

    netwrokruleset = NetworkRuleSet()
    netwrokruleset.ip_rules = []
    netwrokruleset.virtual_network_rules = []

    if ignore_missing_vnet_service_endpoint is None:
        ignore_missing_vnet_service_endpoint = False

    netwrokruleset = client.get_network_rule_set(resource_group_name, namespace_name)
    netwrokruleset.virtual_network_rules.append(NWRuleSetVirtualNetworkRules(subnet=Subnet(id=subnet), ignore_missing_vnet_service_endpoint=ignore_missing_vnet_service_endpoint))
    client.create_or_update_network_rule_set(resource_group_name, namespace_name, netwrokruleset)


def cli_virtualnetwrokrule_list(client, resource_group_name, namespace_name):
    netwrokruleset = client.get_network_rule_set(resource_group_name, namespace_name)
    return netwrokruleset.virtual_network_rules


def cli_virtualnetwrokrule_delete(client, resource_group_name, namespace_name, subnet, ignore_missing_vnet_service_endpoint=None):
    from azure.mgmt.eventhub.v2017_04_01.models import NWRuleSetVirtualNetworkRules
    if ignore_missing_vnet_service_endpoint is None:
        ignore_missing_vnet_service_endpoint = False

    netwrokruleset = client.get_network_rule_set(resource_group_name=resource_group_name, namespace_name=namespace_name)
    virtualnetworkrule = NWRuleSetVirtualNetworkRules()
    virtualnetworkrule.subnet = subnet
    virtualnetworkrule.ignore_missing_vnet_service_endpoint = ignore_missing_vnet_service_endpoint

    for vnetruletodelete in netwrokruleset.virtual_network_rules:
        if vnetruletodelete.subnet.id == subnet:
            netwrokruleset.virtual_network_rules.remove(vnetruletodelete)

    client.create_or_update_network_rule_set(resource_group_name, namespace_name, netwrokruleset)


def cli_iprule_add(client, resource_group_name, namespace_name, ip_mask, action=None):
    from azure.mgmt.eventhub.v2017_04_01.models import NWRuleSetIpRules

    if ip_mask is None:
        ip_mask = ""
    if action is None:
        action = "Allow"

    netwrokruleset = client.get_network_rule_set(resource_group_name, namespace_name)
    netwrokruleset.ip_rules.append(NWRuleSetIpRules(ip_mask=ip_mask, action="Allow"))

    client.create_or_update_network_rule_set(resource_group_name, namespace_name, netwrokruleset)
    netwrokruleset = client.get_network_rule_set(resource_group_name, namespace_name)
    return netwrokruleset.ip_rules


def cli_iprule_list(client, resource_group_name, namespace_name):
    netwrokruleset = client.get_network_rule_set(resource_group_name, namespace_name)
    return netwrokruleset.ip_rules


def cli_iprule_delete(client, resource_group_name, namespace_name, ip_mask):
    from azure.mgmt.eventhub.v2017_04_01.models import NWRuleSetIpRules

    getnetworkruleset = client.get_network_rule_set(resource_group_name, namespace_name)
    ipruletodelete = NWRuleSetIpRules()
    ipruletodelete.ip_mask = ip_mask
    ipruletodelete.action = "Allow"

    if ipruletodelete in getnetworkruleset.ip_rules:
        getnetworkruleset.ip_rules.remove(ipruletodelete)

    client.create_or_update_network_rule_set(resource_group_name, namespace_name, getnetworkruleset)
