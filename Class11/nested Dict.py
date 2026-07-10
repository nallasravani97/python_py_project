model_registry = {
    "Llama-3": {
        "parameters": "70B",
        "layers": 80,
        "type": "Meta"},
    "GPT-4": {
        "parameters": "1.8T",
        "layers": 96,
        "type": "OpenAI"}
}

print(model_registry["Llama-3"]["parameters"])

for model_name, specs in model_registry.items():
    model_type = specs.get("type", "Unknown")
    print(f"Model: {model_name} | Type: {model_type}")