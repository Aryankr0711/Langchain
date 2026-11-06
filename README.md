# README.md – LangChain Experiments

## 1. Installation and Setup

Before running any Python scripts, install all the required dependencies listed in `requirements.txt`.

**Step 1: Clone the repository**

```bash
git clone <repository-url>
cd <repository-folder>
```

**Step 2: Create and activate a virtual environment (recommended)**

```bash
python -m venv venv
```

For Windows:

```bash
venv\Scripts\activate
```

**Step 3: Install all dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Configure API Keys**

Create a `.env` file in the project's root directory and add the API keys for the providers you want to experiment with.

```env
OPENAI_API_KEY="your_openai_api_key"
ANTHROPIC_API_KEY="your_anthropic_api_key"
GOOGLE_API_KEY="your_google_api_key"
```

Add only the API keys required for your experiments. Never share or commit your actual API keys to GitHub.

---

## 2. LLMs (Large Language Models)

- Experimented with OpenAI's LLM models using LangChain.
- The available API credits had been exhausted, so the models could not generate responses.
- To run these examples successfully, you may need to add credits to your OpenAI API account.

## 3. Chat Models

- Experimented with OpenAI Chat Models using LangChain.
- Explored the differences between traditional LLMs and Chat Models.
- An interesting observation was that `gpt-4o-mini` can be integrated as a Chat Model using `ChatOpenAI`, but it is not a traditional completion model supported by the `OpenAI` class.

## 4. Anthropic Models

- Explored the integration of Anthropic's Claude models with LangChain using the `ChatAnthropic` interface.
- Could not test model responses because the Anthropic API account required additional credits.
- To execute these examples, ensure that your Anthropic API account has sufficient credits.

## 5. Google Gemini Models

- Experimented with Google Gemini models using LangChain.
- To get started, generate your API key from [Google AI Studio – API Keys](https://aistudio.google.com/api-keys).
- Add the generated API key to your `.env` file:

```env
GOOGLE_API_KEY="your_google_api_key"
```

- Ensure that the selected Gemini model is available for your API project and supports the `generateContent` method.
- Run the corresponding Python scripts to experiment with Gemini Chat Models.

**Note:** Google AI Studio provides a free API tier for eligible models, subject to usage limits and availability.

---

## 6. Important Notes

- Make sure your virtual environment is activated before running the scripts.
- Ensure all dependencies are installed using `requirements.txt`.
- Configure the appropriate API key in the `.env` file before executing provider-specific scripts.
- Some providers require a funded API account to generate responses.
- Keep your API keys private and never upload your `.env` file to GitHub.
