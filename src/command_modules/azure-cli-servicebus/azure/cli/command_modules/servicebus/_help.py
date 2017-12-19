# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

helps['sb namespace check_name_availability'] = """
    type: command
    short-summary: check for the availability of the given name for the Namespace
    examples:
        - name: Create a new topic.
          text: az sb namespace check_name_availability --name {namespacename}
    """

helps['sb namespace create'] = """
    type: command
    short-summary: Creates the ServiceBus Namespace
    examples:
        - name: Create a new namespace.
          text: helps['sb namespace create --resource-group {rg} --name {namespacename} --location {location}
           --tags {tags} --sku-name {sku} --skutier {tier}']

    """

helps['sb namespace get'] = """
    type: command
    short-summary: Get the Namespace Details
    examples:
        - name: Get the Namespace details.
          text: helps['sb namespace get --resource-group {rg} --name {namespacename}']

    """

helps['sb namespace list'] = """
    type: command
    short-summary: List the Namespaces by ResourceGroup or By subscription
    examples:
        - name: Get the Namespaces by resource Group.
          text: helps['sb namespace list --resource-group {rg}']
        - name: Get the Namespaces by Subscription.
          text: helps['sb namespace list']    

    """

helps['sb namespace delete'] = """
    type: command
    short-summary: Deletes the Namespaces
    examples:
        - name: Deletes the Namespace
          text: helps['sb namespace delete --resource-group {rg} --name {namespacename}']
          
    """

helps['sb namespace authorizationrule create'] = """
    type: command
    short-summary: Creates Authorization rule for the given Namespace 
    examples:
        - name: Creates Authorization rules
          text: helps['sb namespace authorizationrule create --resource-group {rg} --namespace-name {namespacename}
           --name {authoname} --access-rights [Send, Listen]']

    """

helps['sb namespace authorizationrule get'] = """
    type: command
    short-summary: Gets the details of AuthorizatioRule 
    examples:
        - name: Gets the details of AuthorizatioRule
          text: helps['sb namespace authorizationrule get --resource-group {rg} --namespace-name {namespacename}
           --name {authoname}']

    """

helps['sb namespace authorizationrule list'] = """
    type: command
    short-summary: Gets the list of AuthorizatioRule by Namespace 
    examples:
        - name: Gets the list of AuthorizatioRule by Namespace
          text: helps['sb namespace authorizationrule get --resource-group {rg} --namespace-name {namespacename}']

    """

helps['sb namespace authorizationrule listkeys'] = """
    type: command
    short-summary: Gets the connectionstriongs of AuthorizatioRule for the namespace.  
    examples:
        - name: Gets the connectionstriongs of AuthorizatioRule for the namespace.
          text: helps['sb namespace authorizationrule listkeys --resource-group {rg} --namespace-name {namespacename}
           --name {authoname}']

    """

helps['sb namespace authorizationrule regenerate_keys'] = """
    type: command
    short-summary: Regenerate the connectionstriongs of AuthorizatioRule for the namespace.  
    examples:
        - name: Regenerate the connectionstriongs of AuthorizatioRule for the namespace.
          text: helps['sb namespace authorizationrule regenerate_keys --resource-group {rg}
           --namespace-name {namespacename} --name {authoname} --regeneratekey {primary}']

    """

helps['sb namespace authorizationrule delete'] = """
    type: command
    short-summary: Deletes the AuthorizatioRule of the namespace.  
    examples:
        - name: Deletes the AuthorizatioRule of the namespace. 
          text: helps['sb namespace authorizationrule delete --resource-group {rg} --namespace-name {namespacename}
           --name {authoname}']

    """

helps['sb queue create'] = """
    type: command
    short-summary: Creates the ServiceBus Queue
    examples:
        - name: Create a new queue.
          text: helps['sb queue create --resource-group {rg} --namespace-name {namespacename} --name {queuename}']

    """

helps['sb queue get'] = """
    type: command
    short-summary: Get the Queue Details
    examples:
        - name: Get the Queue details.
          text: helps['sb queue get --resource-group {rg} --namespace-name {namespacename} --name {queuename}']

    """

helps['sb queue list'] = """
    type: command
    short-summary: List the Queueby Namepsace
    examples:
        - name: Get the Queues by Namespace.
          text: helps['sb queue list --resource-group {rg} --namespace-name {namespacename}']

    """

helps['sb queue delete'] = """
    type: command
    short-summary: Deletes the Queue
    examples:
        - name: Deletes the queue
          text: helps['sb queue delete --resource-group {rg} --namespace-name {namespacename} --name {queuename}']

    """

helps['sb queue authorizationrule create'] = """
    type: command
    short-summary: Creates Authorization rule for the given Queue 
    examples:
        - name: Creates Authorization rules
          text: helps['sb queue authorizationrule create --resource-group {rg} --namespace-name {namespacename}
           --queue-name {queuename}
           --name {authoname} --access-rights [Send, Listen]']

    """

helps['sb queue authorizationrule get'] = """
    type: command
    short-summary: Gets the details of AuthorizatioRule 
    examples:
        - name: Gets the details of AuthorizatioRule
          text: helps['sb queue authorizationrule get --resource-group {rg} --namespace-name {namespacename}
           --queue-name {queuename}
           --name {authoname}']

    """

helps['sb queue authorizationrule list'] = """
    type: command
    short-summary: Gets the list of AuthorizatioRule by Queue
    examples:
        - name: Gets the list of AuthorizatioRule by Queue
          text: helps['sb queue authorizationrule get --resource-group {rg} --namespace-name {namespacename}
           --queue-name {queuename}']

    """

helps['sb queue authorizationrule listkeys'] = """
    type: command
    short-summary: Gets the connectionstriongs of AuthorizatioRule for the Queue.  
    examples:
        - name: Gets the connectionstriongs of AuthorizatioRule for the queue.
          text: helps['sb queue authorizationrule listkeys --resource-group {rg} --namespace-name {namespacename}
           --queue-name {queuename}
           --name {authoname}']

    """

helps['sb queue authorizationrule regenerate_keys'] = """
    type: command
    short-summary: Regenerate the connectionstriongs of AuthorizatioRule for the namespace.  
    examples:
        - name: Regenerate the connectionstriongs of AuthorizatioRule for the namespace.
          text: helps['sb queue authorizationrule regenerate_keys --resource-group {rg} --namespace-name {namespacename}
           --queue-name {queuename}
           --name {authoname} --regeneratekey {primary}']

    """

helps['sb queue authorizationrule delete'] = """
    type: command
    short-summary: Deletes the AuthorizatioRule of the Queue.  
    examples:
        - name: Deletes the AuthorizatioRule of the queue. 
          text: helps['sb queue authorizationrule delete --resource-group {rg} --namespace-name {namespacename}
           --queue-name {queuename}
           --name {authoname}']

    """

helps['sb topic create'] = """
    type: command
    short-summary: Creates the ServiceBus Topic
    examples:
        - name: Create a new queue.
          text: helps['sb topic create --resource-group {rg} --namespace-name {namespacename} --name {topicname}']

    """

helps['sb topic get'] = """
    type: command
    short-summary: Get the Topic Details
    examples:
        - name: Get the Topic details.
          text: helps['sb topic get --resource-group {rg} --namespace-name {namespacename} --name {topicname}']

    """

helps['sb topic list'] = """
    type: command
    short-summary: List the Topic by Namepsace
    examples:
        - name: Get the Topics by Namespace.
          text: helps['sb topic list --resource-group {rg} --namespace-name {namespacename}']

    """

helps['sb topic delete'] = """
    type: command
    short-summary: Deletes the Topic
    examples:
        - name: Deletes the topic
          text: helps['sb topic delete --resource-group {rg} --namespace-name {namespacename} --name {topicname}']

    """

helps['sb topic authorizationrule create'] = """
    type: command
    short-summary: Creates Authorization rule for the given Topic 
    examples:
        - name: Creates Authorization rules
          text: helps['sb topic authorizationrule create --resource-group {rg} --namespace-name {namespacename}
           --topic-name {topicname}
           --name {authoname} --access-rights [Send, Listen]']

    """

helps['sb topic authorizationrule get'] = """
    type: command
    short-summary: Gets the details of AuthorizatioRule 
    examples:
        - name: Gets the details of AuthorizatioRule
          text: helps['sb topic authorizationrule get --resource-group {rg} --namespace-name {namespacename}
           --topic-name {topicname}
           --name {authoname}']

    """

helps['sb topic authorizationrule list'] = """
    type: command
    short-summary: Gets the list of AuthorizatioRule by Topic
    examples:
        - name: Gets the list of AuthorizatioRule by Topic
          text: helps['sb topic authorizationrule get --resource-group {rg} --namespace-name {namespacename}
           --topic-name {topicname}']

    """

helps['sb topic authorizationrule listkeys'] = """
    type: command
    short-summary: Gets the connectionstriongs of AuthorizatioRule for the Topic.  
    examples:
        - name: Gets the connectionstriongs of AuthorizatioRule for the topic.
          text: helps['sb topic authorizationrule listkeys --resource-group {rg} --namespace-name {namespacename}
           --topic-name {topicname}
           --name {authoname}']

    """

helps['sb topic authorizationrule regenerate_keys'] = """
    type: command
    short-summary: Regenerate the connectionstriongs of AuthorizatioRule for the Topic.  
    examples:
        - name: Regenerate the connectionstriongs of AuthorizatioRule for the Topic.
          text: helps['sb topic authorizationrule regenerate_keys --resource-group {rg} --namespace-name {namespacename}
           --topic-name {topicname}
           --name {authoname} --regeneratekey {primary}']

    """

helps['sb topic authorizationrule delete'] = """
    type: command
    short-summary: Deletes the AuthorizatioRule of the Topic.  
    examples:
        - name: Deletes the AuthorizatioRule of the topic. 
          text: helps['sb topic authorizationrule delete --resource-group {rg} --namespace-name {namespacename}
           --topic-name {topicname}
           --name {authoname}']

    """
helps['sb subscription create'] = """
    type: command
    short-summary: Creates the ServiceBus Subscription
    examples:
        - name: Create a new Subscription.
          text: helps['sb subscription create --resource-group {rg} --namespace-name {namespacename}
           --topic-name {topicname} --name {subscriptionname}']

    """

helps['sb subscription get'] = """
    type: command
    short-summary: Get the Subscription Details
    examples:
        - name: Get the Subscription details.
          text: helps['sb subscription get --resource-group {rg} --namespace-name {namespacename}
           --topic-name {topicname} --name {subscriptionname}']

    """

helps['sb subscription list'] = """
    type: command
    short-summary: List the Subscription by Topic
    examples:
        - name: Get the Subscription by Topic.
          text: helps['sb subscription list --resource-group {rg} --namespace-name {namespacename}']

    """

helps['sb subscription delete'] = """
    type: command
    short-summary: Deletes the Subscription
    examples:
        - name: Deletes the Subscription
          text: helps['sb subscription delete --resource-group {rg} --namespace-name {namespacename}
           --topic-name {topicname} --name {subscriptionname}']

    """

helps['sb rule create'] = """
    type: command
    short-summary: Creates the ServiceBus Rule for Subscription 
    examples:
        - name: Create a new Rule.
          text: helps['sb rule create --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname}
           --subscription-name {subscriptionname} --name {rulename} --filter-sql-expression {sqlexpression}']

    """

helps['sb rule get'] = """
    type: command
    short-summary: Get the Rule Details
    examples:
        - name: Get the Rule details.
          text: helps['sb rule get --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname}
           --subscription-name {subscriptionname} --name {rulename}']

    """

helps['sb rule list'] = """
    type: command
    short-summary: List the Rule by Subscription
    examples:
        - name: Get the Rule by Subscription.
          text: helps['sb rule list --resource-group {rg} --namespace-name {namespacename}
           --subscription-name {subscriptionname}']

    """

helps['sb rule delete'] = """
    type: command
    short-summary: Deletes the Rule
    examples:
        - name: Deletes the Rule
          text: helps['sb rule delete --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname}
           --subscription-name {subscriptionname} --name {rulename}']

    """

helps['sb alias check_name_availability'] = """
    type: command
    short-summary: Check the availability of the Alias (Geo DR Configuration) Name 
    examples:
        - name: Check the availability of the Alias (Geo DR Configuration) Name
          text: helps['sb alias check_name_availability --resource-group {rg} --namespace-name {namespacenameprimary}
           --alias {aliasname}']

    """

helps['sb alias create'] = """
    type: command
    short-summary: Creats Alias (Geo DR Configuration) for the give Namespace 
    examples:
        - name: Creats Alias (Geo DR Configuration) for the give Namespace
          text: helps['sb alias create  --resource-group {rg} --namespace-name {namespacenameprimary}
           --alias {aliasname} --partner-namespace {id}']

    """

helps['sb alias get'] = """
    type: command
    short-summary: Get details of Alias (Geo DR Configuration) for Primay/Secondary Namespace
    examples:
        - name:  Get details of Alias (Geo DR Configuration)  of the Primary Namespace 
          text: helps['sb alias get  --resource-group {rg} --namespace-name {namespacenameprimary}
           --alias {aliasname}']
		- name:  Get details of Alias (Geo DR Configuration)  of the Secondary Namespace 
          text: helps['sb alias get  --resource-group {rg} --namespace-name {namespacenamesecondary}
           --alias {aliasname}']

    """

helps['sb alias break_pairing'] = """
    type: command
    short-summary: Disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces
    examples:
        - name:  Disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces 
          text: helps['sb alias break_pairing  --resource-group {rg} --namespace-name {namespacenameprimary}
           --alias {aliasname}']

    """

helps['sb alias fail_over'] = """
    type: command
    short-summary: Envokes GEO DR failover and reconfigure the alias to point to the secondary namespace
    examples:
        - name:  Envokes GEO DR failover and reconfigure the alias to point to the secondary namespace 
          text: helps['sb alias fail_over  --resource-group {rg} --namespace-name {namespacenamesecondary}
           --alias {aliasname}']

    """

helps['sb alias delete'] = """
    type: command
    short-summary: Delete Alias(Disaster Recovery configuration) request accepted
    examples:
        - name:  Delete Alias(Disaster Recovery configuration) request accepted 
          text: helps['sb alias delete  --resource-group {rg} --namespace-name {namespacenamesecondary}
           --alias {aliasname}']

    """