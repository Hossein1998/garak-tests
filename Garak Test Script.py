import os

# Define models and parameters
models = [
    {"name": "gpt2", "max_length": 1024},
    {"name": "meta-llama/Llama-2-7b-chat-hf", "max_length": 4096}
]
probes = "ansiescape,dan,continuation,topic,glitch"
report_path = "/root/.local/share/garak/garak_runs/"
output_dir = "/content/"

# Install dependencies
os.system("pip install -U garak")
os.system("huggingface-cli login")

# Run tests on each model
for model in models:
    command = (
        f"python -m garak --model_type huggingface "
        f"--model_name {model['name']} "
        f"--generator_options '{{\"max_length\": {model['max_length']}}}' "
        f"--probes {probes}"
    )
    os.system(command)
    
    # Identify latest report
    report_files = [f for f in os.listdir(report_path) if f.endswith(".report.jsonl")]
    latest_report = max(report_files, key=lambda x: os.path.getctime(os.path.join(report_path, x)))
    
    # Copy reports to output directory
    os.system(f"cp {os.path.join(report_path, latest_report)} {output_dir}my_garak_report.jsonl")
    os.system(f"cp {os.path.join(report_path, latest_report.replace('.jsonl', '.html'))} {output_dir}my_garak_report.html")

print("All tests completed. Reports saved in", output_dir)
