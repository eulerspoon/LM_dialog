from agent import Agent
import threading
from queue import Queue


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
        llm_queue = Queue()
        tts_queue = Queue()

        def llm_worker():
            history = []
            for turn_idx in range(self.max_turns):
                agent = self.agent1 if self.whose_turn_now == 1 else self.agent2
                opponent = self.agent2 if self.whose_turn_now == 1 else self.agent1

                hist_str = self.stringify_conversation_history()
                opponent_info = opponent.personality.get_personality_info()

                response = agent.say(hist_str, opponent_info)
                print(f"{turn_idx + 1}. {agent.personality.short_name}: {response}\n")

                history.append((self.whose_turn_now, response))
                llm_queue.put((turn_idx, agent, response))

                self.whose_turn_now = 2 if self.whose_turn_now == 1 else 1

            self.history = history
            llm_queue.put('END')

        def tts_worker():
            while True:
                item = llm_queue.get()
                if item == 'END':
                    tts_queue.put('END')
                    return
                turn_idx, agent, response = item
                wav = f"wav/turn{turn_idx + 1}.wav"
                agent.tts_model.synthesize_speech(
                    response,
                    speaker=agent.personality.short_name,
                    output=wav,
                )
                tts_queue.put((turn_idx, agent, wav))

        t_llm = threading.Thread(target=llm_worker, daemon=True)
        t_tts = threading.Thread(target=tts_worker, daemon=True)

        t_llm.start()
        t_tts.start()

        while True:
            item = tts_queue.get()
            if item == 'END':
                break
            _, agent, wav = item
            agent.speak(wav)
            self.turns += 1

        t_llm.join()
        t_tts.join()

        return self.stringify_conversation_history()