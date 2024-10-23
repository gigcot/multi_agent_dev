from made.chat_chain.service.chat_chain_service_impl import ChatChainServiceImpl


if __name__ == "__main__":
    chain = ChatChainServiceImpl(
        task_prompt="Develop a calculator app using python and tkinter",
        directory="test_dir",
        base_url="https://si-follow.loca.lt/v1/",
        model="llama3.2",
    )
    chain.run()
