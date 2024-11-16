from langchain_ollama import OllamaLLM

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('sales_data.csv')

# Initialize the LLM
llm = OllamaLLM(
    model="qwen2.5:7b",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    temperature=1.0,
)

# Helper function for creating structured prompts
def structured_prompt(query):
    return f"{query} Please provide the output in JSON format enclosed in a markdown code block."

# Agent 1: Find products with sales more than 1000
agent1 = create_pandas_dataframe_agent(
    llm, 
    df, 
    allow_dangerous_code=True, 
    handle_parsing_errors=True, 
    verbose=True
)
result1 = agent1.run(structured_prompt("List all products with sales greater than 1000."))
print("-------------- Products with sales > 1000:")
print(result1)


# Agent 2: Find products with profits more than 200
agent2 = create_pandas_dataframe_agent(
    llm, 
    df, 
    allow_dangerous_code=True, 
    handle_parsing_errors=True, 
    verbose=True
)
result2 = agent2.run(structured_prompt("List all products with profits greater than 200."))
print("\n ------------------------ Products with profits > 200:")
print(result2)

# Convert results to DataFrames (assuming the result is a JSON or dictionary-like format)
df1 = pd.DataFrame(result1)
df2 = pd.DataFrame(result2)
# Find common products
common_products = pd.merge(df1, df2, on='ProductID')

# Agent 3: List the distribution of regions for common products
agent3 = create_pandas_dataframe_agent(
    llm, 
    common_products, 
    allow_dangerous_code=True, 
    handle_parsing_errors=True, 
    verbose=True
)
region_distribution = agent3.run(structured_prompt("Provide the distribution of regions for the listed products."))
print("\nRegion distribution for common products:")
print(region_distribution)



