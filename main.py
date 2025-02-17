import streamlit as st
from langchain_core.messages import AnyMessage, HumanMessage, ToolMessage, SystemMessage, AIMessage
from typing import List
from agent.graph import build_agent  # Assuming build_agent() initializes your Agent class

# Define AgentState-compatible conversation initialization
if "conversation" not in st.session_state:
    st.session_state.conversation: List[AnyMessage] = []

# Build the LangGraph workflow and agent
agent = build_agent()
graph = agent.graph

st.set_page_config(
    page_title="AI Agent",
    page_icon="🧊",
    layout="wide",
)

# Streamlit UI components
st.title("AI Agent with LangGraph")
user_input = st.text_input("Enter your message:")

if st.button("Send") and user_input:
    # Append user input as a HumanMessage to the conversation history
    st.session_state.conversation.append(HumanMessage(content=user_input))

    # Invoke the agent with the current state
    initial_state = {"messages": st.session_state.conversation}
    output = graph.invoke(initial_state)

    # Extract agent's response from the output and append it as a ToolMessage to the conversation history
    response_message = output["messages"][-1]  # Assuming the output contains a list of messages
    st.session_state.conversation.append(response_message)


# Display conversation history
for msg in st.session_state.conversation:
    if isinstance(msg, HumanMessage):
        st.write(f"User: {msg.content}")
    elif isinstance(msg, ToolMessage):
        st.write(f"Agent: {msg.content}")
    elif isinstance(msg, SystemMessage):
        st.write(f"System: {msg.content}")
    elif isinstance(msg, AIMessage):
        st.write(f"AI assistant: {msg.content}")
    
