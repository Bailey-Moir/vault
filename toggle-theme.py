import os

# original = input("from: ").strip()
# replacement = input("to: ").strip()
# 
# for dname, dirs, files in os.walk("C:/Vault/Atomic Sync/Assets/excali"):
#     for fname in files:
#         fpath = os.path.join(dname, fname)
#         with open(fpath, "r", encoding="utf-8") as f:
#             s = f.read()
# 
#         # Replace original with replacement and replacement with original
#         s = s.replace(original, "\0fuckoff\0")  # Temporary placeholder to avoid overwriting
#         s = s.replace(replacement, original)
#         s = s.replace("\0fuckoff\0", replacement)
# 
#         with open(fpath, "w", encoding="utf-8") as f:
#             f.write(s)

mapping = [
    ["#61afef", "#98c379"], #blue, green
    ["CornflowerBlue", "OliveGreen"],
    ["#e06c75", "#d19a66"], #red, orange
    ["red", "orange"],
]

i = 0
for dname, dirs, files in os.walk(f"{os.getcwd()}/Assets/excali"):
    for fname in files:
        with open(os.path.join(dname, fname), "r+", encoding="utf-8") as f:
            s = f.read()

            # Replace original with replacement and replacement with original
            for pair in mapping:
                s = s.replace(pair[0], "\0fuckoff\0")  # Temporary placeholder to avoid overwriting
                s = s.replace(pair[1], pair[0])
                s = s.replace("\0fuckoff\0", pair[1])

            f.seek(0)
            f.truncate()
            f.write(s)
