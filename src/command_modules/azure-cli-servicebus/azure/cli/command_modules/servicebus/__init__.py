# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

import azure.cli.command_modules.servicebus._help  # pylint: disable=unused-import


class ServicebusCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.sdk.util import CliCommandType
        servicebus_custom = CliCommandType(operations_tmpl='azure.cli.command_modules.servicebus.custom#{}')
        super(ServicebusCommandsLoader, self).__init__(cli_ctx=cli_ctx, custom_command_type=servicebus_custom,
                                                    min_profile="2017-03-10-profile")

    def load_command_table(self, args):
        from azure.cli.command_modules.servicebus.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azure.cli.command_modules.servicebus._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = ServicebusCommandsLoader
