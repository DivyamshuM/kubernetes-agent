import json
import os
import yaml

BASE = "data"

def get_pods_local():
    pods_file = f"{BASE}/pods.json"
    with open(pods_file) as f:
        return json.load(f)["pods"]

def get_logs_local(pod_name):
    path = f"{BASE}/logs/{pod_name}.log"
    if not os.path.exists(path):
        return "No logs found."
    return open(path).read()

def describe_pod_local(pod_name):
    path = f"{BASE}/descriptions/{pod_name}_desc.yaml"
    if not os.path.exists(path):
        return {}
    return yaml.safe_load(open(path))
