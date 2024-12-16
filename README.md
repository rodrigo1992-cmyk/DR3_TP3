# Rodrigo_Mesquita_DR3_TP3
## Desenvolvimento de Data-Driven Apps com Python [24E4_3]
### Link Github: https://github.com/rodrigo1992-cmyk/DR3_TP3
### Link Streamlit App: https://rodrigo1992-cmyk-dr3-tp3-appservicesstreamlit-app-wqqlxo.streamlit.app/

### **Assistente de Busca por Informações sobre a Industria Musical**
**Objetivo**: Recuperar informações a respeito de cantores, bandas e músicas, incluindo informações gerais, notícias recentes e próximos eventos.

**Problemática**: Sem o uso de um agente, dependendo da pergunta, seria necessário o usuário garimpar enormes textos na wikipedia para localizar a informação desejada ou acessar diversos sites até localizar. O uso do agente acelera esse processo trazendo uma resposta instantânea. 

**Público-Alvo**: Fãs de cantores em busca de informações de forma rápida.

**Funcionalidades**:
- Realizar busca no Wikipedia por informações gerais, histórico do artista, prêmios e records conquistados.
- Realizar busca no DuckDuckGo por agendas de shows e notícias recentes.

### **Instruções para Execução do Aplicativo**
- Opção 1: Utilizar o link do aplicativo implementado em Cloud, disponibilizado no cabeçalho.
- Opção 2: Instalar as bibliotecas declaradas no arquivo requirements.txt e executar o arquivo app/services/streamlit_app.py.

### **Casos de Uso Utilizados para Teste e os Resultados Obtidos**:
**1.Perguntar a história de vida de Chester Bennington.**

<img src="app\docs\img1.png" alt="Resposta do Modelo" width="600" height="220">

**2.Perguntar em que ano nasceu a Beyoncé.**

<img src="app\docs\img2.png" alt="Resposta do Modelo" width="600" height="120">

**3.Perguntar quando e onde será o próximo show do AC/DC no Brasil.**

<img src="app\docs\img3.png" alt="Resposta do Modelo" width="600" height="180">

**4.Voltar a perguntar a idade da Beyonce e conferir se o modelo irá resgatar do histórico, conforme orientado (para acelerar o tempo de resposta e não consumir chamadas à API), ou buscar na internet.**

<img src="app\docs\img4.png" alt="Resposta do Modelo" width="600" height="120">

<img src="app\docs\img4_1.png" alt="Resposta do Modelo" width="600" height="140">


**5,Realizar uma Pergunta sobre um time de futebol, para avaliar como o modelo irá se comportar.**

<img src="app\docs\img5.png" alt="Resposta do Modelo" width="600" height="120">

### Observações
- Foi realizada a customização do prompt "hwchase17/react", para que ele também analise se o input do usuário está dentro do tópico definido, e para que ele consulte o histórico de mensagens antes de invocar uma das ferramentas externas. 
- O prompt criado (abaixo) também está disponível em: https://smith.langchain.com/hub/musicindustrysearch/prompt

```python
Analyze if the following question is about singers, bands or musics, if it is, try to answer as best you can, If not, respond that you are only allowed to give information about the music industry.

Use the chat history or one of the following tools to get it:

###
Tools: {tools}

###
Chat history:  {chat_history}

###
Use the following format:

Question: the input question you must answer

Thought: you should always think about what to do.

Action: the action to take, should be one of [{tool_names}]

Action Input: the input to the action

Observation: the result of the action

... (this Thought/Action/Action Input/Observation can be repeated a maximum of three times)

Thought: I now know the final answer

Final Answer: the final answer to the original input question

Begin!

Question: {input}

Thought:{agent_scratchpad}
```
