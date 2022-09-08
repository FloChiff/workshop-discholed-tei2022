## Transforming transcriptions into TEI
### Transforming text files
1. Open your command line interface
2. Type ```$ python path/to/text_to_tei.py path/to/text/folder path/to/xml/folder``` 

The command requires three arguments: the first one is the path to the script, the second one is the path to the folder where your text(s) is/are located and the third one is the path to the folder where the newly created XML file(s) will be located  


### Transforming XML
#### ALTO into TEI
1. Open your Oxygen XML Editor,
2. Open one of your XML file from the unzipped folder and the XSL stylesheet file for the transformation _alto_to_tei.xsl_.
3. Go to the _XSLT Debugger perspective_ ![](https://www.oxygenxml.com/doc/versions/24.1/ug-editor/img/Debugger18.png) (Third button at the top right corner).
4. Check that, in the top left corner, an XML file was selected in the 'XML:' window and that your XSL file was chosen in the 'XSL:' window (No need to put anything in 'Output:' as it is already defined in the stylesheet).
5. In the stylesheet, change the paths mentioned line 15 (_collection_) and line 26 (_result-document_) to match the place where you have your XML files and where you want your TEI files.
6. Once this is done, click on _Run_ ![](https://www.oxygenxml.com/doc/versions/24.1/ug-editor/img/Run16.gif) (Fifth button on the second line of command in XSLT Debugger).

#### PAGE into TEI
The steps are pretty much the same, but the XSL stylesheet file for the transformation will be _xmlpage_to_tei.xsl_.

#### TEI into TEI
This transformation is meant to concatenate all the pages from your transcription into one and only TEI file, as it was the case for the _Text_.

1. Open your command line interface
2. Type ```$ python path/to/tei_to_tei.py path/to/xml/folder path/to/new/xml/file```

The command requires three arguments: the first one is the path to the script, the second one is the path to the folder where your TEI files (from the previous transformation) are located and the third one is the path to the file where all of those TEI files have been concatenated.
