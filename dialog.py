from agent import Agent
import time


class Dialogue:
    def __init__(
        self,
        agent1: Agent,
        agent2: Agent,
        topics: str,
        max_turns: int = 4,
        whose_turn_now: int = 1
    ):
        self.agent1 = agent1
        self.agent2 = agent2

        
        self.topics = topics
        self.max_turns = max_turns
        self.whose_turn_now = whose_turn_now

        self.turns = 0
        self.history = []

    def stringify_conversation_history(self) -> str:
        conversation_history = "Тема диалога: " + self.topics + "\n\n"
        for agent, turn in self.history:
            short_name = self.agent1.personality.short_name if agent == 1 else self.agent2.personality.short_name
            turn_info = f"{short_name}: {turn}\n"
            conversation_history += turn_info
        
        return conversation_history

    def main_loop(self):
        agent1_personality_info = self.agent1.personality.get_personality_info()
        agent2_personality_info = self.agent2.personality.get_personality_info()

        while self.turns < self.max_turns:
            time.sleep(2)
            conversation_history = self.stringify_conversation_history()
            if self.whose_turn_now == 1:
                response = self.agent1.say(conversation_history, agent2_personality_info)
            else:
                response = self.agent2.say(conversation_history, agent1_personality_info)

            turn = (self.whose_turn_now, response)
            print(self.whose_turn_now, response, '\n\n')
            self.history.append(turn)
            self.turns += 1
            self.whose_turn_now = 2 if self.whose_turn_now == 1 else 1

        return self.history