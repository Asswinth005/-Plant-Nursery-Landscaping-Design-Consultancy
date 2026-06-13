import os
import re

filepath = 'd:/Groww Official/Plant Nursery/service.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add flex flex-col h-full to the wrapper
content = re.sub(
    r'(<div class="service-card-large[^"]*)(">)',
    lambda m: m.group(1) + ' flex flex-col h-full">' if 'flex-col' not in m.group(1) else m.group(0),
    content
)

# Change mt-4 to mt-auto for the footer
# The footer is like <div class="mt-4 pt-4 border-t
content = re.sub(
    r'(<div class=")(mt-4)( pt-4 border-t border-gray-200 dark:border-gray-700">)',
    r'\g<1>mt-auto\g<3>',
    content
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated service.html")
