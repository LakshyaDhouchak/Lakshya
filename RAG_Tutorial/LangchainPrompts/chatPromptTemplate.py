from langchain_core.prompts import ChatPromptTemplate


ChatPrompt = ChatPromptTemplate([
    ('system', "you are helpful {domain} export"),
    ('human',"Explain in single terms, what is {topic}")
]
)

ChatPrompt.save('PromptTemplate.json')
