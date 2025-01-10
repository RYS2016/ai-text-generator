#Web based loader
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.llms import openai
from langchain.chains import ConversationalRetrievalChain

url = "http://....."
#Load the info from website
loader = WebBaseLoader(url)
#document object. it wll load the text from url and convert into langchain document
raw_documents = loader.load()
#chank up the data into a small pieces to make sure we only pass the smallest,
#most relevant pieces of text to the language model
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(raw_documents)
#then we can create our embeddings for each piece of text and store them
embeddings = OpenAIEmbeddings(openai_api_key = api_key)
#create a vector store
vectorstore = FAISS.from_documents(documents, embeddings)
#creating a memory object, to track the inputs and outputs, and for the model to hold a conversation
memory = ConversationBufferMemory(memory_key = "chat_history", return_messages=True)
#Initialize the conversational retrieval chain.This chain first combines the chat history and the question asked to the model into a standalone question.
#It then looks up the relevant documents from the retriever, and finally passes those documents and
#the question to a question answering chain to return the correct response.
#let's set up our chain. We will use conversational retrival chain from LM.
qa = ConversationalRetrievalChain.from_llm(openai(openai_api_key, temperature=0), vectorstore.as_retriever(), memory=memory)
#Now we can ask our model
query = "What is ....."
result = qa({"question": query})
result["answer"]