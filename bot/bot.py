import os

from decouple import config

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIbot:

    def __init__(self):
        self._chat = ChatGroq(model="llama-3.3-70b-versatile")

    def ivoke(self,question):
        prompt = PromptTemplate(
            input_variables=["texto"],
            template='''
            voce é um comediante, conte piadas de humor um pouco duvidoso, enive apenas uma piada por vez, como se fosse uma mensagem do zap.
            <texto>
            {texto}
            <texto>
            '''
        )
        chain = prompt | self._chat | StrOutputParser()
        response = chain.invoke({
            'texto':question
        })
        return response