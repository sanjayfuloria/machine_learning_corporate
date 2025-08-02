# Sanjay Fuloria Chatbot Configuration

## Environment Variables

### Required
- `ANTHROPIC_API_KEY`: Your Anthropic API key for accessing Claude Sonnet

### Example
```bash
export ANTHROPIC_API_KEY="your-anthropic-api-key-here"
```

## Getting an Anthropic API Key

1. Visit https://console.anthropic.com/
2. Sign up or log in to your account
3. Navigate to the API Keys section
4. Create a new API key
5. Copy the key and set it as an environment variable

## Usage Examples

### Interactive Mode
```bash
python chatbot_cli.py --interactive
```

### Single Question
```bash
python chatbot_cli.py --question "What is Sanjay's expertise in machine learning?"
```

### Show Available Topics
```bash
python chatbot_cli.py --topics
```

### With API Key as Argument
```bash
python chatbot_cli.py --api-key "your-key-here" --interactive
```

## Programmatic Usage

```python
from sanjay_chatbot import create_chatbot

# Initialize chatbot
chatbot = create_chatbot(api_key="your-api-key")

# Ask a question
answer = chatbot.ask_question("Tell me about Sanjay's ANPR project")
print(answer)

# Get available topics
topics = chatbot.get_available_topics()
print(topics)
```

## Customizing the Knowledge Base

To add more information about Sanjay Fuloria, edit the `sanjay_knowledge_base.py` file:

```python
SANJAY_FULORIA_KNOWLEDGE = {
    # Add new categories or expand existing ones
    "new_category": {
        "new_info": "Additional information about Sanjay"
    }
}
```