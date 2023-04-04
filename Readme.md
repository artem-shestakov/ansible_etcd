# Ansible Etcd role
Ansible role to install Etcd server.

## Variables
### Installation variables
* `etcd_bin_dir` - directory to install Etcd binary. default: `/usr/local/bin/`
* `etcd_config_dir` - directory with Etcd configuration file. Default: `/etc/etcd`
* `etcd_config_file_name` - the name of configuration file. Default: `etcd.conf.yml`
* `etcd_data_dir` - directory to store data. Default: `/var/lib/etcd/{{ inventory_hostname }}.etcd`
* `etcd_version` - version to install. Default: `3.5.0`

### Configuration variables
```yml
etcd_name: "{{ inventory_hostname }}"
etcd_wal_dir: ""
etcd_snapshot_count: 10000
etcd_heartbeat_interval: 100
etcd_election_timeout: 1000
etcd_quota_backend_bytes: 0
etcd_initial_advertise_peer_urls: "http://{{ ansible_facts['default_ipv4']['address'] }}:2380"
etcd_advertise_client_urls: "http://{{ ansible_facts['default_ipv4']['address'] }}:2379"
etcd_listen_peer_urls: "http://{{ ansible_facts['default_ipv4']['address'] }}:2380,http://localhost:2380"
etcd_listen_client_urls: "http://{{ ansible_facts['default_ipv4']['address'] }}:2379,http://localhost:2379"
etcd_max_snapshots: 5
etcd_max_wals: 5
etcd_cors: ""
etcd_discovery: ""
etcd_discovery_fallback: 'proxy'
etcd_discovery_proxy: ""
etcd_discovery_srv: ""
etcd_initial_cluster: "{% for host in ansible_play_hosts_all %}{{ hostvars[host]['ansible_facts']['hostname'] }}=http://{{ hostvars[host]['ansible_facts']['default_ipv4']['address'] }}:2380{% if not loop.last %},{% endif %}{% endfor %}"
etcd_initial_cluster_token: 'etcd_cluster'
etcd_initial_cluster_state: 'new'
etcd_strict_reconfig_check: "false"
etcd_enable_pprof: "true"
etcd_proxy: "off"
etcd_proxy_failure_wait: 5000
etcd_proxy_refresh_interval: 30000
etcd_proxy_dial_timeout: 1000
etcd_proxy_write_timeout: 5000
etcd_proxy_read_timeout: 0
etcd_client_cert_file: ""
etcd_client_key_file: ""
etcd_client_client_cert_auth: false
etcd_client_trusted_ca_file: ""
etcd_client_auto_tls: false 
etcd_transport_cert_file: ""
etcd_transport_key_file: ""
etcd_transport_client_cert_auth: false
etcd_transport_trusted_ca_file: ""
etcd_transport_auto_tls: false
etcd_self_signed_cert_validity: 1
etcd_log_level: debug
etcd_logger: zap
etcd_log_outputs: [stderr]
etcd_force_new_cluster: "false"
etcd_auto_compaction_mode: periodic
etcd_auto_compaction_retention: "1"
```