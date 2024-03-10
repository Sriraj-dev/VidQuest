# VidQuest 🖥️ 🔍

VidQuest is a powerful web application designed to decode the secrets hidden within YouTube videos. With VidQuest, you can effortlessly uncover insights and gain a deeper understanding of your favorite video content using AI technology. It uses Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) to build LLM(Large Language Model)-enabled data pipeline in Python and join data from multiple input sources, leverages OpenAI API [Embeddings](https://platform.openai.com/docs/api-reference/embeddings) and [Chat Completion](https://platform.openai.com/docs/api-reference/completions) endpoints to generate AI assistant responses.

## Features

- **Simplify Complexity:** VidQuest harnesses the latest in AI advancements to distill lengthy YouTube videos into concise summaries, making complex content easily digestible.
  
- **Uncover Insights:** Dive deeper into your videos by asking questions directly related to the content. VidQuest's AI-powered question answering system provides accurate and relevant responses.
  
- **User-Friendly Interface:** Our intuitive interface ensures seamless navigation, allowing you to effortlessly interact with the app and unlock valuable insights.

<img width="1467" alt="image" src="https://github.com/Sriraj-dev/pathway_sample_app/assets/85361724/4db7399f-f9f6-42d8-8ebd-4542fe4f1532">
  

## Installation
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/vidquest.git
    ```
    
2. **Create a conda environment using environment.yml file:**
3. **Create a .env file with following content**
   ```bash
    HOST = 0.0.0.0
    PORT = 8080
    EMBEDDER_LOCATOR=text-embedding-ada-002
    MODEL_LOCATOR=gpt-3.5-turbo
    MAX_TOKENS=200
    TEMPERATURE=0.0
    LOCAL_FOLDER_PATH= {YOUR_FOLDER_PATH}
    EMBEDDING_DIMENSION=1536
    OPENAI_API_TOKEN = {YOUR_API_TOKEN}
    ```
4. **Run the following commands**
   ```bash
   pip install llm_app pathway
    ```

## Usage

1. **Run the main.py file**
    ```bash
    python main.py
    ```
    
2. **Run the Streamlit App:**
    ```bash
    streamlit run streamlit_app/ui.py
    ```
    
3. **Add YouTube Video Links:**
    Simply paste the URLs of the YouTube videos you want to explore into the provided text area.
  
4. **Initiate Summarization:**
    Click the "Upload" button to kickstart VidQuest's AI engine, summarizing your videos into easily digestible insights.
  
5. **Ask Questions:**
    Probe deeper into the video content by asking questions directly within the app. VidQuest's AI is ready to provide accurate and insightful answers.

## Contributing

We welcome contributions from the community to enhance VidQuest's capabilities further. Whether it's fixing bugs, adding new features, or improving the user experience, your contributions are valuable. Feel free to open an issue or submit a pull request.

## License

VidQuest is licensed under the [MIT License](LICENSE).

