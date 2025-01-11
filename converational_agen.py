import os
# If using a .env file for your API key:
#from dotenv import load_dotenv
#load_dotenv()

from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


OPENAI_API_KEY="Yor API KEY"
# 1) Create an LLM wrapper:
#    "temperature=0.7" for more creative answers, "max_tokens" can be tuned as well
llm = OpenAI(
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")  # or "sk-xxxx" directly (not recommended)
)

# 2) Create memory to store conversation so the model can recall context:
memory = ConversationBufferMemory()

# 3) Create a conversation chain that uses the LLM and memory
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True  # If True, will print out the conversation steps
)

# 4) Start interacting with your conversation chain
user_input_1 = "Hello! Who are you?"
reply_1 = conversation.run(user_input_1)
print("Assistant:", reply_1)

user_input_2 = "Can you tell me a short joke?"
reply_2 = conversation.run(user_input_2)
print("Assistant:", reply_2)

# 5) The chain remembers context, so let's reference something from earlier
user_input_3 = "Repeat that joke, but in a more poetic style."
reply_3 = conversation.run(user_input_3)
print("Assistant:", reply_3)
