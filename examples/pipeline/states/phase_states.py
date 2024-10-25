from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class ExamplePhaseStates:
    state1: str = ""
    state2: str = ""
    state3: List[int] = field(default_factory=list)
    state4: Dict[str, str] = field(default_factory=dict)
