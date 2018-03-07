# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import tags_type, get_enum_type, resource_group_name_type, name_type, get_location_type, get_three_state_flag, get_resource_name_completion_list
from azure.cli.core.commands.validators import get_default_location_from_resource_group


def load_arguments_sb(self, _):
    from azure.cli.command_modules.servicebus._completers import get_queue_command_completion_list, \
        get_rules_command_completion_list, get_subscriptions_command_completion_list, get_topic_command_completion_list
    from azure.cli.command_modules.servicebus._validators import _validate_auto_delete_on_idle, \
        _validate_duplicate_detection_history_time_window, \
        _validate_default_message_time_to_live, \
        _validate_lock_duration

    from knack.arguments import CLIArgumentType
    from azure.mgmt.servicebus.models.service_bus_management_client_enums import SkuName, AccessRights, KeyType, FilterType
    rights_arg_type = CLIArgumentType(options_list=['--rights'], nargs='+', arg_type=get_enum_type(AccessRights), help='Space-separated list of Authorization rule rights')
    key_arg_type = CLIArgumentType(options_list=['--key-name'], arg_type=get_enum_type(KeyType), help='specifies Primary or Secondary key needs to be reset')

    with self.argument_context('servicebus') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('namespace_name', id_part='name', options_list=['--namespace-name'], help='Name of Namespace')

    with self.argument_context('servicebus namespace') as c:
        c.argument('namespace_name', id_part='name', arg_type=name_type, completer=get_resource_name_completion_list('Microsoft.ServiceBus/namespaces'), help='Name of Namespace')

    with self.argument_context('servicebus namespace create') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), validator=get_default_location_from_resource_group)
        c.argument('tags', arg_type=tags_type)
        c.argument('sku', arg_type=get_enum_type(SkuName))
        c.argument('capacity', help='Capacity for Sku')

    with self.argument_context('servicebus namespace update') as c:
        c.argument('tags', arg_type=tags_type)
        c.argument('sku', arg_type=get_enum_type(SkuName))
        c.argument('capacity', help='Capacity for Sku')

    # region Namespace Authorization Rule
    with self.argument_context('servicebus namespace authorization-rule list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of the Namespace')

    with self.argument_context('servicebus namespace authorization-rule') as c:
        c.argument('authorization_rule_name', arg_type=name_type, id_part='child_name_1', help='Name of Namespace Authorization Rule')
        c.argument('namespace_name', id_part='name', options_list=['--namespace-name'], help='Name of Namespace')

    for scope in ['servicebus namespace authorization-rule create', 'servicebus namespace authorization-rule update', 'servicebus queue authorization-rule create', 'servicebus queue authorization-rule update', 'servicebus topic authorization-rule create', 'servicebus topic authorization-rule update']:
        with self.argument_context(scope) as c:
            c.argument('rights', arg_type=rights_arg_type)

    with self.argument_context('servicebus namespace authorization-rule keys renew') as c:
        c.argument('key_type', arg_type=key_arg_type)

    with self.argument_context('servicebus namespace authorization-rule keys list') as c:
        c.argument('authorization_rule_name', arg_type=name_type, id_part=None, help='Name of Namespace Authorization Rule')
        c.argument('namespace_name', id_part=None, options_list=['--namespace-name'], help='Name of Namespace')

    # region Queue
    with self.argument_context('servicebus queue') as c:
        c.argument('queue_name', arg_type=name_type, id_part='child_name_1', completer=get_queue_command_completion_list, help='Name of Queue')

    # region - Queue Create
    with self.argument_context('servicebus queue create') as c:
        c.argument('queue_name', arg_type=name_type, id_part='child_name_1', help='Name of Queue')
        c.argument('lock_duration', validator=_validate_lock_duration, help='String ISO 8601 timespan or duration format for duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.')
        c.argument('max_size_in_megabytes', options_list=['--max-size'], type=int, choices=[1024, 2048, 3072, 4096, 5120], help='The maximum size of queue in megabytes, which is the size of memory allocated for the queue. Default is 1024.')
        c.argument('requires_duplicate_detection', options_list=['--enable-duplicate-detection'], arg_type=get_three_state_flag(), help='A boolean value indicating if this queue requires duplicate detection.')
        c.argument('requires_session', options_list=['--enable-session'], arg_type=get_three_state_flag(), help='A boolean value indicating whether the queue supports the concept of sessions.')
        c.argument('default_message_time_to_live', validator=_validate_default_message_time_to_live, help='ISO 8601 timespan or duration time format for default message to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.')
        c.argument('dead_lettering_on_message_expiration', options_list=['--enabledead-lettering-on-message-expiration'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether this queue has dead letter support when a message expires.')
        c.argument('duplicate_detection_history_time_window', validator=_validate_duplicate_detection_history_time_window, help='ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.')
        c.argument('max_delivery_count', type=int, help='The maximum delivery count. A message is automatically deadlettered after this number of deliveries. default value is 10.')
        c.argument('status', arg_type=get_enum_type(['Active', 'Disabled', 'SendDisabled', 'ReceiveDisabled']), help='Enumerates the possible values for the status of a messaging entity.')
        c.argument('auto_delete_on_idle', validator=_validate_auto_delete_on_idle, help='ISO 8601 timeSpan or duration time format for idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.')
        c.argument('enable_partitioning', arg_type=get_three_state_flag(), help='A boolean value that indicates whether the queue is to be partitioned across multiple message brokers.')
        c.argument('enable_express', arg_type=get_three_state_flag(), help='A boolean value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.')
        c.argument('forward_to', help='Queue/Topic name to forward the messages')
        c.argument('forward_dead_lettered_messages_to', help='Queue/Topic name to forward the Dead Letter message')

    with self.argument_context('servicebus queue update') as c:
        c.argument('queue_name', arg_type=name_type, id_part='child_name_1', help='Name of Queue')
        c.argument('lock_duration', validator=_validate_lock_duration, help='String ISO 8601 timespan or duration format for duration of a peek-lock; that is, the amount of time that the message is locked for other receivers.')
        c.argument('max_size_in_megabytes', options_list=['--max-size'], type=int, choices=[1024, 2048, 3072, 4096, 5120], help='The maximum size of queue in megabytes, which is the size of memory allocated for the queue.')
        c.argument('requires_duplicate_detection', options_list=['--enable-duplicate-detection'], arg_type=get_three_state_flag(), help='A boolean value indicating if this queue requires duplicate detection.')
        c.argument('requires_session', options_list=['--enable-session'], arg_type=get_three_state_flag(), help='A boolean value indicating whether the queue supports the concept of sessions.')
        c.argument('default_message_time_to_live', validator=_validate_default_message_time_to_live, help='ISO 8601 timespan or duration time format for default message to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.')
        c.argument('dead_lettering_on_message_expiration', options_list=['--enabledead-lettering-on-message-expiration'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether this queue has dead letter support when a message expires.')
        c.argument('duplicate_detection_history_time_window', validator=_validate_duplicate_detection_history_time_window, help='ISO 8601 timeSpan structure that defines the duration of the duplicate detection history.')
        c.argument('max_delivery_count', type=int, help='The maximum delivery count. A message is automatically deadlettered after this number of deliveries.')
        c.argument('status', arg_type=get_enum_type(['Active', 'Disabled', 'SendDisabled', 'ReceiveDisabled']), help='Enumerates the possible values for the status of a messaging entity.')
        c.argument('auto_delete_on_idle', validator=_validate_auto_delete_on_idle, help='ISO 8601 timeSpan or duration time format for idle interval after which the queue is automatically deleted.')
        c.argument('enable_partitioning', arg_type=get_three_state_flag(), help='A boolean value that indicates whether the queue is to be partitioned across multiple message brokers.')
        c.argument('enable_express', arg_type=get_three_state_flag(), help='A boolean value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.')
        c.argument('forward_to', help='Queue/Topic name to forward the messages')
        c.argument('forward_dead_lettered_messages_to', help='Queue/Topic name to forward the Dead Letter message')

    with self.argument_context('servicebus queue list') as c:
        c.argument('namespace_name', id_part=None, options_list=['--namespace-name'], help='Name of Namespace')

    # region Queue Authorization Rule
    with self.argument_context('servicebus queue authorization-rule') as c:
        c.argument('authorization_rule_name', arg_type=name_type, id_part='child_name_2', help='Name of Queue Authorization Rule')
        c.argument('queue_name', id_part='child_name_1', options_list=['--queue-name'], help='Name of Queue')

    with self.argument_context('servicebus queue authorization-rule list') as c:
        c.argument('namespace_name', id_part=None, options_list=['--namespace-name'], help='Name of Namespace')
        c.argument('queue_name', id_part=None, options_list=['--queue-name'], help='Name of Queue')

    with self.argument_context('servicebus queue authorization-rule keys renew') as c:
        c.argument('key_type', arg_type=key_arg_type)

    with self.argument_context('servicebus queue authorization-rule keys list') as c:
        c.argument('authorization_rule_name', arg_type=name_type, id_part=None, help='Name of Queue Authorization Rule')
        c.argument('queue_name', id_part=None, options_list=['--queue-name'], help='Name of Queue')
        c.argument('namespace_name', id_part=None, options_list=['--namespace-name'], help='Name of Namespace')

    # region - Topic
    for scope in ['servicebus topic show', 'servicebus topic delete']:
        with self.argument_context(scope) as c:
            c.argument('topic_name', arg_type=name_type, id_part='child_name_1', completer=get_topic_command_completion_list, help='Name of Topic')

    # region - Topic Create
    with self.argument_context('servicebus topic create') as c:
        c.argument('topic_name', arg_type=name_type, id_part='child_name_1', completer=get_topic_command_completion_list, help='Name of Topic')
        c.argument('default_message_time_to_live', validator=_validate_default_message_time_to_live, help='ISO 8601 or duration time format for Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.')
        c.argument('max_size_in_megabytes', options_list=['--max-size'], type=int, choices=[1024, 2048, 3072, 4096, 5120], help='Maximum size of topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024.')
        c.argument('requires_duplicate_detection', options_list=['--enable-duplicate-detection'], arg_type=get_three_state_flag(), help='A boolean value indicating if this topic requires duplicate detection.')
        c.argument('duplicate_detection_history_time_window', validator=_validate_duplicate_detection_history_time_window, help='ISO 8601 timespan or duration time format for structure that defines the duration of the duplicate detection history. The default value is 10 minutes.')
        c.argument('enable_batched_operations', arg_type=get_three_state_flag(), help='Value that indicates whether server-side batched operations are enabled.')
        c.argument('status', arg_type=get_enum_type(['Active', 'Disabled', 'SendDisabled', 'ReceiveDisabled']), help='Enumerates the possible values for the status of a messaging entity.')
        c.argument('support_ordering', options_list=['--enable-support-ordering'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether the topic supports ordering.')
        c.argument('auto_delete_on_idle', validator=_validate_auto_delete_on_idle, help='ISO 8601 timespan or duration time format for idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.')
        c.argument('enable_partitioning', arg_type=get_three_state_flag(), help='A boolean value that indicates whether the topic to be partitioned across multiple message brokers is enabled.')
        c.argument('enable_express', arg_type=get_three_state_flag(), help='A boolean value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.')

    # region - Topic Update
    with self.argument_context('servicebus topic update') as c:
        c.argument('topic_name', arg_type=name_type, id_part='child_name_1', completer=get_topic_command_completion_list, help='Name of Topic')
        c.argument('default_message_time_to_live', validator=_validate_default_message_time_to_live, help='ISO 8601 or duration time format for Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.')
        c.argument('max_size_in_megabytes', options_list=['--max-size'], type=int, choices=[1024, 2048, 3072, 4096, 5120], help='Maximum size of topic in megabytes, which is the size of the memory allocated for the topic.')
        c.argument('requires_duplicate_detection', options_list=['--enable-duplicate-detection'], arg_type=get_three_state_flag(), help='A boolean value indicating if this topic requires duplicate detection.')
        c.argument('duplicate_detection_history_time_window', validator=_validate_duplicate_detection_history_time_window, help='ISO 8601 timespan or duration time format for structure that defines the duration of the duplicate detection history.')
        c.argument('enable_batched_operations', arg_type=get_three_state_flag(), help='Value that indicates whether server-side batched operations are enabled.')
        c.argument('status', arg_type=get_enum_type(['Active', 'Disabled', 'SendDisabled', 'ReceiveDisabled']), help='Enumerates the possible values for the status of a messaging entity.')
        c.argument('support_ordering', options_list=['--enable-support-ordering'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether the topic supports ordering.')
        c.argument('auto_delete_on_idle', validator=_validate_auto_delete_on_idle, help='ISO 8601 timespan or duration time format for idle interval after which the topic is automatically deleted.')
        c.argument('enable_partitioning', arg_type=get_three_state_flag(), help='A boolean value that indicates whether the topic to be partitioned across multiple message brokers is enabled.')
        c.argument('enable_express', arg_type=get_three_state_flag(), help='A boolean value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.')

    for scope in ['servicebus topic show', 'servicebus topic delete']:
        with self.argument_context(scope) as c:
            c.argument('topic_name', arg_type=name_type, id_part='child_name_1', completer=get_topic_command_completion_list, help='Name of Topic')

    with self.argument_context('servicebus topic list') as c:
        c.argument('namespace_name', id_part=None, options_list=['--namespace-name'], help='Name of Namespace')

    # region Topic Authorization Rule
    with self.argument_context('servicebus topic authorization-rule') as c:
        c.argument('authorization_rule_name', arg_type=name_type, id_part='child_name_2', help='name of Topic Authorization Rule')
        c.argument('topic_name', options_list=['--topic-name'], id_part='child_name_1', help='name of Topic')

    with self.argument_context('servicebus topic authorization-rule list') as c:
        c.argument('namespace_name', id_part=None, options_list=['--namespace-name'], help='Name of Namespace')
        c.argument('topic_name', options_list=['--topic-name'], id_part=None, help='name of Topic')

    with self.argument_context('servicebus topic authorization-rule keys renew') as c:
        c.argument('key_type', arg_type=key_arg_type)

    with self.argument_context('servicebus topic authorization-rule keys list') as c:
        c.argument('namespace_name', id_part=None, options_list=['--namespace-name'], help='Name of Namespace')
        c.argument('authorization_rule_name', arg_type=name_type, id_part=None, help='name of Topic Authorization Rule')
        c.argument('topic_name', options_list=['--topic-name'], id_part=None, help='Name of Topic')

    with self.argument_context('servicebus topic subscription') as c:
        c.argument('subscription_name', arg_type=name_type, id_part='child_name_2', help='Name of Subscription')
        c.argument('topic_name', id_part='child_name_1', options_list=['--topic-name'], help='Name of Topic')

    # region - Subscription Create
    with self.argument_context('servicebus topic subscription create') as c:
        c.argument('lock_duration', validator=_validate_lock_duration, help='ISO 8601 or duration format (day:minute:seconds) for lock duration timespan for the subscription. The default value is 1 minute.')
        c.argument('requires_session', options_list=['--enable-session'], arg_type=get_three_state_flag(), help='A boolean value indicating if a subscription supports the concept of sessions.')
        c.argument('default_message_time_to_live', validator=_validate_default_message_time_to_live, help='ISO 8601 or duration time format for Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.')
        c.argument('dead_lettering_on_message_expiration', options_list=['--enable-dead-lettering-on-message-expiration'], arg_type=get_three_state_flag(), help='A boolean Value that indicates whether a subscription has dead letter support when a message expires.')
        c.argument('max_delivery_count', type=int, help='Number of maximum deliveries.')
        c.argument('status', arg_type=get_enum_type(['Active', 'Disabled', 'SendDisabled', 'ReceiveDisabled']))
        c.argument('enable_batched_operations', arg_type=get_three_state_flag(), help='A boolean value that indicates whether server-side batched operations are enabled.')
        c.argument('auto_delete_on_idle', validator=_validate_auto_delete_on_idle, options_list=['--auto-delete-on-idle'], help='ISO 8601 timeSpan  or duration time format for idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.')
        c.argument('forward_to', help='Queue/Topic name to forward the messages')
        c.argument('forward_dead_lettered_messages_to', help='Queue/Topic name to forward the Dead Letter message')

    with self.argument_context('servicebus topic subscription update') as c:
        c.argument('lock_duration', validator=_validate_lock_duration, help='ISO 8601 or duration format (day:minute:seconds) for lock duration timespan for the subscription.')
        c.argument('requires_session', options_list=['--enable-session'], arg_type=get_three_state_flag(), help='A boolean value indicating if a subscription supports the concept of sessions.')
        c.argument('default_message_time_to_live', validator=_validate_default_message_time_to_live, help='ISO 8601 or duration time format for Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.')
        c.argument('dead_lettering_on_message_expiration', options_list=['--enable-dead-lettering-on-message-expiration'], arg_type=get_three_state_flag(), help='A boolean Value that indicates whether a subscription has dead letter support when a message expires.')
        c.argument('max_delivery_count', type=int, help='Number of maximum deliveries.')
        c.argument('status', arg_type=get_enum_type(['Active', 'Disabled', 'SendDisabled', 'ReceiveDisabled']))
        c.argument('enable_batched_operations', arg_type=get_three_state_flag(), help='A boolean value that indicates whether server-side batched operations are enabled.')
        c.argument('auto_delete_on_idle', validator=_validate_auto_delete_on_idle, options_list=['--auto-delete-on-idle'], help='ISO 8601 timeSpan  or duration time format for idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.')
        c.argument('forward_to', help='Queue/Topic name to forward the messages')
        c.argument('forward_dead_lettered_messages_to', help='Queue/Topic name to forward the Dead Letter message')

    with self.argument_context('servicebus topic subscription list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')
        c.argument('topic_name', options_list=['--topic-name'], id_part=None, help='Name of Topic')

    # Region Subscription Rules
    # Rules Create

    with self.argument_context('servicebus topic subscription rule') as c:
        c.argument('rule_name', arg_type=name_type, completer=get_rules_command_completion_list, help='Name of Rule')
        c.argument('subscription_name', options_list=['--subscription-name'], id_part='child_name_2',help='Name of Subscription')
        c.argument('topic_name', options_list=['--topic-name'], id_part='child_name_1', help='Name of Topic')

    for scope in ['servicebus topic subscription rule create', 'servicebus topic subscription rule update']:
        with self.argument_context(scope, arg_group='Action') as c:
            c.argument('filter_type', arg_type=get_enum_type(FilterType), help='Rule Filter types')
            c.argument('action_sql_expression', help='Action SQL expression.')
            c.argument('action_compatibility_level', type=int, help='This property is reserved for future use. An integer value showing the compatibility level, currently hard-coded to 20.')
            c.argument('action_requires_preprocessing', options_list=['--enable-action-preprocessing'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether the rule action requires preprocessing.')
        with self.argument_context(scope, arg_group='SQL Filter') as c:
            c.argument('filter_sql_expression', help='SQL expression. e.g. myproperty=test')
            c.argument('filter_requires_preprocessing', options_list=['--enable-sql-preprocessing'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether the rule action requires preprocessing.')
        with self.argument_context(scope, arg_group='Correlation Filter') as c:
            c.argument('correlation_id', help='Identifier of correlation.')
            c.argument('message_id', help='Identifier of message.')
            c.argument('to', help='Address to send to.')
            c.argument('reply_to', help='Address of the queue to reply to.')
            c.argument('label', help='Application specific label.')
            c.argument('session_id', help='Session identifier')
            c.argument('reply_to_session_id', help='Session identifier to reply to.')
            c.argument('content_type', help='Content type of message.')
            c.argument('requires_preprocessing', options_list=['--enable-correlation-preprocessing'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether the rule action requires preprocessing.')

    with self.argument_context('servicebus topic subscription rule list') as c:
        c.argument('subscription_name', options_list=['--subscription-name'], id_part=None, help='Name of Subscription')
        c.argument('topic_name', options_list=['--topic-name'], id_part=None, help='Name of Topic')
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    # Geo DR - Disaster Recovery Configs - Alias  : Region
    with self.argument_context('servicebus georecovery-alias exists') as c:
        c.argument('name', arg_type=name_type, help='Name of the Alias (Disaster Recovery) to check availability')

    with self.argument_context('servicebus georecovery-alias') as c:
        c.argument('alias', options_list=['--alias', '-a'], id_part='child_name_1', help='Name of the Alias (Disaster Recovery)')

    with self.argument_context('servicebus georecovery-alias set') as c:
        c.argument('partner_namespace', options_list=['--partner-namespace-id'], help='ARM Id of Primary/Secondary eventhub namespace name, which is part of GEO DR pairing')
        c.argument('alternate_name', help='Alternate Name (Post failover) for Primary Namespace, when Namespace name and Alias name are same')

    for scope in ['servicebus georecovery-alias authorization-rule show', 'servicebus georecovery-alias authorization-rule keys list']:
        with self.argument_context(scope)as c:
            c.argument('authorization_rule_name', arg_type=name_type, help='name of Namespace Authorization Rule')

    with self.argument_context('servicebus georecovery-alias list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    with self.argument_context('servicebus georecovery-alias authorization-rule list') as c:
        c.argument('alias', options_list=['--alias', '-a'], help='Name of Alias (Disaster Recovery)')
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    with self.argument_context('servicebus georecovery-alias authorization-rule keys list') as c:
        c.argument('alias', options_list=['--alias', '-a'], id_part=None, help='Name of Alias (Disaster Recovery)')
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')
        c.argument('authorization_rule_name', arg_type=name_type, help='Name of Namespace AuthorizationRule')
