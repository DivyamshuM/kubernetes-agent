# Kubernetes Troubleshooting Agent

**Description:**
This project implements an AI-powered Kubernetes troubleshooting assistant that translates natural language queries into structured cluster debugging actions. The system uses a large language model to interpret user requests such as fetching pod logs, describing resources, or checking pod status. An agent orchestration layer validates the model’s output and safely executes only supported Kubernetes operations. The tool layer can operate in a local simulation mode using realistic logs and YAML files or connect to a live Kubernetes cluster. This architecture mirrors modern AI-assisted DevOps workflows and demonstrates how LLMs can be integrated into production-style troubleshooting systems.


---

## Features

- Natural language → Kubernetes command translation
- LLM reasoning layer for structured action planning
- Safe tool-calling with validation (prevents hallucination)
- Pod log retrieval
- Pod description and status inspection
- Local simulation mode using realistic production-style logs
- Live Kubernetes integration via Python client
- Modular architecture for future automation extensions

---

## Architecture

The system follows a three-layer agentic design:
- LLM Layer → Converts natural language into structured tool actions
- Agent Layer → Parses and validates LLM output
- Tool Layer → Fetches logs or pod data (local simulation or live cluster)

This separation ensures flexible reasoning while keeping execution safe and deterministic.

---

## Key Engineering Concepts Demonstrated

- Agentic AI architecture
- LLM tool calling
- Hallucination prevention via validation
- Kubernetes troubleshooting workflows
- Local simulation of cluster data
- Modular backend design

## Future Improvements

- Automated anomaly detection
- Multi-step root cause analysis
- Metrics export and monitoring
- Web UI for interactive debugging
- Multi-cluster support
