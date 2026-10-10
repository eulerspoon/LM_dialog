# LM Dialog

One day, CS student was bored on the weekend...

<h2>Entities</h2>

<h3>Personality</h3>

Agent personality.

- full name.
- age.
- profession.
- language.
- character, other info.

<h3>LLM Model</h3>
init(name)
answer(prompt)

<h3>TTS Model (wrapper)</h3>
init(url tts api, wav location)
transcribe

<h3>Agent</h3>

init(personality, llm model, tts model)




<h3>Dialog</h3>

init(agent1, agent2)
start conversation


More: Multithread. One thred for each agent.
<h3>Architecture</h3>
main.py
two agents init
dialog init and start

agent.py
agent class

personality.py
class personality
get personality func (name) -> personality (json read)

personalities.json
data...


<h3>Models</h3>
- LLM (api) - model choice based on request speed, no more criterions yet!!!
	context - sysprompt with personality characteristics and dialogue history
- TTS (localhost api) - or mb two different? get model from devops lab1!
	requests on different threads.



