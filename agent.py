from personality import Personality
from LLM import LLM
from TTS import TTSModel

class Agent:
    def __init__(self, personality: Personality, llm_model: LLM, tts_model: TTSModel = None):
        self.llm_model = llm_model
        self.personality = personality
        self.tts_model = tts_model

    def say(
        self,
        conversation_history: str,
        opponent_personality_info: str
    ) -> str:
        my_personality_info = self.personality.get_personality_info()

        full_input = f'''
            Вот информация о тебе: {my_personality_info}. Ты ведёшь диалог с собеседником.
            "Вот информация о твоём собеседнике:" + \
            "\n\n" + {opponent_personality_info}.
            Тебе нужно продолжить диалог, учитывая информацию о собеседнике и историю диалога.
            Вот история вашего диалога: {conversation_history}.
            Скажи что-нибудь в ответ: {self.personality.short_name}: ..?
            В твоём ответе должны быть только слова, которые ты произнесёшь. Не добавляй никаких пояснений, комментариев или описаний действий.
        '''

        response = self.llm_model.generate_response(full_input, self.personality)
        return response