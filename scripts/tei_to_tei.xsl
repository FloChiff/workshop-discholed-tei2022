<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tei="http://www.tei-c.org/ns/1.0"
    xpath-default-namespace="http://www.tei-c.org/ns/1.0" xmlns="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs tei" version="2.0">
    
    <xsl:output method="xml" indent="yes"/>
    
    <xsl:template match="/">
        <!-- Create a variable to store the xml files in the folder by the function collection() -->
        <xsl:variable name="files" select="collection('../xml/xml_to_xml/?select=*page.xml')"/>
        <!-- Give the path to the output of the newly transformed file -->
        <xsl:result-document method="xml" indent="yes" href="../tei/tei_out.xml">
        <TEI>
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
                <!-- This will call all the sourceDoc from the files and put it in the single XML file -->
                    <xsl:copy-of select="$files//sourceDoc"/>
                <text>
                <body>
                    <!-- This will call all the div[@type="transcription"] from the files and put it in the single XML file -->
                    <xsl:copy-of select='$files//div[@type="transcription"]'/>
                </body>
            </text>
        </TEI>
        </xsl:result-document>
    </xsl:template>
    
    
</xsl:stylesheet>