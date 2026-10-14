# task6_html_checker.py

import re
from task4_structures import Stack


def check_html(html_text):
    tag_pattern = re.compile(r"<\s*(/?)\s*([a-zA-Z0-9]+)[^>]*?(/?)\s*>")
    stack = Stack()

    for match in tag_pattern.finditer(html_text):
        closing = match.group(1) == "/"
        tag = match.group(2).lower()
        self_closing = match.group(3) == "/"

        if self_closing:
            continue

        if not closing:
            stack.push(tag)
        else:
            if stack.is_empty():
                return False, f"Лишний закрывающий тег </{tag}>"
            top = stack.pop()
            if top != tag:
                return False, f"Ожидался </{top}>, а найден </{tag}>"

    if not stack.is_empty():
        return False, f"Не закрыт тег <{stack.pop()}>"
    return True, None


if __name__ == "__main__":
    print(" Задание №6:")

    good = """
    <html>
     <head>
      <title>
      Example
      </title>
     </head>
     <body>
      <h1>Hello, world</h1>
     </body>
    </html>
    """

    bad1 = "<html><head></head></html></body>"
    bad2 = "<html><head></head>"
    bad3 = "<html><body><h1>Hi</h2></body></html>"
    bad4 = "<div><p>text</p></span></div>"

    ok, msg = check_html(good)
    print("good:", ok, msg)
    assert ok is True

    for name, doc in [("bad1", bad1), ("bad2", bad2), ("bad3", bad3), ("bad4", bad4)]:
        ok, msg = check_html(doc)
        print(f"{name}:", ok, "|", msg)
        assert ok is False