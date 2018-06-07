# Copyright 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from networking_generic_switch.devices import netmiko_devices


class DellNos(netmiko_devices.NetmikoSwitch):
    """Netmiko device driver for Dell Force10 switches."""

    ADD_NETWORK = (
        'interface vlan {segmentation_id}',
        'name {network_id}',
        'exit',
    )

    DELETE_NETWORK = (
        'no interface vlan {segmentation_id}',
        'exit',
    )

    PLUG_PORT_TO_NETWORK = (
        'interface vlan {segmentation_id}',
        'untagged {port}',
        'exit',
    )

    DELETE_PORT = (
        'interface vlan {segmentation_id}',
        'no untagged {port}',
        'exit',
    )

    ADD_NETWORK_TO_TRUNK = (
        'interface vlan {segmentation_id}',
        'tagged {port}',
        'exit',
    )

    REMOVE_NETWORK_FROM_TRUNK = (
        'interface vlan {segmentation_id}',
        'no tagged {port}',
        'exit',
    )


class DellPowerConnect(netmiko_devices.NetmikoSwitch):
    """Netmiko device driver for Dell PowerConnect switches."""

    ADD_NETWORK = (
        'vlan database',
        'vlan {segmentation_id}',
        'exit',
    )

    DELETE_NETWORK = (
        'vlan database',
        'no vlan {segmentation_id}',
        'exit',
    )

    PLUG_PORT_TO_NETWORK = (
        'interface {port}',
        'switchport access vlan {segmentation_id}',
        'exit',
    )

    DELETE_PORT = (
        'interface {port}',
        'switchport access vlan none',
        'exit',
    )

    ADD_NETWORK_TO_TRUNK = (
        'interface {port}',
        'switchport general allowed vlan add {segmentation_id} tagged',
        'exit',
    )

    REMOVE_NETWORK_FROM_TRUNK = (
        'interface {port}',
        'switchport general allowed vlan remove {segmentation_id}',
        'exit',
    )
