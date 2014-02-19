import os

source = os.path.dirname(os.path.realpath(__file__))
dest = os.path.expanduser("~")

for root, dirs, files in os.walk(source):
    for vcs in [".git", ".hg", ".svn"]:
        if vcs in dirs:
            dirs.remove(vcs);

    relativeToSource = root.replace(source, "", 1).lstrip("/")
    for filename in files:
        if not relativeToSource and filename in ["README.md", "link-home.py"]:
            continue

        if filename in [".git", ".gitignore", ".hgignore", ".gitmodules"]:
            continue

        dirname = os.path.dirname(os.path.join(dest, relativeToSource, filename))
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        os.system("cp -sRi \""+os.path.join(source, relativeToSource, filename)+"\" \""+os.path.join(dest, relativeToSource, filename)+"\"")