#!/usr/bin/env python


from datetime import datetime
from markdownify import markdownify as md
from utils.text import slugify

import logging
import xml.etree.ElementTree as ET


if __name__ == "__main__":
    tree = ET.parse("./example.xml")
    root = tree.getroot()

    for channel in root:
        for item in channel:
            title = content = ftime = ""
            ptime = datetime.now()

            for i in item:
                if i.tag == "title":
                    title = i.text
                elif i.tag == "{http://purl.org/rss/1.0/modules/content/}encoded":
                    try:
                        content = md(i.text)
                    except BaseException:
                        logging.error(f"Skipped {title}")
                elif i.tag == "{http://wordpress.org/export/1.2/}post_date_gmt":
                    ptime = datetime.strptime(i.text, "%Y-%m-%d %H:%M:%S")
                    ftime = datetime.strftime(ptime, "%Y-%m-%dT%H:%M:%S+00:00")

            slug = datetime.strftime(ptime, "%Y-%m-%d-") + slugify(title)
            file_name = slug + ".md"
            post = """---
title: {title}
date: {date}
---

{content}"""

            print(file_name)
            print(post.format(title=title, date=ftime, content=content))
