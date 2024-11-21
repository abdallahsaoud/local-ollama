import subprocess

def query_ollama(prompt, model="llama3.2"):
    process = subprocess.run(
        ['ollama', 'run', model, prompt],
        capture_output=True,
        text=True
    )
    return process.stdout.strip()
