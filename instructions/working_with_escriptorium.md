## Working with eScriptorium
### Create a new project with your images
1. Go to eScriptorium with the following URL ```https://escriptorium.paris.inria.fr/```.
2. Enter an username and password of your choice after receiving my invite and log into your account.
3. Click on the green button __Create new project__, call it "Workshop TEI 2022" and create it.
4. Open your new project and click on the green button __Create new document__.
5. Give a name to your document, choose a script (probably Latin), check read directions (must be Left to Right) and position of the line (Baseline), then click on the green button __Create__.
6. Once it is done, go to __Images__ and add the images you want to transcribe. Upload them directly on the blue box or if you have a IIIF manifest, click on the blue button __Import__, then _Images (IIIF)_. A pop-up box should open, enter the IIIF manifest URI in the dedicated area and click on the blue button __Start importing__.

### Segment your corpus
1. Press the button __Select all__, and click on __Segment__.
2. The button __Segment__ should open a pop-up box, check that the segmentation model `default (blla.model)` is selected (it should already be automatically selected). Then click on the blue button __Segment__.
3. Once the segmentation is done, you can check each image to check the quality of the automatic segmentation.

### Transcribe your corpus
There is two ways for you to transcribe your corpus:  

1. Manually, with the transcription interface provided by eScriptorium.
2. Automatically, with a machine learning model that you can load in eScriptorium. 

You can also add a transcription already available and made without eScriptorium. It can be imported with the import button, and should be in the XML format. This solution will be the one we will focused on, as the workshop is not intended as a tutorial for working with machine learning models with eScriptorium.

#### Manual transcription
1. Once in the __Images__ tab, click on one of your images.
2. Make sure that you have two views on: __Segmentation__ and __Transcription__ (2nd and 3rd buttons on the far right of the page)
3. Click on the empty box in the __Transcription__ and add the transcription by hand.

#### Automatic transcription
1. Download your images segmented in the _ALTO_ format.
2. Unzip it and make sure that the images are numbered (example: filename_1.xml, filename_2.xml).
3. Open your transcription (TXT file) and put the following characters at each page break:  
`==--==--==--==` followed by a linebreak (_\n_).
4. Open the Python script _text\_alignement.xml_ and at lines 73 and 82, change `PP3_p` by the name of your file prior the number.
5. Save thoses changes, open your terminal and enter the following command:  
```$ python text_alignement.xml --xml path/to/the/ALTO/files --txt path/to/the/TXT/file```
6. Go to the folder of ALTO files; there should be new files, ending with _.modified.xml_.
7. In your terminal, go to this folder (`$ cd path/to/the/ALTO/folder`) and enter the following command:
```$ zip -r -X transcript.zip *.modified.xml``` which will create a zip of your ALTO files
8. In eScriptorium, when you are in the __Images__ tab, click on ![](https://cdn.icon-icons.com/icons2/1875/PNG/32/fileimport_120157.png)__Import__ and choose _Transcription (XML)_.
9. Select _Override existing segmentation._ and click on __Parcourir__, where you will retrieve the zip previously created.
10. Click on __Start importing__ then check your transcription for any error.

### Export your corpus
#### In raw text format
1. Press the button __Select all__, then ![](https://cdn.icon-icons.com/icons2/1875/PNG/32/fileexport_120162.png)__Export__.
2. Select the correct transcription in the first drop-down menu, choose _Text_ in the second drop-down menu.
3. Press the ![](https://cdn.icon-icons.com/icons2/1875/PNG/32/fileexport_120162.png)__Export__ button.
4. Once the green window appear on your page, click on _Download_ and a new window with your text will appear.
5. Select all (Cmd+A), copy (Cmd+C) and paste it (Cmd+V) on your text editor .
6. Save it with the name of your choice and with the extension _.txt_.

#### In ALTO or PAGE format
1. Press the button __Select all__, then ![](https://cdn.icon-icons.com/icons2/1875/PNG/32/fileexport_120162.png)__Export__
2. Select the correct transcription in the first drop-down menu, choose _ALTO_ or _PAGE_ in the second drop-down menu.
3. Press the ![](https://cdn.icon-icons.com/icons2/1875/PNG/32/fileexport_120162.png)__Export__ button.
4. Once the green window appear on your page, click on _Download_ and a zip will be downloaded.
5. Unzip it, rename the folder created (for an easier access) and you will have, at your disposal, your ALTO or PAGE XML files.
