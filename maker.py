import os
import re

def extract_image_links_from_markdown(markdown_text):
    pattern = r'!\[.*?\]\((.*?)\)'
    image_links = re.findall(pattern, markdown_text)
    return image_links


pths = []
names = []
for i, j, k in os.walk("1/"):
    if not len(names):
        names = k
    for l in k:
        pths.append(os.path.join(i, l))

for i in range(0, len(pths)):
    r = ""
    names[i] = names[i].split(".md")[0].replace("~", "-").replace(" ", "")
    with open(pths[i], "r", encoding="utf-8") as f:
        r = f.read()
    for j in extract_image_links_from_markdown(r):
        r = r.replace(j, "https://pic.2ge.org/cdn/?url=%s" % j)
    with open("2/%s.md" % names[i], "w", encoding="utf-8") as f:
        f.write(r)
    print(i, names[i])
    
    
x = ""
for i in names:
    j = i
    x += "- [%s](%s)\n" % (j, j)

with open("2/_sidebar.md", "w", encoding="utf-8") as f:
    f.write(x)

input()