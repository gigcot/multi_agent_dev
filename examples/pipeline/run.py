from examples.pipeline.phases import *
from examples.pipeline.states.env_states import ExampleEnvStates
from made.chat_chain.service.chat_chain_service_impl import ChatChainServiceImpl


if __name__ == "__main__":
    chain = ChatChainServiceImpl(
        task_prompt="Discuss about AI technologies.",
        directory="test_dir",
        base_url="https://si-follow.loca.lt/v1/",
        model="llama3.2",
        phases=["First", "Second"],
        env_states=ExampleEnvStates(),
    )
    chain.run()
