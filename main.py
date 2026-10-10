from agent import Agent
from dialog import Dialogue
from llm import LLM
from tts import TTSModel
from dotenv import load_dotenv
from bootstrap import prepare_run


load_dotenv()

def main():
    log_path = prepare_run()

    llm_model = LLM(model_title="deepseek/deepseek-v3.2")
    tts_model = TTSModel()

    agent1 = Agent(
        personality_short_name="aidar",
        llm_model=llm_model,
        tts_model=tts_model
    )

    agent2 = Agent(
        personality_short_name="eugene",
        llm_model=llm_model,
        tts_model=tts_model
    )

    dialogue = Dialogue(
        agent1=agent1,
        agent2=agent2,
        topics="Верна ли гипотеза Римана?",
        max_turns=8
    )

    dialogue_history = dialogue.main_loop()

    with open(log_path, 'w') as file:
        file.write(dialogue_history)

if __name__ == "__main__":
    main()