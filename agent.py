from personality import Personality
from llm import LLM
from tts import TTSModel

class Agent:
    def __init__(self, personality_short_name: str, llm_model: LLM, tts_model: TTSModel = None):
        self.personality = Personality(short_name=personality_short_name)

        self.llm_model = llm_model
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
            Не забывай соблюбать правила русского языка и пунктуации. Если в описании твоей личности есть черты грубого характера,
            то в твоих репликах могут быть грубые слова. Старайся, чтобы стиль ответа соответствовал твоей личности, возрасту и характеру.
        '''

        response = self.llm_model.generate_response(full_input)
        return response