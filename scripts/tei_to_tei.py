import glob
import os

from bs4 import BeautifulSoup

# Creating a generic TEI tree to be injected with content later
TEI_tree = """<TEI xmlns="http://www.tei-c.org/ns/1.0">
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
<sourceDoc>
</sourceDoc>
<text>
    <body>
        <div type="transcription">
        </div>
    </body>
</text>
</TEI>"""

# Directory where the transcribed pages are stored
directory = "../xml/xml_to_xml"

# We create the "soup" for the generic TEI tree to begin data manipulation
soup_TEI = BeautifulSoup(TEI_tree, features='xml')

# Creating a file list storing all page xml files
filelist = glob.glob(os.path.join(directory, '*.page.xml'))
# Sorting the PAGE XML file list for processing
for f in sorted(filelist):
    print(f"Processing {f}...")
    # Checking if the file is actually a file and if it's a PAGE XML
    if os.path.isfile(f) and f.endswith('.page.xml'):
        # Looking for the sourceDoc in the generic TEI tree
        sourceDoc_all = soup_TEI.find('sourceDoc')
        # Looking for the main div in the generic TEI tree
        main_div_all = soup_TEI.find('div')

        # Opening the page XML while iterating on the filelist
        with open(f, mode='r', encoding='utf-8') as fh_page:
            # Creating the "soup" for the page xml file
            soup_page = BeautifulSoup(fh_page, "xml")
            # Looking for the sourceDoc in the transformed page xml
            sourceDoc = soup_page.find('sourceDoc')
            # Looking for the transcription in the transformed page xml
            transcription = soup_page.findAll("div", {"type": "transcription"})

            for sourceDoc_child in sourceDoc.contents:
                # Appending the sourceDoc content to the generic TEI tree
                sourceDoc_all.append(sourceDoc_child.next_element)

            for div in transcription:
                # Appending the transcription to the generic TEI tree
                for div_child in div.contents:
                    # A bit of string manipulation here, to get rid of unnecessary divs
                    div_to_be_removed = str(div_child.next_element)
                    removed_div = div_to_be_removed.replace('<div>', '').replace('</div>', '')
                    div_soup = BeautifulSoup(removed_div, 'xml')
                    main_div_all.append(div_soup)

with open("../tei/pride_and_prejudice_all.xml", mode="w+", encoding='utf-8') as fh:
    # We write the generic TEI tree injected with the page xml files content into a new file
    fh.write(soup_TEI.prettify())
