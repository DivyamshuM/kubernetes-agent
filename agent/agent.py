import yaml
from agent.llm import ask_llm
from agent.k8s_tools import *
from agent.data_tools import *

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


config = yaml.safe_load(open("config.yaml"))
MODE = config["mode"]
NAMESPACE = config["namespace"]

def get_pods():
    if MODE == "live":
        return get_pods_live(NAMESPACE)
    return get_pods_local()

def get_logs(pod_name):
    if MODE == "live":
        return get_logs_live(pod_name, NAMESPACE)
    return get_logs_local(pod_name)

def describe_pod(pod_name):
    if MODE == "live":
        return describe_pod_live(pod_name, NAMESPACE)
    return describe_pod_local(pod_name)

def run_agent(question):
    print("[Agent] Understanding your request...\n")

    llm_output = ask_llm(question)
    print("[LLM Thought]\n", llm_output, "\n")

    pods = get_pods()

    # Determine action from LLM output
    action = None
    for line in llm_output.splitlines():
        if "get_logs" in line:
            action = "logs"
            break
        elif "describe_pod" in line:
            action = "describe"
            break

    # Find pod mentioned in LLM output
    target_pod = None
    for pod in pods:
        if pod in llm_output:
            target_pod = pod
            break

    if action and target_pod:
        if action == "logs":
            print(f"[Action] Fetching logs for {target_pod}")
            print(get_logs(target_pod))
        elif action == "describe":
            print(f"[Action] Describing {target_pod}")
            desc = describe_pod(target_pod)
            print(desc)
        return

    print("[Agent] No clear action detected.")