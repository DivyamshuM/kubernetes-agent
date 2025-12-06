from kubernetes import client, config

def init_k8s():
    config.load_kube_config()
    return client.CoreV1Api()

v1 = None

def get_pods_live(namespace):
    global v1
    if v1 is None:
        v1 = init_k8s()
    pods = v1.list_namespaced_pod(namespace)
    return [p.metadata.name for p in pods.items]

def get_logs_live(pod_name, namespace):
    global v1
    if v1 is None:
        v1 = init_k8s()
    return v1.read_namespaced_pod_log(name=pod_name, namespace=namespace)

def describe_pod_live(pod_name, namespace):
    global v1
    if v1 is None:
        v1 = init_k8s()
    pod = v1.read_namespaced_pod(pod_name, namespace)
    return pod.to_dict()
