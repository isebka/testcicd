import os

def test_index_html_exists():
    assert os.path.exists("index.html"), "Файл index.html не найден!"

def test_index_html_content():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
        assert "<html>" in content, "В файле нет тега <html>"
        assert "<body>" in content, "В файле нет тега <body>"