# 💸 Agente Financeiro AI

Um assistente inteligente que responde perguntas sobre finanças pessoais utilizando inteligência artificial com interface interativa feita em Python com Flet. O projeto é construído com tecnologias modernas como **LangChain**, **Serper API**, **OpenRouter** e **Flet** para entregar uma experiência completa e acessível ao usuário.

---

## 🧠 O que o sistema faz?

- Recebe perguntas financeiras do usuário via interface gráfica.
- Encaminha a pergunta para um agente de IA treinado para lidar com esse tipo de dúvida.
- Exibe a resposta formatada na tela, com histórico de mensagens.
- Utiliza **modelos de linguagem (LLM)** via **OpenRouter** e pesquisas web através da **Serper API** para dar respostas atualizadas e contextualizadas.

---

## 🚀 Tecnologias Utilizadas

| Tecnologia     | Descrição                                                                 |
|----------------|--------------------------------------------------------------------------|
| 🧠 **LangChain**  | Framework para orquestração de agentes e ferramentas de IA.                |
| 🔍 **Serper API** | Permite realizar buscas no Google de forma programada.                   |
| 🤖 **OpenRouter** | Plataforma que conecta seu código a diferentes LLMs, como GPT, Mixtral. |
| 🖥️ **Flet**       | Biblioteca para construção de interfaces gráficas em Python.             |
| 🔐 **Dotenv**     | Para carregar variáveis de ambiente sensíveis como chaves de API.       |

---
## 🔑 Chaves Necessárias

- SERPER_API_KEY=sua_chave_serper
- OPENROUTER_API_KEY=sua_chave_openrouter
