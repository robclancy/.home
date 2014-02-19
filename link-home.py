import os

def linkFolder(source, dest):
    for root, dirs, files in os.walk(source):
        for vcs in [".git", ".hg", ".svn"]:
            if vcs in dirs:
                dirs.remove(vcs);

        relativeToSource = root.replace(source, "", 1)
        for filename in files:
            if filename in [".git", ".gitignore", ".hgignore", ".gitmodules"]:
                continue

            dirname = os.path.dirname(os.path.join(dest+relativeToSource, filename))
            if dirname and not os.path.exists(dirname):
                os.makedirs(dirname)
            os.system("cp -sRi \""+os.path.join(source+relativeToSource, filename)+"\" \""+os.path.join(dest+relativeToSource, filename)+"\"")

linkFolder(os.path.dirname(os.path.realpath(__file__)), os.path.expanduser("~"))