r"""Tokenize code came from https://stackoverflow.com/questions/34511673/extracting-comments-from-python-source-code"""
import os
import tokenize

with open("scrapedcomments.csv","w") as fCommentsFile:
    for (dirname, dirs, files) in os.walk("PreProcessing"):
        for file in files:
            if os.path.basename(file).endswith(".py"):
                try:
                    path = os.path.join(dirname,file)
                    with open(path,"r") as fPYFile:
                        fCommentsFile.write("\n______________\n")
                        fCommentsFile.write("\t\t{}\n".format(path))
                        for toktype, tok, start, end, line in tokenize.generate_tokens(fPYFile.readline):
                            # we can also use token.tok_name[toktype] instead of 'COMMENT'
                            # from the token module
                            if toktype == tokenize.COMMENT:
                                # print 'COMMENT' + " " + tok
                                tok = str(tok).replace(",","[COMMA]")
                                fCommentsFile.write("COMMENT: {}\n".format(tok))
                except Exception as e:
                    print(dirname,file, e)