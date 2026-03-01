# Project Setup Guide

## Prerequisites

Before running the project, make sure the following tools are installed on your system:

* Python (recommended version 3.10+)
* Ollama


---

## 1. Setup Ollama

Install **Ollama** from the official website:

https://ollama.com/download

After installation, verify it is working:

```bash
ollama --version
```

---

## 2. Pull the LLM Model

This project uses the **llama3.2** model.

Download the model using:

```bash
ollama pull llama3.2
```

To confirm the model is available:

```bash
ollama list
```

---

## 3. Run Individual Agents

### Run Google Agent

To start the Google Agent using Google ADK:

```bash
adk web
```

This command launches the web interface for interacting with the agent.

---

## Notes

* Ensure Ollama is running before starting any agents.
* Make sure the required model (`llama3.2`) is successfully pulled.
* If `adk` command is not recognized, verify that Google ADK is properly installed and added to your system PATH.

---

## Troubleshooting

**Issue:** `adk is not recognized as an internal or external command`

**Solution:**

* Reinstall Google ADK
* Restart terminal
* Ensure Python Scripts directory is added to PATH

---

## Quick Start Summary

```bash
# Pull model
ollama pull llama3.2

# Run Google agent
adk web
```

---
