# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.parameters import (
    get_location_type, get_resource_name_completion_list, tags_type,
    file_type, get_enum_type, zone_type, zones_type, resource_group_name_type)

# pylint: disable=line-too-long
def load_arguments(self, _):

    # region - Namespace Create
    with self.argument_context('servicebus namespace create') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type, required=True)
        c.argument('namespace_name', options_list=['--namespace-name'], required=True, help='name of the Namespace')
        c.argument('tags', options_list=['--tags', '-t'], arg_type=tags_type, help='tags for the namespace in Key value pair format')
        c.argument('sku', options_list=['--sku-name'], arg_type=get_enum_type(['Basic', 'Standard', 'Premium']), help='Sku name and allowed values are, Basic, Standard, Premium')
        c.argument('location', options_list=['--location', '-l'], help='Location')
        c.argument('skutier', option_list=['--skutier'], arg_type=get_enum_type(['Basic', 'Standard', 'Premium']), help='Sku Tire with allowed values are, Basic, Standard, Premium')
        c.argument('capacity', option_list=['--capacity'], help='Capacity for Sku')

    # region Namespace Get
    with self.argument_context('servicebus namespace get') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type, required=True)
        c.argument('name', options_list=['--namespace-name', '-n'], required=True, help='name of the Namespace')

    # region Namespace Authorizationrule
    for scope in ['servicebus namespace authorizationrule create', 'servicebus namespace authorizationrule get', 'servicebus namespace authorizationrule listkeys', 'servicebus namespace authorizationrule regeneratekeys']:
        with self.argument_context('servicebus namespace authorizationrule create') as c:
            c.argument('resource_group_name', arg_type=resource_group_name_type, required=True),
            c.argument('namespace', options_list=['--namespace-name', '-n'], required=True, help='name of the Namespace'),
            c.argument('name', options_list=['--name', '-n'], required=True, help='name of the Namespace AuthorizationRule')

    with self.argument_context('servicebus namespace authorizationrule create') as c:
        c.argument('accessrights', options_list=['--access-rights'], required=False, help='Authorization rule rights of type list, allowed values are Send, Listen or Manage')


    with self.argument_context('servicebus namespace authorizationrule regeneratekeys') as c:
        c.argument('regeneratekey', options_list=['--regeneratekey'], required=True, arg_type=get_enum_type(['PrimaryKey', 'SecondaryKey']), help='Authorization rule rights of type list, allowed values are Send, Listen or Manage')

###################################################################
    # region - Queue Create
    with self.argument_context('servicebus queue create') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type, required=True)
        c.argument('namespace_name', options_list=['--namespace-name'], required=True, help='name of the Namespace')
        c.argument('name', options_list=['--name', '-n'], required=True, help='Queue Name'),
        c.argument('lock_duration', options_list=['--lock-duration'], help='ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.'),
        c.argument('max_size_in_megabytes', options_list=['--max-size-in-megabytes'], help='The maximum size of the queue in megabytes, which is the size of memory allocated for the queue. Default is 1024.'),
        c.argument('requires_duplicate_detection', options_list=['--requires-duplicate-detection'], help='A boolean value indicating if this queue requires duplicate detection.'),
        c.argument('requires_session', options_list=['--requires-session'], help='A boolean value that indicates whether the queue supports the concept of sessions.'),
        c.argument('default_message_time_to_live', options_list=['--default-message-time-to-live'], help='ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.'),
        c.argument('dead_lettering_on_message_expiration', options_list=['--dead-lettering-on-message-expiration'], help='A boolean value that indicates whether this queue has dead letter support when a message expires.'),
        c.argument('duplicate_detection_history_time_window', options_list=['--duplicate-detection-history-time-window'], help='ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.'),
        c.argument('max_delivery_count', options_list=['--max-delivery-count'], help='The maximum delivery count. A message is automatically deadlettered after this number of deliveries. default value is 10.'),
        c.argument('status', options_list=['--status'], arg_type=get_enum_type(['Active', 'Disabled', 'Restoring', 'SendDisabled', 'ReceiveDisabled', 'Creating', 'Deleting', 'Renaming','Unknown']), help='Enumerates the possible values for the status of a messaging entity.'),
        c.argument('auto_delete_on_idle', options_list=['--auto-delete-on-idle'], help='ISO 8061 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.'),
        c.argument('enable_partitioning', options_list=['--enable-partitioning'], help='A boolean value that indicates whether the queue is to be partitioned across multiple message brokers.'),
        c.argument('enable_express', options_list=['--enable-express'], help='A boolean value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.')
        c.argument('forward_to', options_list=['--forward-to'], help='Queue/Topic name to forward the messages'),
        c.argument('forward_dead_lettered_messages_to', options_list=['--forward-dead-lettered-messages-to'], help='Queue/Topic name to forward the Dead Letter message')

    # region Queue Get
    with self.argument_context('servicebus queue get') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type, required=True)
        c.argument('namespace_name', options_list=['--namespace-name'], required=True,
                   help='name of the Namespace')
        c.argument('name', options_list=['--name', '-n'], required=True, help='Queue Name')

    # region Queue Authorizationrule
    for scope in ['servicebus queue authorizationrule create', 'servicebus queue authorizationrule get',
                  'serviceubs queue authorizationrule listkeys',
                  'servicebus queue authorizationrule regeneratekeys']:
        with self.argument_context('servicebus queue authorizationrule create') as c:
            c.argument('name', options_list=['--name', '-n'], required=True,
                           help='name of the Queue AuthorizationRule')
            c.argument('namespace', options_list=['--namespace-name', '-n'], required=True,
                           help='name of the Namespace')
            c.argument('queuename', options_list=['--queue-name', '-n'], required=True,
                       help='name of the Queue')

    with self.argument_context('servicebus queue authorizationrule create') as c:
        c.argument('accessrights', options_list=['--access-rights'], required=False,
                   help='Authorization rule rights of type list, allowed values are Send, Listen or Manage')

    with self.argument_context('servicebus queue authorizationrule regeneratekeys') as c:
        c.argument('regeneratekey', options_list=['--regeneratekey'], required=True,
                   arg_type=get_enum_type(['PrimaryKey', 'SecondaryKey']),
                   help='Authorization rule rights of type list, allowed values are Send, Listen or Manage')

 #################################################################
    # region - Topic Create
    with self.argument_context('servicebus topic create') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type, required=True),
        c.argument('namespace_name', options_list=['--namespace-name'], required=True, help='name of the Namespace'),
        c.argument('name', options_list=['--name', '-n'], required=True, help='Topic Name'),
        c.argument('default_message_time_to_live', options_list=['--default-message-time-to-live'], help='ISO 8601 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.'),
        c.argument('max_size_in_megabytes', options_list=['--default-message-time-to-live'], help='Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024.'),
        c.argument('requires_duplicate_detection', options_list=['--default-message-time-to-live'], help='Value indicating if this topic requires duplicate detection.'),
        c.argument('duplicate_detection_history_time_window', options_list=['--duplicate-detection-history-time-window'], help='ISO8601 timespan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.'),
        c.argument('enable_batched_operations', options_list=['--enable-batched-operations'], help='Value that indicates whether server-side batched operations are enabled.'),
        c.argument('status', options_list=['--status'], arg_type=get_enum_type(['Active', 'Disabled', 'Restoring', 'SendDisabled', 'ReceiveDisabled', 'Creating', 'Deleting', 'Renaming','Unknown']), help='Enumerates the possible values for the status of a messaging entity.'),
        c.argument('support_ordering', options_list=['--support-ordering'], help='Value that indicates whether the topic supports ordering.'),
        c.argument('auto_delete_on_idle', options_list=['--auto-delete-on-idle'], help='ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.'),
        c.argument('enable_partitioning', options_list=['--enable-partitioning'], help='Value that indicates whether the topic to be partitioned across multiple message brokers is enabled.'),
        c.argument('enable_express', options_list=['--enable-express'], help='Value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.')

    # region Topic Get
    with self.argument_context('servicebus topic get') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type, required=True),
        c.argument('name', options_list=['--namespace-name', '-n'], required=True, help='name of the Namespace'),
        c.argument('name', options_list=['--name', '-n'], help='Topic Name')

    # region Topic Authorizationrule
    for scope in ['servicebus topic authorizationrule create', 'servicebus topic authorizationrule get',
                  'serviceubs topic authorizationrule listkeys',
                  'servicebus topic authorizationrule regeneratekeys']:
        with self.argument_context('servicebus topic authorizationrule create') as c:
            c.argument('name', options_list=['--name', '-n'], required=True,
                           help='name of the Topic AuthorizationRule')
            c.argument('namespace', options_list=['--namespace-name', '-n'], required=True,
                           help='name of the Namespace')
            c.argument('queuename', options_list=['--topic-name', '-n'], required=True,
                       help='name of the Topic')

    with self.argument_context('servicebus topic authorizationrule create') as c:
        c.argument('accessrights', options_list=['--access-rights'], required=False,
                   help='Authorization rule rights of type list, allowed values are Send, Listen or Manage')

    with self.argument_context('servicebus topic authorizationrule regeneratekeys') as c:
        c.argument('regeneratekey', options_list=['--regeneratekey'], required=True,
                   arg_type=get_enum_type(['PrimaryKey', 'SecondaryKey']),
                   help='Authorization rule rights of type list, allowed values are Send, Listen or Manage')


#################################################################
    # region - Subscription Create
    with self.argument_context('servicebus subscription create') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type, required=True),
        c.argument('namespace_name', options_list=['--namespace-name'], required=True,help='name of the Namespace'),
        c.argument('topicname', options_list=['--topic-name', '-n'], required=True, help='Topic Name'),
        c.argument('name', options_list=['--name', '-n'], required=True, help='Subscription Name'),
        c.argument('lock_duration', options_list=['--lock-duration'], help='ISO 8061 lock duration timespan for the subscription. The default value is 1 minute.'),
        c.argument('requires_session', options_list=['--enable-express'], help='A boolean value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.')
        c.argument('default_message_time_to_live', options_list=['--default-message-time-to-live'], help='ISO 8061 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.'),
        c.argument('dead_lettering_on_message_expiration', options_list=['--dead-lettering-on-message-expiration'], help='A boolean Value that indicates whether a subscription has dead letter support when a message expires.'),
        c.argument('duplicate_detection_history_time_window', options_list=['--duplicate-detection-history-time-window'], help='ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.'),
        c.argument('max_delivery_count', options_list=['--max-delivery-count'], help='Number of maximum deliveries.'),
        c.argument('status', options_list=['--status'], arg_type=get_enum_type(['Active', 'Disabled', 'Restoring', 'SendDisabled', 'ReceiveDisabled', 'Creating', 'Deleting', 'Renaming','Unknown']), help='Enumerates the possible values for the status of a messaging entity.'),
        c.argument('enable_batched_operations', options_list=['--enable-batched-operations'], help='Value that indicates whether server-side batched operations are enabled.'),
        c.argument('auto_delete_on_idle', options_list=['--auto-delete-on-idle'], help='ISO 8061 timeSpan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.'),
        #c.argument('forward_to', options_list=['--forward-to'], help='Queue/Topic name to forward the messages'),
        #c.argument('forward_dead_lettered_messages_to', options_list=['--forward-dead-lettered-messages-to'], help='Queue/Topic name to forward the Dead Letter message')

    # region Subscription Get
    with self.argument_context('servicebus subscription get') as c:
        c.argument('namespacename', options_list=['--namespace-name', '-n'], required=False, help='name of the Namespace'),
        c.argument('topicname', options_list=['--topic-name', '-n'], help='name of the Topic'),
        c.argument('name', options_list=['--name', '-n'], help='name of the Subscription of Topic')

    with self.argument_context('servicebus subscription list') as c:
        c.argument('namespacename', options_list=['--namespace-name', '-n'], required=False, help='name of the Namespace'),
        c.argument('topicname', options_list=['--topic-name', '-n'], help='name of the Topic')

    with self.argument_context('servicebus subscription delete') as c:
        c.argument('namespacename', options_list=['--namespace-name', '-n'], required=False, help='name of the Namespace'),
        c.argument('topicname', options_list=['--topic-name', '-n'], help='name of the Topic'),
        c.argument('name', options_list=['--name', '-n'], help='name of the Subscription of Topic')
