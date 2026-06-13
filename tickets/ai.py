import json
import logging
from .client import client

logger = logging.getLogger(__name__)

# Define expected response schema
DEFAULT_RESPONSE = {
    "category": "General",
    "suggestion": "Thank you for contacting support. Our team will review your issue shortly."
}

VALID_CATEGORIES = [
    "Account",
    "Billing",
    "Order",
    "Delivery",
    "Return/Refund",
    "Technical",
    "General"
]


def validate_ai_response(data):
    """
    Validate that AI response has required fields and valid values.
    
    Args:
        data (dict): Response from AI model
        
    Returns:
        dict: Validated response with defaults if needed
    """
    if not isinstance(data, dict):
        logger.warning(f"AI response is not a dict: {type(data)}")
        return DEFAULT_RESPONSE
    
    # Check for required keys
    if "category" not in data or "suggestion" not in data:
        logger.warning(f"AI response missing required keys: {data.keys()}")
        return DEFAULT_RESPONSE
    
    category = data.get("category", "").strip()
    suggestion = data.get("suggestion", "").strip()
    
    # Validate category is in allowed list
    if category not in VALID_CATEGORIES:
        logger.warning(f"Invalid category: {category}. Using 'General'")
        category = "General"
    
    # Validate suggestion is not empty
    if not suggestion or len(suggestion) < 10:
        logger.warning(f"Suggestion too short: {suggestion}")
        suggestion = DEFAULT_RESPONSE["suggestion"]
    
    # Truncate if too long (prevent DB issues)
    if len(suggestion) > 1000:
        suggestion = suggestion[:997] + "..."
        logger.warning(f"Suggestion truncated to 1000 chars")
    
    return {
        "category": category,
        "suggestion": suggestion
    }


def analyze_ticket(description):
    """
    Analyze ticket using AI and return categorized response.
    Falls back to safe defaults if anything fails.
    
    Args:
        description (str): Ticket description to analyze
        
    Returns:
        dict: {"category": str, "suggestion": str}
    """
    try:
        # Validate input
        if not description or len(description) < 5:
            logger.warning("Ticket description too short")
            return DEFAULT_RESPONSE
        
        # Truncate very long descriptions
        if len(description) > 2000:
            description = description[:2000]
        
        prompt = f"""
You are a customer support assistant.

Categorize the ticket into ONE category:
- Account
- Billing
- Order
- Delivery
- Return/Refund
- Technical
- General

Also generate a helpful response suggestion (max 200 words).

Ticket:
{description}

Return ONLY valid JSON:
{{
    "category": "category_name",
    "suggestion": "response suggestion"
}}
"""

        # Call AI API with timeout
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,  # Lower randomness for more consistent responses
            max_tokens=300
        )
        
        # Extract content
        content = response.choices[0].message.content.strip()
        
        # Try to parse JSON
        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse AI response as JSON: {e}")
            logger.debug(f"Raw response was: {content}")
            return DEFAULT_RESPONSE
        
        # Validate response structure
        result = validate_ai_response(data)
        
        logger.info(f"Successfully analyzed ticket: {result['category']}")
        return result
    
    except Exception as e:
        # Catch any unexpected errors
        logger.error(f"Unexpected error in analyze_ticket: {type(e).__name__}: {e}", exc_info=True)
        return DEFAULT_RESPONSE