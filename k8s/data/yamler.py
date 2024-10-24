from functools import lru_cache

import yaml
import os


daemon_set_path = os.environ.get("DAEMON_SET_PATH", "k8s/data/daemon_set.yaml")


@lru_cache
def load_yaml(file_path: str) -> dict:
    with open(file_path, "r") as fp:
        return yaml.safe_load(stream=fp)


def load_instance_types() -> dict:
    data = load_yaml(file_path="k8s/data/instance_type.yaml")
    return data["EC2"]


def load_daemon_set(path: str = daemon_set_path) -> dict:
    data = load_yaml(file_path=path)
    return data["daemon_set"]
