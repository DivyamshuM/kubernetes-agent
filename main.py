from agent.agent import run_agent

print("\n=== Kubernetes Troubleshooting Agent ===\n")

while True:
    q = input("> ")
    if q.lower() in ["exit", "quit"]:
        break
    run_agent(q)
