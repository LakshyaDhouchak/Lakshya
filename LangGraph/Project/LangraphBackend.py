from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

load_dotenv()
model =  ChatOllama(model = 'minimax-m3:cloud', temperature=0.5)

# define the state
class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]

# define the methord
def chat_node(State: ChatState):
    messages= State['messages']
    response = model.invoke(messages)
    return {'messages': [response]}

# calling the checkpointer
checkpointer = InMemorySaver()

# calling the graph
graph = StateGraph(ChatState)
# add node
graph.add_node('chat_node', chat_node)
# add edge
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node', END)

chatbot=graph.compile(checkpointer= checkpointer)
