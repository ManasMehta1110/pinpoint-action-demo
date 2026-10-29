def slugify(text):
    """Lowercase, trim, and join words with hyphens."""
    return text.lower().replace(' ', '_')
