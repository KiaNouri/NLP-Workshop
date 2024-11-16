from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Initialize the LLM
llm = Ollama(
    model="qwen2.5:7b",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    temperature=1.0,
)

# Define a prompt template
# prompt = PromptTemplate.from_template("Translate the following English text to Farsi: {text}")

prompt = PromptTemplate.from_template("Sentiment analyze the following text from 0 (hioghly negative) to 5 (highly positive) and give the numeric confidence of the sentiment you recogniozed : {text}")


# Create an LLMChain with the prompt and model
chain = LLMChain(prompt=prompt, llm=llm)

# Input text for translation
input_text = "I love programming."

# Run the chain and get the translation
translation = chain.run({"text": input_text})



