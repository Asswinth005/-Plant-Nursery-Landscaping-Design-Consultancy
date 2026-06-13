import os
import re

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            new_content = content
            
            # For btn-primary, just add justify-content: center; if it has align-items: center;
            if 'align-items: center;' in new_content and '.btn-primary {' in new_content:
                # We can replace the exact block if it is consistent
                pass
            
            # A safer regex replacement:
            # Find .btn-primary block and add justify-content: center; before the closing brace if not present
            btn_primary_pattern = re.compile(r'(\.btn-primary\s*{[^}]+)(})')
            def add_justify(match):
                block = match.group(1)
                if 'justify-content: center;' not in block:
                    if block.endswith(';'):
                        return block + '\n            justify-content: center;\n        }'
                    elif block.strip().endswith(';'):
                        return block + ' justify-content: center; }'
                    else:
                        return block + '; justify-content: center; }'
                return match.group(0)
            
            new_content = btn_primary_pattern.sub(add_justify, new_content)
            
            btn_outline_pattern = re.compile(r'(\.btn-outline\s*{[^}]+)(})')
            def add_flex_justify(match):
                block = match.group(1)
                if 'justify-content: center;' not in block:
                    adds = '\n            display: inline-flex;\n            align-items: center;\n            justify-content: center;\n        }'
                    if block.endswith(';') or block.endswith(' '):
                        return block.rstrip() + adds
                    else:
                        return block + ';' + adds
                return match.group(0)
            
            new_content = btn_outline_pattern.sub(add_flex_justify, new_content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {filepath}")
