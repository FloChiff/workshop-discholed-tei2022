<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<?xml-stylesheet type="text/xsl"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0" xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs xi xsi pc" xmlns="http://www.tei-c.org/ns/1.0" xmlns:xi="http://www.w3.org/2001/XInclude"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15 http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15/pagecontent.xsd"
    xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15">

    <xsl:output method="xml" indent="yes" encoding="UTF-8"/>

    <xsl:template match="/">


        <!-- Create a variable to store the xml files in the folder by the function collection() -->
        <xsl:variable name="file" as="document-node()+" select="collection('../text/xml/?select=*page.xml')"/>

        <!-- The collection is processed file by file -->
        <xsl:for-each select="$file">
            <!-- Create a variable that will store the filename of the file currently processed -->
            <xsl:variable name="filename" as="xs:string" select="base-uri() ! tokenize(., '/')[last()] ! substring-before(., '.xml')"/>
            <!-- Creation of a variable for storing the file's name -->
            <xsl:variable name="file_name">
                <xsl:value-of select="replace(/pc:PcGts/pc:Page/@imageFilename, '.png', '')"/>
            </xsl:variable>
            <!-- Give the path to the output of the newly transformed files -->
            <xsl:result-document method="xml" indent="yes" href="../xml/xml_to_xml/{$filename}.xml">
                <!-- teiHeader elements -->
                <TEI>
                    <teiHeader>
                        <fileDesc>
                            <titleStmt>
                                <title>
                                    <xsl:value-of select="$file_name"/>
                                </title>
                                <respStmt>
                                    <resp>Transcribed with</resp>
                                    <name>
                                        <xsl:value-of select="pc:PcGts/pc:Metadata/pc:Creator"/>
                                    </name>
                                </respStmt>
                            </titleStmt>
                            <publicationStmt>
                                <p/>
                            </publicationStmt>
                            <sourceDesc>
                                <p/>
                            </sourceDesc>
                        </fileDesc>
                        <revisionDesc>
                            <xsl:element name="change"><xsl:attribute name="when"><xsl:value-of select="pc:PcGts/pc:Metadata/pc:Created"
                                    /></xsl:attribute>Creation</xsl:element>
                            <xsl:element name="change"><xsl:attribute name="when"><xsl:value-of select="pc:PcGts/pc:Metadata/pc:LastChange"
                                    /></xsl:attribute>Last change</xsl:element>
                        </revisionDesc>
                    </teiHeader>
                    <sourceDoc>
                        <!-- A <graphic> TEI element is used for tagging attributes of the <Page> node in the PAGE XML -->
                        <graphic>
                            <xsl:attribute name="url">
                                <xsl:value-of select="/pc:PcGts/pc:Page/@imageFilename"/>
                            </xsl:attribute>
                            <xsl:attribute name="width">
                                <xsl:value-of select="concat(//pc:Page/@imageWidth, 'px')"/>
                            </xsl:attribute>
                            <xsl:attribute name="height">
                                <xsl:value-of select="concat(//@imageHeight, 'px')"/>
                            </xsl:attribute>
                        </graphic>
                        <surfaceGrp>
                            <xsl:apply-templates select="//pc:Page" mode="surface"/>
                        </surfaceGrp>
                    </sourceDoc>
                    <text>
                        <body>
                            <div type="transcription">
                                <pb>
                                    <xsl:attribute name="facs">
                                        <xsl:value-of select="/pc:PcGts/pc:Page/@imageFilename"/>
                                    </xsl:attribute>
                                </pb>
                                <!-- Options for choosing the transformation needed for the body according to the type of files -->
                                <!-- If you don't want content in the body, it is possible to leave everything in comments -->

                                <!--<table><xsl:apply-templates select="//pc:Page" mode="table"/></table>-->
                                <!--<xsl:apply-templates select="//pc:Page" mode="poem"/>-->
                                <xsl:apply-templates select="//pc:Page" mode="standard"/>
                            </div>
                        </body>
                    </text>
                </TEI>
            </xsl:result-document>
        </xsl:for-each>

    </xsl:template>
    <!-- A <TextRegion> node in the PAGE XML becomes a <surface> element in the TEI -->
    <!-- <surface> in the TEI represents all baselines associated with a <TextRegion> in the PAGE XML -->
    <xsl:template match="//pc:TextRegion" mode="surface">
        <xsl:element name="surface">
            <xsl:attribute name="xml:id">
                <xsl:value-of select="@id"/>
            </xsl:attribute>
            <xsl:attribute name="type">
                <xsl:choose>
                    <xsl:when test="@custom">
                        <xsl:value-of select="replace(replace(@custom, 'structure \{type:', ''), ';\}', '')"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of>none</xsl:value-of>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:choose>
                <xsl:when test="pc:Coords/@points">
                    <xsl:attribute name="points">
                        <xsl:value-of select="pc:Coords/@points"/>
                    </xsl:attribute>
                </xsl:when>
            </xsl:choose>
            <!-- For each <TextLine> in the PAGE XML, a <zone> element is created in the TEI. -->
            <xsl:for-each select="pc:TextLine">
                <!-- <zone> in the TEI represents baseline's mask in the PAGE XML -->
                <xsl:element name="zone">
                    <xsl:attribute name="xml:id">
                        <xsl:value-of select="@id"/>
                    </xsl:attribute>
                    <xsl:attribute name="type">
                        <xsl:value-of>mask</xsl:value-of>
                    </xsl:attribute>
                    <xsl:attribute name="points">
                        <xsl:value-of select="pc:Coords/@points"/>
                    </xsl:attribute>
                    <!-- <path> in the TEI represents baseline's coordinates -->
                    <xsl:element name="path">
                        <xsl:attribute name="type">
                            <xsl:value-of>baseline</xsl:value-of>
                        </xsl:attribute>
                        <xsl:attribute name="points">
                            <xsl:value-of select="pc:Baseline/@points"/>
                        </xsl:attribute>
                    </xsl:element>
                    <!-- <line> element in the TEI represents the transcription in the PAGE XML -->
                    <xsl:element name="line">
                        <xsl:value-of select="pc:TextEquiv/pc:Unicode"/>
                    </xsl:element>
                </xsl:element>
            </xsl:for-each>
        </xsl:element>
    </xsl:template>

    <!-- Templates to display the text in the body according to the kind of files -->
    <xsl:template match="//pc:TextRegion" mode="table">
        <xsl:element name="row">
            <xsl:for-each select="pc:TextLine">
                <xsl:element name="cell">
                    <xsl:value-of select="pc:TextEquiv/pc:Unicode"/>
                </xsl:element>
            </xsl:for-each>
        </xsl:element>
    </xsl:template>

    <xsl:template match="//pc:TextRegion" mode="poem">
        <xsl:element name="lg">
            <xsl:for-each select="pc:TextLine">
                <xsl:element name="l">
                    <xsl:value-of select="pc:TextEquiv/pc:Unicode"/>
                </xsl:element>
            </xsl:for-each>
        </xsl:element>
    </xsl:template>

    <xsl:template match="//pc:TextRegion" mode="standard">
        <xsl:element name="div">
            <xsl:element name="p">
                <xsl:for-each select="pc:TextLine">
                    <xsl:value-of select="pc:TextEquiv/pc:Unicode"/>
                    <xsl:element name="lb"/>
                    <xsl:text> </xsl:text>
                </xsl:for-each>
            </xsl:element>
        </xsl:element>
    </xsl:template>

</xsl:stylesheet>
