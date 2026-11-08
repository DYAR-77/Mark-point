import base64, os, re
text = open('bundle.txt', encoding='utf-8').read()
parts = re.split(r'^=== (FILE|B64): (.+?) ===\n', text, flags=re.M)
for i in range(1, len(parts), 3):
    kind, path, body = parts[i], parts[i+1], parts[i+2]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if kind == 'B64':
        open(path, 'wb').write(base64.b64decode(body.strip()))
    else:
        open(path, 'w', encoding='utf-8', newline='\n').write(body)
    print('wrote', path)
