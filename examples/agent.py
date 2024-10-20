from agent.service.agent_service_impl import AgentServiceImpl
from engine import ModelConfig
from engine.entity.config.ollama.ollama_config import OllamaConfig
from messages.entity.chat_message.user_message import UserChatMessage
from messages.entity.system_message.base_system_message import BaseSystemMessage


class Chat:
    def __init__(self, model_config: ModelConfig):
        self.engine = AgentServiceImpl(
            system_message=system_message,
            model_config=model_config,
        )

    def run(self):
        while True:
            prompt = input("user:")

            if prompt.lower() == "exit":
                break

            user_message = UserChatMessage(
                role_name="onebottlekick", content=f"{prompt}"
            )

            res = self.engine.step(user_message)

            print()
            print("assistant:\n", res.message.content)
            print()


if __name__ == "__main__":
    system_message = BaseSystemMessage(
        role_name="Han",
        content=f"You are a expert programmer. Your job is writting backlogs for development. \
You should only answer to the questions that asks about making backlogs",
    )
    model_config = OllamaConfig()
    chat = Chat(model_config)
    chat.run()
