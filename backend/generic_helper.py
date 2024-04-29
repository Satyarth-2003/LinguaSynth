import re

# Extract session ID from a session string using a regular expression
def extract_session_id(session_str: str):
    # Use regular expression to find the session ID
    match = re.search(r"/sessions/([^/]+)/contexts/", session_str)
    if match:
        # Return the extracted session ID (group 1 from the match)
        return match.group(1)
    # Return an empty string if no match found
    return ""
