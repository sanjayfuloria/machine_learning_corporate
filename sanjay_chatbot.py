"""
Chatbot that answers questions about Sanjay Fuloria using Claude Sonnet.
"""

import os
import json
from typing import Optional, Dict, Any
import anthropic
from sanjay_knowledge_base import get_knowledge_base, search_knowledge

class SanjayFuloriaChatbot:
    """
    A chatbot that answers questions about Sanjay Fuloria using Claude Sonnet.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the chatbot with Claude Sonnet API.
        
        Args:
            api_key (str, optional): Anthropic API key. If not provided, 
                                   will look for ANTHROPIC_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError(
                "Anthropic API key is required. Please provide it as a parameter "
                "or set the ANTHROPIC_API_KEY environment variable."
            )
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.knowledge_base = get_knowledge_base()
        
        # System prompt to guide Claude's responses
        self.system_prompt = """You are a helpful assistant that answers questions about Sanjay Fuloria. 
        You have access to a knowledge base with information about his professional background, 
        technical skills, and projects. Use this information to provide accurate and helpful responses.
        
        When answering questions:
        1. Be factual and based on the provided knowledge
        2. If you don't have specific information, say so clearly
        3. Be conversational and helpful
        4. Focus on Sanjay Fuloria's expertise in machine learning and computer vision
        
        Available information includes his technical skills, professional background, 
        expertise in areas like machine learning, computer vision, YOLO models, 
        and his ANPR (Automatic Number Plate Recognition) project."""
    
    def _prepare_context(self, query: str) -> str:
        """
        Prepare context from knowledge base based on the user's query.
        
        Args:
            query (str): User's question
            
        Returns:
            str: Formatted context for Claude
        """
        # Extract key terms from query for knowledge search
        query_terms = query.lower().split()
        relevant_info = search_knowledge(query_terms)
        
        if not relevant_info:
            # If no specific match, provide general context
            relevant_info = self.knowledge_base
        
        context = "Knowledge base about Sanjay Fuloria:\n"
        context += json.dumps(relevant_info, indent=2)
        return context
    
    def ask_question(self, question: str) -> str:
        """
        Ask a question about Sanjay Fuloria and get an answer from Claude Sonnet.
        
        Args:
            question (str): The question to ask
            
        Returns:
            str: Claude's response based on the knowledge base
        """
        try:
            context = self._prepare_context(question)
            
            # Prepare the message for Claude
            messages = [
                {
                    "role": "user", 
                    "content": f"{context}\n\nBased on the above information about Sanjay Fuloria, please answer this question: {question}"
                }
            ]
            
            # Call Claude Sonnet
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                temperature=0.7,
                system=self.system_prompt,
                messages=messages
            )
            
            return response.content[0].text
            
        except Exception as e:
            return f"I'm sorry, I encountered an error while processing your question: {str(e)}"
    
    def get_available_topics(self) -> Dict[str, Any]:
        """
        Get a summary of available topics about Sanjay Fuloria.
        
        Returns:
            dict: Available topics and categories
        """
        return {
            "categories": list(self.knowledge_base.keys()),
            "topics": [
                "Professional background and expertise",
                "Technical skills and programming languages",
                "Machine learning and computer vision projects",
                "ANPR (Automatic Number Plate Recognition) system",
                "YOLO models and object detection",
                "Repository information"
            ]
        }

def create_chatbot(api_key: Optional[str] = None) -> SanjayFuloriaChatbot:
    """
    Factory function to create a chatbot instance.
    
    Args:
        api_key (str, optional): Anthropic API key
        
    Returns:
        SanjayFuloriaChatbot: Configured chatbot instance
    """
    return SanjayFuloriaChatbot(api_key=api_key)