from agent import Agent
from dialog import Dialogue
from llm import LLM
from tts import TTSModel
from dotenv import load_dotenv


load_dotenv()

def main():
    llm_model = LLM(model_title="deepseek/deepseek-v3.2")
    tts_model = TTSModel()

    agent1 = Agent(
        personality_short_name="aidar",
        llm_model=llm_model,
        tts_model=tts_model
    )

    agent2 = Agent(
        personality_short_name="xenia",
        llm_model=llm_model,
        tts_model=tts_model
    )

    dialogue = Dialogue(
        agent1=agent1,
        agent2=agent2,
        topics="Поговорите на тему поэзии. Что для вас поэзия? Какой любимый поэт?",
        max_turns=8
    )

    dialogue_history = dialogue.main_loop()
    print(dialogue_history)

if __name__ == "__main__":
    main()