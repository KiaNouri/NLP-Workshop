#pip install langchain
#pip install -U langchain-community
#pip install langchain-experimental
#pip install ollama
#ollama pull mistral
#ollama list

from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(
    model='mistral',
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    temperature = 0.9
)


prompt = PromptTemplate(
    input_variables=["topic"],
    template="Give me 3 most important facts about {topic}"
)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("LLMs"))
