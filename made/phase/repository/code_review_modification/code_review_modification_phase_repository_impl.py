from made.chat_env.repository.chat_env_repository_impl import ChatEnvRepositoryImpl
from made.engine import ModelConfig
from made.phase.repository.base_phase_repository_impl import BasePhaseRepositoryImpl


class CodeReviewModificationPhaseRepositoryImpl(BasePhaseRepositoryImpl):
    def __init__(
        self,
        model_config: ModelConfig,
        phase_prompt: str,
        assistant_role_name: str,
        assistant_role_prompt: str,
        user_role_name: str,
        user_role_prompt: str,
        chat_turn_limit: int = 5
    ):
        super().__init__(
            model_config=model_config,
            phase_prompt=phase_prompt,
            assistant_role_name=assistant_role_name,
            assistant_role_prompt=assistant_role_prompt,
            user_role_name=user_role_name,
            user_role_prompt=user_role_prompt,
            chat_turn_limit=chat_turn_limit
        )

    def update_phase_states(self, env: ChatEnvRepositoryImpl):
        # TODO implement
        self.states.__dict__ = env.states.__dict__
        self.states.task = env.config.task_prompt
        self.states.description = env.states.task_description
        self.states.comments = env.states.review_comments
        pass

    def update_env_states(self, env: ChatEnvRepositoryImpl) -> ChatEnvRepositoryImpl:
        self.states.modification_conclusion = self.seminar_conclusion
        return env
