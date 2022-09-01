## Working on eScriptorium
### Create a new project with your images
1. Go to eScriptorium with the following URL ```https://escriptorium.paris.inria.fr/```
2. Enter your username and password that you decide after receiving my invite and login
3. Click on the green button __Create new project__, call it "Workshop TEI 2022" and create it
4. Go to that new project and click on the green button __Create new document__
5. Give a name to your project, choose a script (probably Latin), check read directions (must be Left to Right) and position of the line (Baseline), then create
6. Once it is done, go to __Images__ and add the images for your transformation. Upload them directly on the blue box or if you have a IIIF manifest, click on the blue button __Import__, then _Images (IIIF)_, and enter on the window that opens the link to your manifest.

### Segment your corpus
1. Press the button __Select all__ click on the blue button __Binarize__ and/or __Segment__
2. With the __Segment__ window that opens, choose the `default (blla.model)`
3. Once the segmentation done, click on each of your images and verify if the segmentation is good

### Transcribe your corpus
There is two ways for you to transcribe your corpus:  

1. Manually (on eScriptorium)
2. Automatically, if you already have the transcription (with a Python script)

#### Manual transcription
1. Once in the __Images__ tab, click on one of your images
2. Make sure that you have two views on: __Segmentation__ and __Transcription__ (2nd and 3rd buttons on the far right of the page)
3. Click on the empty box in the __Transcription__ and add the transcription

#### Automatic transcription
...

### Export your corpus
#### In the text format
1. Press the button __Select all__, then __Export__
2. Select in the first window of choice the correct transcription of your images and choose _Text_ for the second window
3. Press the __Export__ button
4. Once the green window appear on your page, click on _Download_ and a new window with your text will appear
5. Select all (Cmd+A), copy (Cmd+C) and paste it (Cmd+V) on your text editor 
6. Save it with the name of your choice and with the extension _.txt_

#### In the ALTO or PAGE format
1. Press the button __Select all__, then __Export__
2. Select in the first window of choice the correct transcription of your images and choose _ALTO_ or _PAGE_ (according to what you prefer) for the second window
3. Press the __Export__ button
4. Once the green window appear on your page, click on _Download_ and a zip will be downloaded
5. Unzip it, rename the folder created (for an easier access) and you will have, at your disposal, your ALTO or PAGE XML files