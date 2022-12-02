def slugify(text):
    slug = text.lower().strip().replace(" ","-")
    while "--" in slug:
        slug = slug.replace('--', '-')
    return slug


title = input("Enter your Title :")
slug = slugify(title)
print(slug)
