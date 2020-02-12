import os
import sys

index_html = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="./assets/css/styles.css">
    <title>Document</title>
</head>

<body>
    <h1>
        HTML-CSS-JAVASCRIPT Project created!
    </h1>
</body>
<script src="./assets/js/script.js"></script>

</html>"""

project_types = ["html"]


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


if sys.argv[1] not in project_types:
    print("#AVALIBLE TEMPLATES#")
    print("#    HTML")
else:
    if sys.argv[1] == 'html':
        # Get Working Directory
        path = os.getcwd()
        # Create new folder named by first argv
        os.mkdir(sys.argv[2])
        # Change to the new folder
        new_path = os.path.join(path, sys.argv[2])
        os.chdir(new_path)
        print(os.getcwd())
        # Create index.html
        #copyfile(index_path, new_path)
        touch(os.path.join(new_path, "index.html"))
        f = open(os.path.join(new_path, "index.html"), "w")
        f.write(index_html)
        f.close()
        # Create resources folder
        os.mkdir("assets")
        new_path = os.path.join(new_path, "assets")
        os.chdir(new_path)
        os.mkdir("css")
        os.mkdir("js")
        os.mkdir("img")
        touch(os.path.join(new_path, "css", "styles.css"))
        touch(os.path.join(new_path, "js", "script.js"))
