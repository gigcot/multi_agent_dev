from openai.types.chat.chat_completion import ChatCompletion

from made.engine import ModelConfig
from made.engine.repository.ollama.ollama_engine_repository_impl import (
    OllamaEngineRepositoryImpl,
)
from made.engine.service.base_engine_service import BaseEngineService


class OllamaEngineServiceImpl(BaseEngineService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__ollama_engine_repository = (
                OllamaEngineRepositoryImpl.get_instance()
            )

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def run(self, messages, ollama_config: ModelConfig) -> ChatCompletion:
        engine = self.__ollama_engine_repository.get_engine(ollama_config)

        response = engine.chat.completions.create(
            model=ollama_config.model,
            messages=messages,
            max_tokens=ollama_config.max_tokens,
        )

        return response
