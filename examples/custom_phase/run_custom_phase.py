from examples.custom_phase.example_phase import *
from made.chat_chain.service.chat_chain_service_impl import ChatChainServiceImpl


chain = ChatChainServiceImpl(
    task_prompt="Discuss about LLM multi agents.", directory="test", phases=["Example"]
)

chain.run()
