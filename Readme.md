# Ansible Etcd role
Ansible role to install Etcd server.

## Variables
```yml
etcd_bin_dir: /opt/etcd/bin
etcd_config_dir: /etc/etcd
etcd_config_file_name: etcd.conf.yml
etcd_data_dir: "/var/lib/etcd/{{ inventory_hostname }}.etcd"
etcd_listen_interface: "{{}}"

etcd_version: 3.5.0

etcd_configuration:
  name: "{{ inventory_hostname }}"
  data_dir: "{{ etcd_data_dir }}"
  wal_dir: ""
  snapshot_count: 10000
  heartbeat_interval: 100
  election_timeout: 1000
  quota_backend_bytes: 0
  initial_advertise_peer_urls: "http://{{ ansible_facts['default_ipv4']['address'] }}:2380"
  advertise_client_urls: "http://{{ ansible_facts['default_ipv4']['address'] }}:2379"
  listen_peer_urls: "http://{{ ansible_facts['default_ipv4']['address'] }}:2380,http://localhost:2380"
  listen_client_urls: "http://{{ ansible_facts['default_ipv4']['address'] }}:2379,http://localhost:2379"
  max_snapshots: 5
  max_wals: 5
  cors: ""
  discovery: ""
  discovery_fallback: 'proxy'
  discovery_proxy: ""
  discovery_srv: ""
  initial_cluster: "{% for host in ansible_play_hosts_all %}{{ hostvars[host]['ansible_facts']['hostname'] }}=http://{{ hostvars[host]['ansible_facts']['default_ipv4']['address'] }}:2380{% if not loop.last %},{% endif %}{% endfor %}"
  initial_cluster_token: 'etcd_cluster'
  initial_cluster_state: 'new'
  strict_reconfig_check: "false"
  enable_pprof: "true"
  proxy: "off"
  proxy_failure_wait: 5000
  proxy_refresh_interval: 30000
  proxy_dial_timeout: 1000
  proxy_write_timeout: 5000
  proxy_read_timeout: 0
  client_transport_security:
    cert_file: ""
    key_file: ""
    client_cert_auth: false
    trusted_ca_file: ""
    auto_tls: false 
  peer_transport_security:
    cert_file: ""
    key_file: ""
    client_cert_auth: false
    trusted_ca_file: ""
    auto_tls: false
  self_signed_cert_validity: 1
  log_level: debug
  logger: zap
  log_outputs: [stderr]
  force_new_cluster: "false"
  auto_compaction_mode: periodic
  auto_compaction_retention: "1"
```