# Copyright 2012 Nebula, Inc.
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

from openstack_dashboard.test.test_data import utils

from neutron_vpnaas_dashboard.api import vpn


def data(TEST):
    # Data returned by neutron_vpnaas_dashboard.api.vpn wrapper.
    TEST.vpnservices = utils.TestDataContainer()
    TEST.ikepolicies = utils.TestDataContainer()
    TEST.ipsecpolicies = utils.TestDataContainer()
    TEST.ipsecsiteconnections = utils.TestDataContainer()

    # Data return by neutronclient.
    TEST.api_vpnservices = utils.TestDataContainer()
    TEST.api_ikepolicies = utils.TestDataContainer()
    TEST.api_ipsecpolicies = utils.TestDataContainer()
    TEST.api_ipsecsiteconnections = utils.TestDataContainer()

    # 1st VPNService.
    vpnservice_dict = {'id': '09a26949-6231-4f72-942a-0c8c0ddd4d61',
                       'tenant_id': '1',
                       'name': 'cloud_vpn1',
                       'description': 'vpn description',
                       'subnet_id': TEST.subnets.first().id,
                       'router_id': TEST.routers.first().id,
                       'vpn_type': 'ipsec',
                       'ipsecsiteconnections': [],
                       'admin_state_up': True,
                       'status': 'Active',
                       'ipsecsiteconns': TEST.ipsecsiteconnections.list()
                       }
    TEST.api_vpnservices.add(vpnservice_dict)
    TEST.vpnservices.add(vpn.VPNService(vpnservice_dict))

    # 2nd VPNService.
    vpnservice_dict = {'id': '09a26949-6231-4f72-942a-0c8c0ddd4d62',
                       'tenant_id': '1',
                       'name': 'cloud_vpn2',
                       'description': 'vpn description',
                       'subnet_id': TEST.subnets.first().id,
                       'router_id': TEST.routers.first().id,
                       'vpn_type': 'ipsec',
                       'ipsecsiteconnections': [],
                       'admin_state_up': True,
                       'status': 'Active',
                       'ipsecsiteconns': [],
                       'external_v4_ip': '10.0.0.0/24',
                       'external_v6_ip': 'fd4c:a535:831c::/64'
                       }
    TEST.api_vpnservices.add(vpnservice_dict)
    TEST.vpnservices.add(vpn.VPNService(vpnservice_dict))

    # 1st IKEPolicy
    ikepolicy_dict = {'id': 'a1f009b7-0ffa-43a7-ba19-dcabb0b4c981',
                      'tenant_id': '1',
                      'name': 'ikepolicy_1',
                      'description': 'ikepolicy description',
                      'auth_algorithm': 'sha1',
                      'encryption_algorithm': 'aes-256',
                      'ike_version': 'v1',
                      'lifetime': {'units': 'seconds', 'value': 3600},
                      'phase1_negotiation_mode': 'main',
                      'pfs': 'group5',
                      'ipsecsiteconns': TEST.ipsecsiteconnections.list()}
    TEST.api_ikepolicies.add(ikepolicy_dict)
    TEST.ikepolicies.add(vpn.IKEPolicy(ikepolicy_dict))

    # 2nd IKEPolicy
    ikepolicy_dict = {'id': 'a1f009b7-0ffa-43a7-ba19-dcabb0b4c982',
                      'tenant_id': '1',
                      'name': 'ikepolicy_2',
                      'description': 'ikepolicy description',
                      'auth_algorithm': 'sha1',
                      'encryption_algorithm': 'aes-256',
                      'ike_version': 'v1',
                      'lifetime': {'units': 'seconds', 'value': 3600},
                      'phase1_negotiation_mode': 'main',
                      'pfs': 'group5',
                      'ipsecsiteconns': []}
    TEST.api_ikepolicies.add(ikepolicy_dict)
    TEST.ikepolicies.add(vpn.IKEPolicy(ikepolicy_dict))

    # 1st IPSecPolicy
    ipsecpolicy_dict = {'id': '8376e1dd-2b1c-4346-b23c-6989e75ecdb8',
                        'tenant_id': '1',
                        'name': 'ipsecpolicy_1',
                        'description': 'ipsecpolicy description',
                        'auth_algorithm': 'sha1',
                        'encapsulation_mode': 'tunnel',
                        'encryption_algorithm': '3des',
                        'lifetime': {'units': 'seconds', 'value': 3600},
                        'pfs': 'group5',
                        'transform_protocol': 'esp',
                        'ipsecsiteconns': TEST.ipsecsiteconnections.list()}
    TEST.api_ipsecpolicies.add(ipsecpolicy_dict)
    TEST.ipsecpolicies.add(vpn.IPSecPolicy(ipsecpolicy_dict))

    # 2nd IPSecPolicy
    ipsecpolicy_dict = {'id': '8376e1dd-2b1c-4346-b23c-6989e75ecdb9',
                        'tenant_id': '1',
                        'name': 'ipsecpolicy_2',
                        'description': 'ipsecpolicy description',
                        'auth_algorithm': 'sha1',
                        'encapsulation_mode': 'tunnel',
                        'encryption_algorithm': '3des',
                        'lifetime': {'units': 'seconds', 'value': 3600},
                        'pfs': 'group5',
                        'transform_protocol': 'esp',
                        'ipsecsiteconns': []}
    TEST.api_ipsecpolicies.add(ipsecpolicy_dict)
    TEST.ipsecpolicies.add(vpn.IPSecPolicy(ipsecpolicy_dict))

    # 1st IPSecSiteConnection
    ipsecsiteconnection_dict = {'id': 'dd1dd3a0-f349-49be-b013-245e147763d6',
                                'tenant_id': '1',
                                'name': 'ipsec_connection_1',
                                'description': 'vpn connection description',
                                'dpd': {'action': 'hold',
                                        'interval': 30,
                                        'timeout': 120},
                                'ikepolicy_id': ikepolicy_dict['id'],
                                'initiator': 'bi-directional',
                                'ipsecpolicy_id': ipsecpolicy_dict['id'],
                                'mtu': 1500,
                                'peer_address':
                                '2607:f0d0:4545:3:200:f8ff:fe21:67cf',
                                'peer_cidrs': ['20.1.0.0/24', '21.1.0.0/24'],
                                'peer_id':
                                    '2607:f0d0:4545:3:200:f8ff:fe21:67cf',
                                'psk': 'secret',
                                'vpnservice_id': vpnservice_dict['id'],
                                'admin_state_up': True,
                                'status': 'Active'}
    TEST.api_ipsecsiteconnections.add(ipsecsiteconnection_dict)
    TEST.ipsecsiteconnections.add(
        vpn.IPSecSiteConnection(ipsecsiteconnection_dict))

    # 2nd IPSecSiteConnection
    ipsecsiteconnection_dict = {'id': 'dd1dd3a0-f349-49be-b013-245e147763d7',
                                'tenant_id': '1',
                                'name': 'ipsec_connection_2',
                                'description': 'vpn connection description',
                                'dpd': {'action': 'hold',
                                        'interval': 30,
                                        'timeout': 120},
                                'ikepolicy_id': ikepolicy_dict['id'],
                                'initiator': 'bi-directional',
                                'ipsecpolicy_id': ipsecpolicy_dict['id'],
                                'mtu': 1500,
                                'peer_address': '172.0.0.2',
                                'peer_cidrs': ['20.1.0.0/24'],
                                'peer_id': '172.0.0.2',
                                'psk': 'secret',
                                'vpnservice_id': vpnservice_dict['id'],
                                'admin_state_up': True,
                                'status': 'Active'}
    TEST.api_ipsecsiteconnections.add(ipsecsiteconnection_dict)
    TEST.ipsecsiteconnections.add(
        vpn.IPSecSiteConnection(ipsecsiteconnection_dict))
