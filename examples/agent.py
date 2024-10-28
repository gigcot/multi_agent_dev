from made.agent.service.agent_service_impl import AgentServiceImpl
from made.engine import ModelConfig
from made.engine.entity.ollama_config import OllamaConfig
from made.messages.entity.chat_message.user_message import UserChatMessage
from made.messages.entity.system_message.assistant_system_message import (
    AssistantSystemMessage,
)


class Chat:
    def __init__(self, model_config: ModelConfig):
        self.agent = AgentServiceImpl(
            system_message=system_message,
            model_config=model_config,
        )

    def run(self):
        while True:
            prompt = input("user:")

            if prompt.lower() == "exit":
                break

            if prompt.lower() == "reset":
                self.agent.agent_repository.reset()
                continue

            user_message = UserChatMessage(content=f"{prompt}")

            res = self.agent.step(user_message)

            print()
            print("assistant:\n", res.message.content)
            print()


if __name__ == "__main__":
    system_message = AssistantSystemMessage(
        content=f"You are a expert programmer. Your job is writting backlogs for development. \
You should only answer to the questions that asks about making backlogs",
    )
    model_config = OllamaConfig(
        base_url="https://si-follow.loca.lt/v1/", model="llama3.2"
    )
    chat = Chat(model_config)
    chat.run()
