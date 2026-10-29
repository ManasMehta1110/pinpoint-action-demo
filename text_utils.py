def slugify(text):
    """Lowercase, trim, and join words with hyphens."""
    return "-".join(text.strip().lower().split())
