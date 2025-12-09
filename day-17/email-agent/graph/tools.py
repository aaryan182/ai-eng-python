def email_template_tool(intent: str, body: str) -> str:
    return f"""
Subject: {intent}

Dear [Recipient],

{body}

Warm regards,
[Your Name]
""".strip()
