from made.engine.entity.ollama_config import OllamaConfig
from made.phase import PhaseRegistry
from made.phase.entity.phase_states import PhaseStates
from made.phase.repository.base_composed_phase_repository_impl import (
    BaseComposedPhaseRepositoryImpl,
)


@PhaseRegistry.register()
class InitCode(BaseComposedPhaseRepositoryImpl):
    def __init__(
        self,
        model_config=OllamaConfig(),
        phases=["DefaultCoding", "DefaultCodeComplete"],
        states=PhaseStates(),
        num_cycle=1,
    ):
        super().__init__(
            model_config=model_config, phases=phases, states=states, num_cycle=num_cycle
        )

    def update_phase_states(self, env):
        pass

    def update_env_states(self, env):
        pass

    def break_cycle(self, phase_states):
        pass
