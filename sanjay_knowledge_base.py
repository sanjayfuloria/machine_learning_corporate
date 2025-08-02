"""
Knowledge base containing information about Sanjay Fuloria.
This module stores facts and information that the chatbot can use to answer questions.
"""

# Knowledge base about Sanjay Fuloria
SANJAY_FULORIA_KNOWLEDGE = {
    "basic_info": {
        "name": "Sanjay Fuloria",
        "description": "A professional in the field of machine learning and computer vision",
    },
    
    "professional_background": {
        "expertise": [
            "Machine Learning",
            "Computer Vision", 
            "Artificial Intelligence",
            "Deep Learning",
            "Object Detection",
            "Image Processing"
        ],
        "projects": [
            "Automatic Number Plate Recognition (ANPR) system using YOLO models",
            "License plate detection and recognition",
            "Vehicle tracking systems"
        ]
    },
    
    "technical_skills": {
        "programming_languages": ["Python", "OpenCV"],
        "frameworks": ["YOLO", "Ultralytics", "EasyOCR"],
        "specializations": [
            "Object Detection",
            "Optical Character Recognition (OCR)",
            "Video Processing",
            "Real-time Computer Vision"
        ]
    },
    
    "repositories": {
        "machine_learning_corporate": {
            "description": "A repository focused on machine learning applications for corporate use",
            "main_project": "Automatic Number Plate Recognition system",
            "technologies": ["YOLOv8", "OpenCV", "EasyOCR", "Python"],
            "features": [
                "Vehicle detection and tracking",
                "License plate detection",
                "OCR for license plate text recognition",
                "Video processing and visualization"
            ]
        }
    }
}

def get_knowledge_base():
    """
    Returns the complete knowledge base about Sanjay Fuloria.
    
    Returns:
        dict: Dictionary containing structured information about Sanjay Fuloria
    """
    return SANJAY_FULORIA_KNOWLEDGE

def search_knowledge(query_terms):
    """
    Search the knowledge base for relevant information based on query terms.
    
    Args:
        query_terms (list): List of terms to search for
        
    Returns:
        dict: Relevant information from the knowledge base
    """
    relevant_info = {}
    query_lower = [term.lower() for term in query_terms]
    
    for category, content in SANJAY_FULORIA_KNOWLEDGE.items():
        if isinstance(content, dict):
            for key, value in content.items():
                if any(term in key.lower() or 
                       (isinstance(value, str) and term in value.lower()) or
                       (isinstance(value, list) and any(term in str(item).lower() for item in value))
                       for term in query_lower):
                    if category not in relevant_info:
                        relevant_info[category] = {}
                    relevant_info[category][key] = value
        elif isinstance(content, str):
            if any(term in content.lower() for term in query_lower):
                relevant_info[category] = content
                
    return relevant_info