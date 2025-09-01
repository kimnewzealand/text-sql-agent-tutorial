## Agent for text-to-SQL with automatic error correction


> In this tutorial, we’ll see how to implement an agent that leverages SQL using smolagents.

See tutorial https://huggingface.co/learn/cookbook/agent_text_to_sql

## Setup

Follow these steps to set up the environment:

Use Python 3.13

1. **Create a virtual environment**:
    ```bash
    py -m venv .venv
    ```

2. **Activate the virtual environment**:
    - On Windows:
      ```bash
      .venv\Scripts\Activate
      ```
    - On macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt    
    ```

  ```bash
    HF_API_KEY="your_huggingface_api_key_here"
    ```
    
    **To get a HuggingFace API key:**
    1. Go to [HuggingFace](https://huggingface.co/)
    2. Create an account or sign in
    3. Go to your profile settings
    4. Navigate to "Access Tokens"
    5. Create a new token with "read" permissions
    6. Copy the token and paste it in your `.env` file

  
## License

This project is for educational purposes only.
