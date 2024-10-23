from chat_chain.repository.chat_chain_repository_impl import ChatChainRepositoryImpl
from chat_chain.service.chat_chain_service import ChatChainService
from chat_env.entity.env_config import EnvConfig
from chat_env.entity.env_states import EnvStates
from chat_env.repository.chat_env_repository_impl import ChatEnvRepositoryImpl
from engine.entity.config.ollama.ollama_config import OllamaConfig
from phase.service.phase_service_impl import PhaseServiceImpl


class ChatChainServiceImpl(ChatChainService):
    def __init__(
        self,
        task_prompt: str,
        directory: str,
        base_url: str = "http://127.0.0.1:11434/v1/",
        model: str = "llama3.2",
        api_key: str = "ollama",
        max_tokens: int = 40000
    ):
        self.model_config = OllamaConfig(base_url=base_url, model=model, api_key=api_key, max_tokens=max_tokens)
        self.chat_chain_repository = ChatChainRepositoryImpl()
        self.phase_service = PhaseServiceImpl(
            model_config=self.model_config,
        )
        
        env_config = EnvConfig(task_prompt=task_prompt, directory=directory)
        env_states = EnvStates()
        # env_states = EnvStates(modality="application", language="python")
        self.env = ChatEnvRepositoryImpl(env_config=env_config, env_states=env_states)
        self.phases = self.get_phases()

    def get_phases(self):
        phases = [
            self.phase_service.get_demand_analysis_phase(),
            self.phase_service.get_language_choose_phase(),
            self.phase_service.get_coding_phase(),
            self.phase_service.get_code_complete_phase(),
            self.phase_service.get_code_review_comment_phase(),
            self.phase_service.get_code_review_modification_phase(),
            self.phase_service.get_test_error_summary_phase(),
            self.phase_service.get_test_modification_phase(),
            self.phase_service.get_manual_phase(),
        ]
        return phases

    def run(self):
        self.chat_chain_repository.preprocessing()
        self.chat_chain_repository.execute_chain(env=self.env, phases=self.phases)
        self.chat_chain_repository.postprocessing()
