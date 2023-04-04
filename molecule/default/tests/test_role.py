import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config_file(host):
    config = host.file("/etc/etcd/etcd.conf.yml")
    assert config.exists
    assert config.is_file
    assert config.user == 'etcd'
    assert config.mode == 0o600

def test_service(host):
    etcd = host.service("etcd")
    assert etcd.is_running
    assert etcd.is_enabled

def test_socket(host):
    assert host.socket(f"tcp://{host.interface('eth0').addresses[0]}:2379").is_listening
    assert host.socket(f"tcp://{host.interface('eth0').addresses[0]}:2380").is_listening