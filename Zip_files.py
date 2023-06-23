import zipfile
import os

def createZip(Path):
    with zipfile.ZipFile(f"{Path}\\Zipped videos.zip","w") as handle:
        for x in os.listdir():
            fileNameAerray = x.split()
            if len(fileNameAerray) == 5 and fileNameAerray[1] == "(part":
                handle.write(x, compress_type=zipfile.ZIP_DEFLATED)