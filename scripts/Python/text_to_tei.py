# -*- UTF-8 -*-

"""
- author: Floriane Chiffoleau
- date: August 2022
- description: Encoding a corpus with some basic XML tags
- input: plain text
- output: XML tree with tagged text
- usage :
    ======
    python name_of_this_script.py arg1 arg2

    arg1: folder of the transcription in a text format
    arg2: folder for the transcription in an XML format

"""

import os
import re
import sys

start_of_the_tree = """<TEI xmlns="http://www.tei-c.org/ns/1.0">
                    <teiHeader>
                        <fileDesc>
                            <titleStmt>
                                <title xml:lang="en"/>
                                <principal>
                                    <persName ref="#."/>
                                </principal>
                                <respStmt>
                                    <resp>Edited by</resp>
                                    <persName ref="#."/>
                                </respStmt>
                            </titleStmt>
                            <publicationStmt>
                                <authority/>
                                <availability>
                                    <licence target="https://creativecommons.org/licenses/by/3.0/deed.en">Attribution 3.0 Unported (CC BY 3.0) </licence>
                                </availability>
                                <date when-iso="...."/>
                            </publicationStmt>
                            <seriesStmt>
                                <title type="main"/>
                                <title type="genre"/>
                                <title type="topic"/>
                            </seriesStmt>
                            <sourceDesc>
                                <msDesc>
                                    <msIdentifier/>
                                    <msContents/>
                                    <physDesc/>
                                </msDesc>
                            </sourceDesc>
                        </fileDesc>
                        <encodingDesc>
                            <projectDesc>
                                <p/>
                            </projectDesc>
                        </encodingDesc>
                        <profileDesc>
                            <langUsage>
                                <language ident=""/>
                            </langUsage>
                        </profileDesc>
                        <revisionDesc>
                            <change when-iso="....-..-.." who="#.">Encoding of the text</change>
                        </revisionDesc>
                    </teiHeader>
                    <text>
                        <body>
                            <div type="transcription">
                                <pb n="" facs=".JPG"/>
                                <p>
                            """

end_of_the_tree = """      
                            </p></div>
                        </body>
                    </text>
                </TEI>
                """

def tagging_paragraph(text):
    """ Add paragraph tags in a text
    
    :param text str: text that has to be modify
    :returns: text encoded with paragraph tags
    :rtype: str
    """
    punctuation = "!\"»?."  
    # This variable contains all the punctuation signs that indicates a phrase ending
    # and a need for an ending paragraph tag

    for sign in punctuation:
        text = text.replace(sign + "\n", sign + '</p>\n<p rend="indent">')
        text = text.replace(sign + " \n", sign + '</p>\n<p rend="indent">')
    # This function can add unnecessary paragraph tag that will have to be suppress afterwards
    return text

def tagging_regex(text):
    """Apply tags to the regex

    :param text str: text that has to be modify
    :returns: text encoded with the right tags for the regex
    :rtype: str
    """

    #This series of statements contains regex of recurrent terms from the corpus
    dateline = re.compile(r'^[A-Za-zÀ-ÖØ-öø-ÿ-]+(( |-)[A-Za-zÀ-ÖØ-öø-ÿ-]+)?, (le )?[0-9]* [A-Za-zÀ-ÖØ-öø-ÿ-]+ 19[1-2][0-9] ?.?')
    page_break = re.compile(r'==--==--==--==')
    page_numbering = re.compile(r'(-|\() ?[0-9]* ?(-|\))')

    #This series of statements contains the encoding for the declared recurrent terms from the corpus
    text = re.sub(dateline, r'<dateline rend="align(right)">\g<0></dateline>', text)
    text = re.sub(page_break, '', text)
    text = re.sub(page_numbering, r'<pb n="" facs=".JPG"/><note type="foliation" place="top">\g<0></note>',text)
    return text

def tagging_linebreak(text):
    LINEBREAK = {'-\n': '-<lb break="no"/>', ' \n': '<lb/> ', "'\n": "'<lb/>"}
    for key, value in LINEBREAK.items():
        text = text.replace(key, value)
    if ">" not in text:
        text = text.replace("\n","<lb/> ")
    return text


for root, dirs, files in os.walk(sys.argv[1]):
    for filename in files:
        with open(sys.argv[1] + filename, 'r') as file_in:
            print("reading from "+sys.argv[1] + filename)
            file = file_in.read()
        file = file.replace("\n", "\n$")
        #This sign is added to help split the text afterwards while preserving the newlines.
        processed_text_as_list = []
        text_as_list = file.split('$')
        for text in text_as_list:
            text = text.replace("’", "'")
            text = tagging_regex(text)
            text = tagging_paragraph(text)
            text = tagging_linebreak(text)
            processed_text_as_list.append(text)
        body_of_the_tree = "".join(processed_text_as_list)

        output_file = sys.argv[2] + filename.replace(".txt", ".xml")
        with open(output_file, "w") as file_out:
            print("writing to " + output_file)
            file_out.write(start_of_the_tree)
            file_out.write(body_of_the_tree)
            file_out.write(end_of_the_tree)