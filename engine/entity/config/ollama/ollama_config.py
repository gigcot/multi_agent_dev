from dataclasses import dataclass


@dataclass
class OllamaConfig:
    base_url: str = "http://127.0.0.1:11434/v1/"
    model: str = "llama3.2"
    api_key: str = "ollama"
    max_tokens: int = 40000
