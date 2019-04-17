# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=unused-import

from knack.help_files import helps

helps['servicebus'] = """
    type: group
    short-summary: Manage Azure Service Bus namespaces, queues, topics, subscriptions, rules and geo-disaster recovery configuration alias
"""

helps['servicebus namespace'] = """
    type: group
    short-summary: Manage Azure Service Bus Namespace
"""

helps['servicebus namespace authorization-rule'] = """
    type: group
    short-summary: Manage Azure Service Bus Namespace Authorization Rule
"""

helps['servicebus namespace authorization-rule keys'] = """
    type: group
    short-summary: Manage Azure Authorization Rule connection strings for Namespace
"""
helps['servicebus namespace network-rule'] = """
    type: group
    short-summary: Manage Azure ServiceBus NetwrokruleSet for Namespace
"""

helps['servicebus namespace network-rule virtual-network-rule'] = """
    type: group
    short-summary: Manage Azure ServiceBus VirtualNetworkRule of NetwrokruleSet for Namespace
"""

helps['servicebus namespace network-rule ip-address-rule'] = """
    type: group
    short-summary: Manage Azure ServiceBus IPRule of NetwrokruleSet for Namespace
"""

helps['servicebus queue'] = """
    type: group
    short-summary: Manage Azure Service Bus Queue and Authorization Rule
"""

helps['servicebus queue authorization-rule'] = """
    type: group
    short-summary: Manage Azure Service Bus Queue Authorization Rule
"""

helps['servicebus queue authorization-rule keys'] = """
    type: group
    short-summary: Manage Azure Authorization Rule keys for Service Bus Queue
"""

helps['servicebus topic'] = """
    type: group
    short-summary: Manage Azure Service Bus Topic and Authorization Rule
"""

helps['servicebus topic authorization-rule'] = """
    type: group
    short-summary: Manage Azure Service Bus Topic Authorization Rule
"""

helps['servicebus topic authorization-rule keys'] = """
    type: group
    short-summary: Manage Azure Authorization Rule keys for Service Bus Topic
"""

helps['servicebus topic subscription'] = """
    type: group
    short-summary: Manage Azure Service Bus Subscription
"""

helps['servicebus topic subscription rule'] = """
    type: group
    short-summary: Manage Azure Service Bus Rule
"""

helps['servicebus georecovery-alias'] = """
    type: group
    short-summary: Manage Azure Service Bus Geo-Disaster Recovery Configuration Alias
"""

helps['servicebus georecovery-alias authorization-rule'] = """
    type: group
    short-summary: Manage Azure Service Bus Authorization Rule for Namespace with Geo-Disaster Recovery Configuration Alias
"""

helps['servicebus georecovery-alias authorization-rule keys'] = """
    type: group
    short-summary: Manage Azure Authorization Rule keys for Service Bus Namespace
"""

helps['servicebus migration'] = """
    type: group
    short-summary: Manage Azure Service Bus Migration of Standard to Premium
"""

helps['servicebus namespace exists'] = """
    type: command
    short-summary: check for the availability of the given name for the Namespace
    examples:
        - name: check for the availability of mynamespace for the Namespace
          text: az servicebus namespace exists --name mynamespace
"""

helps['servicebus namespace create'] = """
    type: command
    short-summary: Create a Service Bus Namespace
    examples:
        - name: Create a Service Bus Namespace.
          text: az servicebus namespace create --resource-group myresourcegroup --name mynamespace --location westus --tags tag1=value1 tag2=value2 --sku Standard
"""

helps['servicebus namespace update'] = """
    type: command
    short-summary: Updates a Service Bus Namespace
    examples:
        - name: Updates a Service Bus Namespace.
          text: az servicebus namespace update --resource-group myresourcegroup --name mynamespace --tags tag=value
"""

helps['servicebus namespace show'] = """
    type: command
    short-summary: Shows the Service Bus Namespace details
    examples:
        - name: shows the Namespace details.
          text: az servicebus namespace show --resource-group myresourcegroup --name mynamespace
"""

helps['servicebus namespace list'] = """
    type: command
    short-summary: List the Service Bus Namespaces
    examples:
        - name: Get the Service Bus Namespaces by resource group
          text: az servicebus namespace list --resource-group myresourcegroup
        - name: Get the Service Bus Namespaces by Subscription.
          text: az servicebus namespace list
"""

helps['servicebus namespace delete'] = """
    type: command
    short-summary: Deletes the Service Bus Namespace
    examples:
        - name: Deletes the Service Bus Namespace
          text: az servicebus namespace delete --resource-group myresourcegroup --name mynamespace
"""

helps['servicebus namespace authorization-rule create'] = """
    type: command
    short-summary: Create Authorization Rule for the given Service Bus Namespace
    examples:
        - name: Create Authorization Rule 'myauthorule' for the given Service Bus Namespace 'mynamepsace' in resourcegroup
          text: az servicebus namespace authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --rights Send Listen
"""

helps['servicebus namespace authorization-rule update'] = """
    type: command
    short-summary: Updates Authorization Rule for the given Service Bus Namespace
    examples:
        - name: Updates Authorization Rule 'myauthorule' for the given Service Bus Namespace 'mynamepsace' in resourcegroup
          text: az servicebus namespace authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --rights Send
"""

helps['servicebus namespace authorization-rule show'] = """
    type: command
    short-summary: Shows the details of Service Bus Namespace Authorization Rule
    examples:
        - name: Shows the details of Service Bus Namespace Authorization Rule
          text: az servicebus namespace authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['servicebus namespace authorization-rule list'] = """
    type: command
    short-summary: Shows the list of Authorization Rule by Service Bus Namespace
    examples:
        - name: Shows the list of Authorization Rule by Service Bus Namespace
          text: az servicebus namespace authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus namespace authorization-rule keys list'] = """
    type: command
    short-summary: List the keys and connection strings of Authorization Rule for Service Bus Namespace
    examples:
        - name: List the keys and connection strings of Authorization Rule for Service Bus Namespace
          text: az servicebus namespace authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['servicebus namespace authorization-rule keys renew'] = """
    type: command
    short-summary: Regenerate keys of Authorization Rule for the Service Bus Namespace.
    examples:
        - name: Regenerate keys of Authorization Rule for the Service Bus Namespace.
          text: az servicebus namespace authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --key PrimaryKey
"""

helps['servicebus namespace authorization-rule delete'] = """
    type: command
    short-summary: Deletes the Authorization Rule of the Service Bus Namespace.
    examples:
        - name: Deletes the Authorization Rule of the Service Bus Namespace.
          text: az servicebus namespace authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['servicebus queue create'] = """
    type: command
    short-summary: Create the Service Bus Queue
    examples:
        - name: Create Service Bus Queue.
          text: az servicebus queue create --resource-group myresourcegroup --namespace-name mynamespace --name myqueue
"""

helps['servicebus queue update'] = """
    type: command
    short-summary: Updates existing Service Bus Queue
    examples:
        - name: Updates Service Bus Queue.
          text: az servicebus queue update --resource-group myresourcegroup --namespace-name mynamespace --name myqueue --auto-delete-on-idle PT3M
"""

helps['servicebus queue show'] = """
    type: command
    short-summary: shows the Service Bus Queue Details
    examples:
        - name: Shows the Service Bus Queue Details
          text: az servicebus queue show --resource-group myresourcegroup --namespace-name mynamespace --name myqueue
"""

helps['servicebus queue list'] = """
    type: command
    short-summary: List the Queue by Service Bus Namepsace
    examples:
        - name: Get the Queues by Service Bus Namespace.
          text: az servicebus queue list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus queue delete'] = """
    type: command
    short-summary: Deletes the Service Bus Queue
    examples:
        - name: Deletes the queue
          text: az servicebus queue delete --resource-group myresourcegroup --namespace-name mynamespace --name myqueue
"""

helps['servicebus queue authorization-rule create'] = """
    type: command
    short-summary: Create Authorization Rule for the given Service Bus Queue.
    examples:
        - name: Create Authorization Rule for Queue
          text: az servicebus queue authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule --rights Listen
"""

helps['servicebus queue authorization-rule update'] = """
    type: command
    short-summary: Update Authorization Rule for the given Service Bus Queue.
    examples:
        - name: Update Authorization Rule for Queue
          text: az servicebus queue authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule --rights Send
"""

helps['servicebus queue authorization-rule show'] = """
    type: command
    short-summary: show properties of Authorization Rule for the given Service Bus Queue.
    examples:
        - name: show properties of Authorization Rule
          text: az servicebus queue authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule
"""

helps['servicebus queue authorization-rule list'] = """
    type: command
    short-summary: List of Authorization Rule by Service Bus Queue.
    examples:
        - name: List of Authorization Rule by Queue
          text: az servicebus queue authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue
"""

helps['servicebus queue authorization-rule keys list'] = """
    type: command
    short-summary: List the keys and connection strings of Authorization Rule for the given Service Bus Queue
    examples:
        - name: List the keys and connection strings of Authorization Rule for the given Service Bus Queue
          text: az servicebus queue authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule
"""

helps['servicebus queue authorization-rule keys renew'] = """
    type: command
    short-summary: Regenerate keys of Authorization Rule for Service Bus Queue
    examples:
        - name: Regenerate keys of Authorization Rule for Service Bus Queue
          text: az servicebus queue authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule --key PrimaryKey
"""

helps['servicebus queue authorization-rule delete'] = """
    type: command
    short-summary: Delete the Authorization Rule of Service Bus Queue
    examples:
        - name: Delete the Authorization Rule of Service Bus Queue
          text: az servicebus queue authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule
"""

helps['servicebus topic create'] = """
    type: command
    short-summary: Create the Service Bus Topic
    examples:
        - name: Create a new Service Bus Topic
          text: az servicebus topic create --resource-group myresourcegroup --namespace-name mynamespace --name mytopic
"""

helps['servicebus topic update'] = """
    type: command
    short-summary: Updates the Service Bus Topic
    examples:
        - name: Updates existing Service Bus Topic.
          text: az servicebus topic update --resource-group myresourcegroup --namespace-name mynamespace --name mytopic --enable-ordering True
"""

helps['servicebus topic show'] = """
    type: command
    short-summary: Shows the Service Bus Topic Details
    examples:
        - name: Shows the Topic details.
          text: az servicebus topic show --resource-group myresourcegroup --namespace-name mynamespace --name mytopic
"""

helps['servicebus topic list'] = """
    type: command
    short-summary: List the Topic by Service Bus Namepsace
    examples:
        - name: Get the Topics by Namespace.
          text: az servicebus topic list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus topic delete'] = """
    type: command
    short-summary: Deletes the Service Bus Topic
    examples:
        - name: Deletes the Service Bus Topic
          text: az servicebus topic delete --resource-group myresourcegroup --namespace-name mynamespace --name mytopic
"""

helps['servicebus topic authorization-rule create'] = """
    type: command
    short-summary: Create Authorization Rule for given Service Bus Topic
    examples:
        - name: Create Authorization Rule for given Service Bus Topic
          text: az servicebus topic authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule --rights Send Listen
"""

helps['servicebus topic authorization-rule update'] = """
    type: command
    short-summary: Create Authorization Rule for given Service Bus Topic
    examples:
        - name: Create Authorization Rule for given Service Bus Topic
          text: az servicebus topic authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule --rights Send
"""

helps['servicebus topic authorization-rule show'] = """
    type: command
    short-summary: Shows the details of Authorization Rule for given Service Bus Topic
    examples:
        - name: Shows the details of Authorization Rule for given Service Bus Topic
          text: az servicebus topic authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule
"""

helps['servicebus topic authorization-rule list'] = """
    type: command
    short-summary: shows list of Authorization Rule by Service Bus Topic
    examples:
        - name: shows list of Authorization Rule by Service Bus Topic
          text: az servicebus topic authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic
"""

helps['servicebus topic authorization-rule keys list'] = """
    type: command
    short-summary: List the keys and connection strings of Authorization Rule for Service Bus Topic.
    examples:
        - name: List the keys and connection strings of Authorization Rule for Service Bus Topic.
          text: az servicebus topic authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule
"""

helps['servicebus topic authorization-rule keys renew'] = """
    type: command
    short-summary: Regenerate keys of Authorization Rule for Service Bus Topic.
    examples:
        - name: Regenerate key of Service Bus Topic.
          text: az servicebus topic authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule --key PrimaryKey
"""

helps['servicebus topic authorization-rule delete'] = """
    type: command
    short-summary: Deletes the Authorization Rule of the given Service Bus Topic.
    examples:
        - name: Deletes the Authorization Rule of Service Bus Topic.
          text: az servicebus topic authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule
"""

helps['servicebus topic subscription create'] = """
    type: command
    short-summary: Create the ServiceBus Subscription
    examples:
        - name: Create a new Subscription.
          text: az servicebus topic subscription create --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription

    """

helps['servicebus topic subscription update'] = """
    type: command
    short-summary: Updates the ServiceBus Subscription
    examples:
        - name: Update a new Subscription.
          text: az servicebus topic subscription update --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription --lock-duration PT3M
    """

helps['servicebus topic subscription show'] = """
    type: command
    short-summary: Shows Service Bus Subscription Details
    examples:
        - name: Shows the Subscription details.
          text: az servicebus topic subscription show --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription
"""

helps['servicebus topic subscription list'] = """
    type: command
    short-summary: List the Subscription by Service Bus Topic
    examples:
        - name: Shows the Subscription by Service Bus Topic.
          text: az servicebus topic subscription list --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic
"""

helps['servicebus topic subscription delete'] = """
    type: command
    short-summary: Deletes the Service Bus Subscription
    examples:
        - name: Deletes the Subscription
          text: az servicebus topic subscription delete --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription
"""

helps['servicebus topic subscription rule create'] = """
    type: command
    short-summary: Create the ServiceBus Rule for Subscription
    examples:
        - name: Create Rule.
          text: az servicebus topic subscription rule create --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule --filter-sql-expression myproperty=myvalue
"""

helps['servicebus topic subscription rule update'] = """
    type: command
    short-summary: Updates the ServiceBus Rule for Subscription
    examples:
        - name: Updates Rule.
          text: az servicebus topic subscription rule update --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule --filter-sql-expression myproperty=myupdatedvalue
"""

helps['servicebus topic subscription rule show'] = """
    type: command
    short-summary: Shows ServiceBus Rule Details
    examples:
        - name: Shows the ServiceBus Rule details.
          text: az servicebus topic subscription rule show --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule
"""

helps['servicebus topic subscription rule list'] = """
    type: command
    short-summary: List the ServiceBus Rule by Subscription
    examples:
        - name: Shows the Rule ServiceBus by Subscription.
          text: az servicebus topic subscription rule list --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic
           --subscription-name mysubscription
"""

helps['servicebus topic subscription rule delete'] = """
    type: command
    short-summary: Deletes the ServiceBus Rule
    examples:
        - name: Deletes the ServiceBus Rule
          text: az servicebus topic subscription rule delete --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule
"""

helps['servicebus georecovery-alias exists'] = """
    type: command
    short-summary: Check if Geo Recovery Alias Name is available
    examples:
        - name: Check availability of the Geo-Disaster Recovery Configuration Alias Name
          text: az servicebus georecovery-alias exists --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias set'] = """
    type: command
    short-summary: Sets Service Bus Geo-Disaster Recovery Configuration Alias for the give Namespace
    examples:
        - name: Sets Geo Disaster Recovery configuration - Alias for the give Namespace
          text: az servicebus georecovery-alias set --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname --partner-namespace armresourceid
"""

helps['servicebus georecovery-alias show'] = """
    type: command
    short-summary: shows properties of Service Bus Geo-Disaster Recovery Configuration Alias for Primay/Secondary Namespace
    examples:
        - name:  show properties Geo-Disaster Recovery Configuration Alias of the Primary Namespace
          text: az servicebus georecovery-alias show  --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
        - name:  Get details of Alias (Geo DR Configuration)  of the Secondary Namespace
          text: az servicebus georecovery-alias show  --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias authorization-rule list'] = """
    type: command
    short-summary: Shows the list of Authorization Rule by Service Bus Namespace
    examples:
        - name: Shows the list of Authorization Rule by Service Bus Namespace
          text: az servicebus georecovery-alias authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias authorization-rule keys list'] = """
    type: command
    short-summary: List the keys and connection strings of Authorization Rule for the Service Bus Namespace
    examples:
        - name: List the keys and connection strings of Authorization Rule for the namespace.
          text: az servicebus georecovery-alias authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --alias myaliasname
"""

helps['servicebus georecovery-alias break-pair'] = """
    type: command
    short-summary: Disables Service Bus Geo-Disaster Recovery Configuration Alias and stops replicating changes from primary to secondary namespaces
    examples:
        - name:  Disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces
          text: az servicebus georecovery-alias break-pair --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias fail-over'] = """
    type: command
    short-summary: Invokes Service Bus Geo-Disaster Recovery Configuration Alias failover and re-configure the alias to point to the secondary namespace
    examples:
        - name:  Invokes Geo-Disaster Recovery Configuration Alias failover and reconfigure the alias to point to the secondary namespace
          text: az servicebus georecovery-alias fail-over --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias delete'] = """
    type: command
    short-summary: Deletes Service Bus Geo-Disaster Recovery Configuration Alias request accepted
    examples:
        - name:  Delete Service Bus Geo-Disaster Recovery Configuration Alias request accepted
          text: az servicebus georecovery-alias delete --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
"""

helps['servicebus migration start'] = """
    type: command
    short-summary: Create and Start Service Bus Migration of Standard to Premium namespace.
    long-summary: Service Bus Migration requires an empty Premium namespace to replicate entities from Standard namespace.
    examples:
        - name: Create and Start Service Bus Migration of Standard to Premium namespace
          text: az servicebus migration start --resource-group myresourcegroup --name standardnamespace --target-namespace ARMIDpremiumnamespace --post-migration-name mypostmigrationname
"""

helps['servicebus migration show'] = """
    type: command
    short-summary: shows properties of properties of Service Bus Migration
    examples:
        - name: shows properties of properties of Service Bus Migration
          text: az servicebus migration show --resource-group myresourcegroup --name standardnamespace
"""

helps['servicebus migration complete'] = """
    type: command
    short-summary: Completes the Service Bus Migration of Standard to Premium namespace
    long-summary: After completing migration, the existing connection strings to standard namespace will connect to premium namespace automatically. Post migration name is the name that can be used to connect to standard namespace after migration is complete.
    examples:
        - name:  Completes the Service Bus Migration of Standard to Premium namespace
          text: az servicebus migration complete --resource-group myresourcegroup --name standardnamespace
"""

helps['servicebus migration abort'] = """
    type: command
    short-summary: Disable the Service Bus Migration of Standard to Premium namespace
    long-summary: abort command stops the replication of entities from standard to premium namespaces. The entities replicated to premium namespace before abort command will be available under premium namespace. The aborted migration can not be resumed, its has to restarted.
    examples:
        - name:  Disable Service Bus Migration of Standard to Premium namespace
          text: az servicebus migration abort --resource-group myresourcegroup --name standardnamespace
"""


helps['servicebus namespace network-rule create'] = """
    type: command
    short-summary: Set a Network rule for a Namespace
    examples:
        - name: set a Network rule for a namespace
          text: az servicebus namespace network-rule create --resource-group myresourcegroup --namespace-name mynamespace  --default-action true
"""

helps['servicebus namespace network-rule update'] = """
    type: command
    short-summary: Update a Network rule for a Namespace
    examples:
        - name: set a network rule for a namespace
          text: az servicebus namespace network-rule update --resource-group myresourcegroup --namespace-name mynamespace --default-action false
"""

helps['servicebus namespace network-rule list'] = """
    type: command
    short-summary: Show properties of Network rule of the given Namespace
    examples:
        - name: Show properties of Network rule of the given Namespace
          text: az servicebus namespace network-rule list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus namespace network-rule delete'] = """
    type: command
    short-summary: Delete Network Rule of the given Namespace
    examples:
        - name: Delete Network rulet of the given Namespace
          text: az servicebus namespace network-rule delete --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus namespace network-rule virtual-network-rule add'] = """
    type: command
    short-summary: Adds a VirtualNetworkRule to Network rule for the given Namespace
    examples:
        - name: Adds a VirtualNetworkRule to Network rule for the given Namespace
          text: az servicebus namespace network-rule virtualnetworkrule add --resource-group myresourcegroup --namespace-name mynamespace --subnet-id mysubnetid --ignore-missing-vnet-serviceendpoint true/false
"""

helps['servicebus namespace network-rule virtual-network-rule list'] = """
    type: command
    short-summary: List all VirtualNetworkRule of Network rule for the given Namespace
    examples:
        - name: List all VirtualNetworkRule of Network rule for the given Namespace
          text: az servicebus namespace network-rule virtual-network-rule list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus namespace network-rule virtual-network-rule remove'] = """
    type: command
    short-summary: Deletes the specified VirtualNetworkRule of Network rule for the given Namespace
    examples:
        - name: Deletes the specified VirtualNetworkRule of Network rule for the given Namespace
          text: az servicebus namespace network-rule virtual-network-rule remove --resource-group myresourcegroup --namespace-name mynamespace --subnet mysubnetid
"""

helps['servicebus namespace network-rule ip-address-rule add'] = """
    type: command
    short-summary: Adds a IPRule to Network rule for the given Namespace
    examples:
        - name: Adds a IPRule to Network rule for the given Namespace
          text: az servicebus namespace network-rule ip-address-rule add --resource-group myresourcegroup --namespace-name mynamespace --ip-address myipmask --action allow
"""

helps['servicebus namespace network-rule ip-address-rule list'] = """
    type: command
    short-summary: List all IPRule of Network rule for the given Namespace
    examples:
        - name: List all IPRule of Network rule for the given Namespace
          text: az servicebus namespace network-rule ip-address-rule list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus namespace network-rule ip-address-rule remove'] = """
    type: command
    short-summary: Adds a IPRule to Network rule for the given Namespace
    examples:
        - name: Adds a IPRule to Network rule for the given Namespace
          text: az servicebus namespace network-rule ip-address-rule --resource-group myresourcegroup --namespace-name mynamespace --ip-address myipmask
"""
