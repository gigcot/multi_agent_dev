from made.chat_env.entity.env_config import EnvConfig
from made.chat_env.entity.env_states import EnvStates
from made.chat_env.repository.chat_env_repository_impl import ChatEnvRepositoryImpl
from made.engine.entity.ollama_config import OllamaConfig
from made.phase.service.phase_service_impl import PhaseServiceImpl

if __name__ == "__main__":
    phase_service = PhaseServiceImpl(
        model_config=OllamaConfig(
            base_url="https://si-follow.loca.lt/v1/", model="llama3.2"
        ),
    )

    env = ChatEnvRepositoryImpl(
        env_config=EnvConfig(task_prompt="develop a simple calculator in python"),
        env_states=EnvStates(),
    )

    phases = [
        phase_service.get_demand_analysis_phase(),
        phase_service.get_language_choose_phase(),
        phase_service.get_coding_phase(),
        phase_service.get_code_complete_phase(),
        phase_service.get_code_review_comment_phase(),
        phase_service.get_code_review_modification_phase(),
        phase_service.get_test_error_summary_phase(),
        phase_service.get_test_modification_phase(),
        phase_service.get_manual_phase(),
    ]

    for phase in phases:
        phase.execute(env=env)
        print()
        print("phase states:")
        print(phase.states)
        print()
        print("env states: ")
        print(env.states)
        print()
