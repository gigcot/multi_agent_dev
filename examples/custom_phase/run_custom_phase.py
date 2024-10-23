from examples.custom_phase.example_phase import *
from made.phase.service.phase_service_impl import PhaseServiceImpl
from made.engine.entity.ollama_config import OllamaConfig
from made.chat_env.entity.env_config import EnvConfig
from made.chat_env.repository.chat_env_repository_impl import ChatEnvRepositoryImpl


model_config = OllamaConfig(base_url="https://si-follow.loca.lt/v1/")
phase_service = PhaseServiceImpl(model_config=model_config)
env = ChatEnvRepositoryImpl(EnvConfig(task_prompt="discuss"))
custom_phase = phase_service.get_phase(
    phase_name="Example",
)

custom_phase.execute(env=env)