# Namespace Region
def cli_namespace_create(cmd, client, resource_group_name, namespace_name, location=None, tags=None, sku='Standard', capacity=None, is_auto_inflate_enabled=None, maximum_throughput_units=None, is_kafka_enabled=None, default_action=None):
    # from azure.mgmt.eventhub.models import EHNamespace, Sku
    EHNamespace = cmd.get_models('EHNamespace', ('azure.mgmt.eventhub', 'EventHub2018PreviewManagementClient'))
    Sku = cmd.get_models('Sku', ('azure.mgmt.eventhub', 'EventHub2018PreviewManagementClient'))
    client.create_or_update(
        resource_group_name=resource_group_name,
        namespace_name=namespace_name,
        parameters=EHNamespace(
            location=location,
            tags=tags,
            sku=Sku(name=sku, tier=sku, capacity=capacity),
            is_auto_inflate_enabled=is_auto_inflate_enabled,
            maximum_throughput_units=maximum_throughput_units,
            kafka_enabled=is_kafka_enabled)).result()

    if default_action:
        netwrokruleset = client.get_network_rule_set(resource_group_name, namespace_name)
        netwrokruleset.default_action = default_action

    client.create_or_update_network_rule_set(resource_group_name, namespace_name, netwrokruleset)

    return client.get(resource_group_name, namespace_name)


def cli_namespace_update(cmd, client, instance, tags=None, sku=None, capacity=None, is_auto_inflate_enabled=None, maximum_throughput_units=None, is_kafka_enabled=None, default_action=None):

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

    if default_action:
        resourcegroup = instance.id.split('/')[4]
        netwrokruleset = client.get_network_rule_set(resourcegroup, instance.name)
        netwrokruleset.default_action = default_action
        client.create_or_update_network_rule_set(resourcegroup, instance.name, netwrokruleset)

    return instance


def cli_namespace_list(cmd, client, resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)

    return client.list()
