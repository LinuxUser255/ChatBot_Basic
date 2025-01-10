#!/usr/bin/env python3

from langchain.chains.question_answering import chain
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Embedding the variable inside the prompt, to be passed to the model via {context}
template = """"
Answer the question below:
Here is the conversation history: {context}
Question: {input}
Answer:
"""

model = OllamaLLM(model="llama3.1")
prompt = ChatPromptTemplate.from_template(template)
# chain the prompt and model using langchain. Pass the prompt to the model
chain = prompt | model

def convo_handle():
    context = ""
    print("Welcome to the AI Assistant. How may I help you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            break
            # Generating a response from the chain using the provided context and user input
        response = chain.invoke({"context": context, "input": user_input})
        print(f"Assistant: {response}")
        context += f"\nUser: {user_input}\nAssistant: {response} \n\n"

def main():
    convo_handle()

if __name__ == '__main__':
    main()
