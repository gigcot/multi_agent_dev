from examples.custom_phase.example_phase import *
from made.chat_chain.service.chat_chain_service_impl import ChatChainServiceImpl


if __name__ == "__main__":
    chain = ChatChainServiceImpl(
        task_prompt="Discuss about AI technologies.",
        directory="test_dir",
        base_url="https://si-follow.loca.lt/v1/",
        model="llama3.2",
        phases=["Example"]
    )
    chain.run()
