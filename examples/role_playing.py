from engine.entity.config.ollama.ollama_config import OllamaConfig
from role_playing.service.role_playing_service_impl import RolePlayingServiceImpl

if __name__ == "__main__":
    model_config = OllamaConfig(
        base_url="https://si-follow.loca.lt/v1/", model="llama3.2"
    )

    role_playing = RolePlayingServiceImpl(
        model_config=model_config,
        task_prompt="say only just one alphabet.",
        # task_prompt="Study partial derivative equation",
        background_prompt="We are best friends for 10 years from elementry school.",
        assistant_role_name="dave",
        assistant_role_prompt="{background_prompt} You are {assistant_role}, a student. {task} with {user_role}.",
        user_role_name="mark",
        user_role_prompt="{background_prompt} You are {user_role}, a student. {task} with {assistant_role}.",
    )

    _, user_message = role_playing.role_playing_repository.init_chat(
        phase_prompt="say an alphabet in alphabetical order on eachtime starting from a"
        # phase_prompt="Let's study"
    )
    print()
    print(f"\033[93m{user_message.role_name}\033[0m", ": ", user_message.content)
    for _ in range(13):
        assistant_response, user_response = role_playing.step(
            user_message=user_message, assistant_only=False
        )
        print()
        print(f"\033[93m{assistant_response.message.role_name}\033[0m", ": ", assistant_response.message.content)
        print()
        print(f"\033[93m{user_response.message.role_name}\033[0m", ": ", user_response.message.content)
        user_message = user_response.message
