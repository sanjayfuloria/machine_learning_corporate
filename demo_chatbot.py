#!/usr/bin/env python3
"""
Demo script for the Sanjay Fuloria chatbot.
This script demonstrates the chatbot functionality with sample questions.
"""

import os
from sanjay_chatbot import create_chatbot

def demo_chatbot():
    """
    Demonstrate the chatbot with sample questions.
    """
    print("🤖 Sanjay Fuloria Chatbot Demo")
    print("=" * 50)
    
    # Check if API key is available
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ Error: ANTHROPIC_API_KEY environment variable not set!")
        print("This demo requires an Anthropic API key to work.")
        print("\nTo run the demo:")
        print("1. Get an API key from https://console.anthropic.com/")
        print("2. Set it as an environment variable:")
        print("   export ANTHROPIC_API_KEY='your-api-key-here'")
        print("3. Run this demo again")
        return
    
    try:
        # Create chatbot instance
        print("🔄 Initializing chatbot...")
        chatbot = create_chatbot()
        print("✅ Chatbot initialized successfully!")
        
        # Sample questions to demonstrate
        sample_questions = [
            "What is Sanjay Fuloria's expertise?",
            "Tell me about his ANPR project",
            "What programming languages does he use?",
            "What are his technical skills?",
            "Describe his machine learning projects"
        ]
        
        print("\n🎯 Demo Questions and Answers:")
        print("-" * 50)
        
        for i, question in enumerate(sample_questions, 1):
            print(f"\n{i}. ❓ Question: {question}")
            print("   🤔 Processing...")
            
            try:
                answer = chatbot.ask_question(question)
                print(f"   🤖 Answer: {answer}")
            except Exception as e:
                print(f"   ❌ Error: {e}")
            
            print("   " + "-" * 45)
        
        # Show available topics
        print(f"\n📋 Available Topics:")
        topics = chatbot.get_available_topics()
        for category in topics["categories"]:
            print(f"   • {category.replace('_', ' ').title()}")
        
        print(f"\n✨ Demo completed! The chatbot is ready to answer questions about Sanjay Fuloria.")
        print(f"💡 Try running: python chatbot_cli.py --interactive")
        
    except Exception as e:
        print(f"❌ Error during demo: {e}")

def test_knowledge_base():
    """
    Test the knowledge base functionality without requiring API key.
    """
    print("\n🔍 Testing Knowledge Base (No API Key Required)")
    print("=" * 50)
    
    from sanjay_knowledge_base import get_knowledge_base, search_knowledge
    
    # Test knowledge base retrieval
    kb = get_knowledge_base()
    print(f"✅ Knowledge base loaded with {len(kb)} categories:")
    for category in kb.keys():
        print(f"   • {category.replace('_', ' ').title()}")
    
    # Test knowledge search
    print(f"\n🔍 Testing knowledge search:")
    test_queries = ["machine learning", "python", "yolo", "projects"]
    
    for query in test_queries:
        results = search_knowledge([query])
        print(f"   Query '{query}': Found {len(results)} relevant categories")
        
    print("✅ Knowledge base tests completed!")

if __name__ == "__main__":
    print("Choose demo mode:")
    print("1. Full chatbot demo (requires API key)")
    print("2. Knowledge base test only (no API key needed)")
    
    try:
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            demo_chatbot()
        elif choice == "2":
            test_knowledge_base()
        else:
            print("Running both tests...")
            test_knowledge_base()
            demo_chatbot()
    except KeyboardInterrupt:
        print("\n👋 Demo cancelled!")
    except EOFError:
        print("\n👋 Demo cancelled!")