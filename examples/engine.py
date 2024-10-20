import logging
import time
from concurrent import futures

from engine.entity.config.ollama.ollama_config import OllamaConfig
from engine.service.ollama.ollama_engine_service_impl import OllamaEngineServiceImpl

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def run_service(messages, config):
    logging.info(f"Starting service with config: {config.base_url}")
    start_time = time.time()

    ollama_engine_service = OllamaEngineServiceImpl.get_instance()
    result = ollama_engine_service.run(messages, config)

    end_time = time.time()
    logging.info(
        f"Finished service with config: {config.base_url} in {end_time - start_time:.2f} seconds"
    )

    return result


if __name__ == "__main__":
    ollama_engine_service = OllamaEngineServiceImpl.get_instance()
    ollama_config1 = OllamaConfig(
        base_url="https://si-follow.loca.lt/v1/", model="llama3.1"
    )
    ollama_config2 = OllamaConfig(
        base_url="https://si-follow.loca.lt/v1/", model="llama3.2"
    )

    messages = [{"role": "user", "content": "why is the sky blue?"}]

    with futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(run_service, messages, ollama_config1)
        future2 = executor.submit(run_service, messages, ollama_config2)

        res1 = future1.result()
        res2 = future2.result()
