# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_servicebus(cli_ctx, **_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.servicebus import ServiceBusManagementClient
    return get_mgmt_service_client(cli_ctx, ServiceBusManagementClient)


def namespaces_mgmt_client_factory(cli_ctx, _):
    return cf_servicebus(cli_ctx).namespaces


def queues_mgmt_client_factory(cli_ctx, _):
    return cf_servicebus(cli_ctx).queues


def topics_mgmt_client_factory(cli_ctx, _):
    return cf_servicebus(cli_ctx).topics


def subscriptions_mgmt_client_factory(cli_ctx, _):
    return cf_servicebus(cli_ctx).subscriptions


def rules_mgmt_client_factory(cli_ctx, _):
    return cf_servicebus(cli_ctx).rules


def regions_mgmt_client_factory(cli_ctx, _):
    return cf_servicebus(cli_ctx).regions


def premium_messaging_mgmt_client_factory(cli_ctx, _):
    return cf_servicebus(cli_ctx).premium_messaging


def event_subscriptions_mgmt_client_factory(cli_ctx, _):
    return cf_servicebus(cli_ctx).event_subscriptions


def event_hubs_mgmt_client_factory(cli_ctx, _):
    return cf_servicebus(cli_ctx).event_hubs


def disaster_recovery_mgmt_client_factory(cli_ctx, _):
    return cf_servicebus(cli_ctx).disaster_recovery_configs
