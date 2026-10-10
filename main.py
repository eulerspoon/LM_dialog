from agent import Agent
from dialog import Dialogue
from llm import LLM
from personality import Personality
from dotenv import load_dotenv

load_dotenv()

def main():
    llm_model = LLM(model_title="deepseek/deepseek-v3.2")
    print('OK')
    agent1 = Agent(
        personality_short_name="dan",
        llm_model=llm_model
    )

    agent2 = Agent(
        personality_short_name="alex",
        llm_model=llm_model
    )

    dialogue = Dialogue(
        agent1=agent1,
        agent2=agent2,
        topics="Поспорьте на предмет того, что круче: технические образование или математическое."
    )

    dialogue_history = dialogue.main_loop()
    print(dialogue_history)

if __name__ == "__main__":
    main()