import os
import markdown
from bs4 import BeautifulSoup
from glob import glob
from datetime import datetime

POSTS_DIR = "_posts"
DRAFTS_DIR = "drafts"


class Post:
    def __init__(self) -> None:
        layout = "posts"
        title = None
        date = None
        html = None

    def format_metadata(self):
        # hardcoded the timezone because I don't care
        return f"""
        ---
        layout: {self.layout}
        title: {self.title}
        date: {self.date} -0800
        ---"""

    def write_post(self):
        filename = self.title.encode("ASCII", "ignore")
        filename = filename.replace(" ", "-")
        filename = f"{self.date.split()[0]}-{filename}"

        return filename


# right now I could just do datetime.now() because they're going to be the
# same with the current workflow. However, I've got plans for a future
# script that will do something different, and actually need this.
def get_last_edit_date(path):
    unix_time = os.path.getmtime(path)
    return datetime.utcfromtimestamp(unix_time).strftime("%Y-%m-%d %H:%M:%S")


# okay just realized that we have to convert html BACK to markdown.
# would prefer to build a tree of markdown, but the python library I'm
# using doesn't seem to support that. I could just do custom parsing.
# Grabbing the title is easy. Grabbing images is pretty easy; ![] is pretty
# distinctive and ammenable to regex. Not as easy or clean as just using
# bs, though... markdownify will convert html to markdown.

script_location = os.path.dirname(os.path.abspath(__file__))
for filename in glob(os.path.join(script_location, "*.markdown")):
    post = Post()
    print(f"{filename}: {get_last_edit_date(os.path.join(script_location, filename))}")
    post.date = get_last_edit_date(filename)
    html = ""
    with open(filename) as f:
        html = markdown.markdown(f.read())
    soup = BeautifulSoup(html, "html.parser")
    post.title = soup
