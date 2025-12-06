from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a Kubernetes troubleshooting agent.
You take user questions and decide which tool to run:
- get_logs(pod_name)
- describe_pod(pod_name)
- get_pods()
- get_status()
Return answers in a structured reasoning -> action -> output format.
"""

def ask_llm(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
