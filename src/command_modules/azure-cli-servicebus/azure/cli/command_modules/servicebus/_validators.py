# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import re

from azure.cli.core.commands.validators import \
    (validate_tags, get_default_location_from_resource_group)
from azure.cli.core.commands.template_create import get_folded_parameter_validator
from azure.cli.core.commands.client_factory import get_subscription_id, get_mgmt_service_client
from azure.cli.core.commands.validators import validate_parameter_set
from azure.cli.core.profiles import ResourceType

from knack.util import CLIError

# PARAMETER VALIDATORS
# Type ISO 8061 duration

iso8601pattern = re.compile("^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d)(\d+H)?(\d+M)?(\d+.)?(\d+S)?)?$")


def _validate_lock_duration(namespace):
    if namespace.lock_duration:
        if not iso8601pattern.match(namespace.lock_duration):
            raise CLIError('--lock-duration Value Error : {0} value is not in ISO 8601 timespan/duration format. e.g.'
                           ' PT10M for duration of 10 min'.format(namespace.lock_duration))


def _validate_default_message_time_to_live(namespace):
    if namespace.default_message_time_to_live:
        if not iso8601pattern.match(namespace.default_message_time_to_live):
            raise CLIError('--default-message-time-to-live Value Error : {0} value is not in ISO 8601 timespan/duration'
                           ' format. e.g. PT10M for duration of 10 min'.format(namespace.default_message_time_to_live))


def _validate_duplicate_detection_history_time_window(namespace):
    if namespace.duplicate_detection_history_time_window:
        if not iso8601pattern.match(namespace.duplicate_detection_history_time_window):
            raise CLIError('--duplicate-detection-history-time-window Value Error : {0} value is not in ISO 8601 '
                           'timespan/duration format. e.g. PT10M for duration of 10 min'
                           .format(namespace.duplicate_detection_history_time_window))


def _validate_auto_delete_on_idle(namespace):
    if namespace.auto_delete_on_idle:
        if not iso8601pattern.match(namespace.auto_delete_on_idle):
            raise CLIError('--auto-delete-on-idle Value Error : {0} value is not in ISO 8601 timespan/duration format.'
                           ' e.g. PT10M for duration of 10 min'.format(namespace.auto_delete_on_idle))

