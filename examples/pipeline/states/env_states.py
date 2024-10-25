from dataclasses import field
from typing import Dict, List

from made.chat_env.entity.env_states import EnvStates


class ExampleEnvStates(EnvStates):
    state1: str = ""
    state2: str = ""
    state3: List[int] = field(default_factory=list)
    state4: Dict[str, str] = field(default_factory=dict)
