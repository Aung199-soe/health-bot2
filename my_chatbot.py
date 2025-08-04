from search import search_questions  # Your existing search function
from typing import List, Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_chatbot_response(query: str) -> str:
    """
    Process user query and return formatted response
    Args:
        query: User's question
    Returns:
        Formatted bot response
    """
    try:
        if not query.strip():
            return "Please ask a health-related question."
            
        # Get search results
        results = search_questions(query)
        
        if not results:
            return "I couldn't find information about that. Try asking differently."
        
        # Format response
        response = "Here's what I found:\n\n"
        for i, result in enumerate(results[:3], 1):  # Show top 3 results
            response += (
                f"{i}. Question: {result['question']}\n"
                f"   Answer: {result['answer']}\n"
                f"   Confidence: {result['score']:.0%}\n\n"
            )
        return response
        
    except Exception as e:
        logger.error(f"Chatbot error: {e}")
        return "Sorry, I'm having trouble answering that right now."