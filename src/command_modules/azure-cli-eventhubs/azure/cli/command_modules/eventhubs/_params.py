# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import tags_type, get_enum_type, resource_group_name_type, name_type, get_location_type, get_three_state_flag, get_resource_name_completion_list
from azure.cli.core.commands.validators import get_default_location_from_resource_group


# pylint: disable=line-too-long
def load_arguments_eh(self, _):
    from knack.arguments import CLIArgumentType
    from azure.mgmt.eventhub.models.event_hub_management_client_enums import KeyType, AccessRights, SkuName
    from azure.cli.command_modules.eventhubs._completers import get_consumergroup_command_completion_list, get_eventhubs_command_completion_list
    from azure.cli.command_modules.eventhubs._validator import validate_storageaccount

    rights_arg_type = CLIArgumentType(options_list=['--rights'], nargs='+', arg_type=get_enum_type(AccessRights), help='Space-separated Authorization rule rights list')
    key_arg_type = CLIArgumentType(options_list=['--key-name'], arg_type=get_enum_type(KeyType), help='specifies Primary or Secondary key needs to be reset')
    event_hub_name_arg_type = CLIArgumentType(options_list=['--eventhub-name'], help='Name of EventHub')
    namespace_name_arg_type = CLIArgumentType(options_list=['--namespace-name'], help='Name of Namespace', id_part='name')

    with self.argument_context('eventhubs') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('namespace_name', id_part='name', help='name of Namespace')

    with self.argument_context('eventhubs namespace exists') as c:
        c.argument('namespace_name', arg_type=name_type, help='name of Namespace')

    with self.argument_context('eventhubs namespace') as c:
        c.argument('namespace_name', arg_type=name_type, id_part='name', completer=get_resource_name_completion_list('Microsoft.ServiceBus/namespaces'), help='Name of Namespace')

    with self.argument_context('eventhubs namespace create') as c:
        c.argument('tags', arg_type=tags_type)
        c.argument('sku', options_list=['--sku'], arg_type=get_enum_type(SkuName))
        c.argument('location', arg_type=get_location_type(self.cli_ctx), validator=get_default_location_from_resource_group)
        c.argument('capacity', type=int, help='Capacity for Sku')
        c.argument('is_auto_inflate_enabled', options_list=['--enable-auto-inflate'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether AutoInflate is enabled for eventhub namespace.')
        c.argument('maximum_throughput_units', type=int, help='Upper limit of throughput units when AutoInflate is enabled, vaule should be within 0 to 20 throughput units. ( 0 if AutoInflateEnabled = true)')

    with self.argument_context('eventhubs namespace update') as c:
        c.argument('tags', arg_type=tags_type)
        c.argument('sku', options_list=['--sku'], arg_type=get_enum_type(SkuName))
        c.argument('capacity', type=int, help='Capacity for Sku')
        c.argument('is_auto_inflate_enabled', options_list=['--enable-auto-inflate'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether AutoInflate is enabled for eventhub namespace.')
        c.argument('maximum_throughput_units', type=int, help='Upper limit of throughput units when AutoInflate is enabled, vaule should be within 0 to 20 throughput units. ( 0 if AutoInflateEnabled = true)')

    # region Namespace Authorizationrule
    with self.argument_context('eventhubs namespace authorization-rule list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    with self.argument_context('eventhubs namespace authorization-rule keys list') as c:
        c.argument('authorization_rule_name', arg_type=name_type, id_part=None, help='Name of Namespace AuthorizationRule')
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    for scope in ['eventhubs namespace authorization-rule', 'eventhubs namespace authorization-rule keys renew']:
        with self.argument_context(scope) as c:
            c.argument('authorization_rule_name', arg_type=name_type, id_part='child_name_1', help='Name of Namespace AuthorizationRule')
            c.argument('namespace_name', arg_type=namespace_name_arg_type)

    for scope in ['eventhubs namespace authorization-rule create', 'eventhubs namespace authorization-rule update', 'eventhubs eventhub authorization-rule create', 'eventhubs eventhub authorization-rule update']:
        with self.argument_context(scope) as c:
            c.argument('rights', arg_type=rights_arg_type)

    with self.argument_context('eventhubs namespace authorization-rule keys renew') as c:
        c.argument('key_type', arg_type=key_arg_type)


# region - Eventhub Create
    with self.argument_context('eventhubs eventhub') as c:
        c.argument('event_hub_name', arg_type=name_type, id_part='child_name_1', completer=get_eventhubs_command_completion_list, help='Name of Eventhub')

    for scope in ['eventhubs eventhub update', 'eventhubs eventhub create']:
        with self.argument_context(scope) as c:
            c.argument('message_retention_in_days', options_list=['--message-retention'], type=int, help='Number of days to retain events for this Event Hub, value should be 1 to 7 days')
            c.argument('partition_count', type=int, help='Number of partitions created for the Event Hub, allowed values are from 1 to 32 partitions.')
            c.argument('status', arg_type=get_enum_type(['Active', 'Disabled', 'SendDisabled', 'ReceiveDisabled']), help='Status of Eventhub')
            c.argument('enabled', options_list=['--enable-capture'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether capture description is enabled.')
            c.argument('capture_interval_seconds', arg_group='Capture', options_list=['--capture-interval'], type=int, help='Allows you to set the frequency with which the capture to Azure Blobs will happen, value should between 60 to 900 seconds')
            c.argument('capture_size_limit_bytes', arg_group='Capture', options_list=['--capture-size-limit'], type=int, help='Defines the amount of data built up in your Event Hub before an capture operation, value should be between 10485760 to 524288000 bytes')
            c.argument('destination_name', arg_group='Capture-Destination', help='Name for capture destination')
            c.argument('storage_account_resource_id', arg_group='Capture-Destination', validator=validate_storageaccount, options_list=['--storage-account'], help='Name (if within same resource group and not of type Classic Storage) or ARM id of the storage account to be used to create the blobs')
            c.argument('blob_container', arg_group='Capture-Destination', help='Blob container Name')
            c.argument('archive_name_format', arg_group='Capture-Destination', help='Blob naming convention for archive, e.g. {Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}. Here all the parameters (Namespace,EventHub .. etc) are mandatory irrespective of order')

    with self.argument_context('eventhubs eventhub list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    # region EventHub Authorizationrule
    for scope in ['eventhubs eventhub authorization-rule', 'eventhubs eventhub authorization-rule keys renew']:
        with self.argument_context(scope) as c:
            c.argument('authorization_rule_name', arg_type=name_type, id_part='child_name_2', help='Name of EventHub AuthorizationRule')
            c.argument('event_hub_name', id_part='child_name_1', arg_type=event_hub_name_arg_type)

    for scope in ['eventhubs eventhub authorization-rule create', 'eventhubs eventhub authorization-rule update']:
        with self.argument_context(scope) as c:
            c.argument('rights', arg_type=rights_arg_type)

    with self.argument_context('eventhubs eventhub authorization-rule keys renew') as c:
        c.argument('key_type', arg_type=key_arg_type)

    with self.argument_context('eventhubs eventhub authorization-rule list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')
        c.argument('event_hub_name', id_part=None, arg_type=event_hub_name_arg_type)

    with self.argument_context('eventhubs eventhub authorization-rule keys list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')
        c.argument('event_hub_name', id_part=None, arg_type=event_hub_name_arg_type)
        c.argument('authorization_rule_name', arg_type=name_type, id_part=None, help='Name of EventHub AuthorizationRule')


# - ConsumerGroup Region
    with self.argument_context('eventhubs eventhub consumer-group') as c:
        c.argument('event_hub_name', arg_type=event_hub_name_arg_type)
        c.argument('consumer_group_name', arg_type=name_type, id_part='child_name_2', completer=get_consumergroup_command_completion_list, help='Name of ConsumerGroup')

    for scope in ['eventhubs eventhub consumer-group create', 'eventhubs eventhub consumer-group update']:
        with self.argument_context(scope) as c:
            c.argument('user_metadata', help='Usermetadata is a placeholder to store user-defined string data with maximum length 1024. e.g. it can be used to store descriptive data, such as list of teams and their contact information also user-defined configuration settings can be stored.')

    with self.argument_context('eventhubs eventhub consumer-group list') as c:
        c.argument('event_hub_name', arg_type=event_hub_name_arg_type, id_part=None)

#   : Region Geo DR Configuration
    with self.argument_context('eventhubs georecovery-alias') as c:
        c.argument('alias', id_part='child_name_1', help='Name of Alias (Disaster Recovery)')

    with self.argument_context('eventhubs georecovery-alias exists') as c:
        c.argument('name', options_list=['--alias'], arg_type=name_type, help='Name of Geo Recovery Configs - Alias to check availability')

    with self.argument_context('eventhubs georecovery-alias set') as c:
        c.argument('partner_namespace', help='ARM Id of the Primary/Secondary eventhub namespace name, which is part of GEO DR pairing')
        c.argument('alternate_name', help='Alternate Name for the Alias, when the Namespace name and Alias name are same')

    for scope in ['eventhubs georecovery-alias authorization-rule show']:
        with self.argument_context(scope)as c:
            c.argument('authorization_rule_name', arg_type=name_type, help='Name of Namespace AuthorizationRule')

    with self.argument_context('eventhubs georecovery-alias list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    with self.argument_context('eventhubs georecovery-alias authorization-rule list') as c:
        c.argument('alias', options_list=['--alias', '-a'], help='Name of Alias (Disaster Recovery)')
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    with self.argument_context('eventhubs georecovery-alias authorization-rule keys list') as c:
        c.argument('alias', options_list=['--alias', '-a'], id_part=None, help='Name of Alias (Disaster Recovery)')
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')
        c.argument('authorization_rule_name', arg_type=name_type, help='Name of Namespace AuthorizationRule')
