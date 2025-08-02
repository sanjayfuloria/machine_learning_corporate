#!/usr/bin/env python3
"""
Command-line interface for the Sanjay Fuloria chatbot.
"""

import argparse
import sys
import os
from sanjay_chatbot import create_chatbot

def main():
    """
    Main function for the chatbot CLI.
    """
    parser = argparse.ArgumentParser(
        description="Chatbot that answers questions about Sanjay Fuloria using Claude Sonnet",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python chatbot_cli.py --interactive
  python chatbot_cli.py --question "What is Sanjay's expertise?"
  python chatbot_cli.py --topics
        """
    )
    
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Start interactive chatbot session'
    )
    
    parser.add_argument(
        '--question', '-q',
        type=str,
        help='Ask a single question and exit'
    )
    
    parser.add_argument(
        '--topics', '-t',
        action='store_true',
        help='Show available topics about Sanjay Fuloria'
    )
    
    parser.add_argument(
        '--api-key',
        type=str,
        help='Anthropic API key (can also be set via ANTHROPIC_API_KEY env var)'
    )
    
    args = parser.parse_args()
    
    # Check if API key is available
    api_key = args.api_key or os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ Error: Anthropic API key is required!")
        print("Please either:")
        print("  1. Set the ANTHROPIC_API_KEY environment variable, or")
        print("  2. Use the --api-key argument")
        print("\nExample:")
        print("  export ANTHROPIC_API_KEY='your-api-key-here'")
        print("  python chatbot_cli.py --interactive")
        sys.exit(1)
    
    try:
        # Create chatbot instance
        chatbot = create_chatbot(api_key=api_key)
        
        if args.topics:
            show_topics(chatbot)
        elif args.question:
            ask_single_question(chatbot, args.question)
        elif args.interactive:
            interactive_session(chatbot)
        else:
            parser.print_help()
            
    except Exception as e:
        print(f"❌ Error initializing chatbot: {e}")
        sys.exit(1)

def show_topics(chatbot):
    """
    Display available topics about Sanjay Fuloria.
    
    Args:
        chatbot: SanjayFuloriaChatbot instance
    """
    print("\n🤖 Sanjay Fuloria Chatbot - Available Topics")
    print("=" * 50)
    
    topics = chatbot.get_available_topics()
    
    print("\n📋 Categories in Knowledge Base:")
    for category in topics["categories"]:
        print(f"  • {category.replace('_', ' ').title()}")
    
    print("\n💡 Sample Topics You Can Ask About:")
    for topic in topics["topics"]:
        print(f"  • {topic}")
    
    print("\n📝 Example Questions:")
    example_questions = [
        "What is Sanjay's expertise?",
        "Tell me about his ANPR project",
        "What programming languages does he use?",
        "What machine learning frameworks does he work with?",
        "Describe his computer vision projects"
    ]
    
    for question in example_questions:
        print(f"  • {question}")

def ask_single_question(chatbot, question):
    """
    Ask a single question and display the answer.
    
    Args:
        chatbot: SanjayFuloriaChatbot instance
        question (str): Question to ask
    """
    print(f"\n❓ Question: {question}")
    print("-" * 50)
    
    print("🤔 Thinking...")
    answer = chatbot.ask_question(question)
    
    print(f"\n🤖 Answer:\n{answer}")

def interactive_session(chatbot):
    """
    Start an interactive chatbot session.
    
    Args:
        chatbot: SanjayFuloriaChatbot instance
    """
    print("\n🤖 Sanjay Fuloria Chatbot - Interactive Mode")
    print("=" * 50)
    print("Ask me anything about Sanjay Fuloria!")
    print("Type 'help' for available topics, 'quit' or 'exit' to leave.\n")
    
    while True:
        try:
            question = input("❓ Your question: ").strip()
            
            if not question:
                continue
                
            if question.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye!")
                break
                
            if question.lower() in ['help', 'topics']:
                show_topics(chatbot)
                continue
            
            print("\n🤔 Thinking...")
            answer = chatbot.ask_question(question)
            print(f"\n🤖 Answer:\n{answer}\n")
            print("-" * 50)
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except EOFError:
            print("\n\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()