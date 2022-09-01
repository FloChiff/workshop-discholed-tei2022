## Working with TEI Publisher
As I recommended it in the presentation of the workshop, you should have TEI Publisher installed on your computer, whether it is with eXist or Docker. To work with it, you will first need to launch it. Then, you will have to login to the instance by using the username and password given on the homepage (tei-demo; demo).

### Discovering the playground
1. Go to __Playground__
2. Add your XML file into TEI Publisher with the ![](https://cdn.icon-icons.com/icons2/1369/PNG/32/-file-upload_90320.png)__Upload__ box on the right
3. Once it added, click on it to have it displayed by TEI Publisher
4. In the toolbar, click on the __Menu__ icon ![](https://cdn.icon-icons.com/icons2/916/PNG/32/Menu_icon_2_icon-icons.com_71856.png) in the far right
5. Here you can select other ODD and/or templates to see different display of your text. You can also click on _Page view_ to have your text displayed with the page break

### Developing your own ODD
1. If you are not already there, go back to the homepage of TEI Publisher
2. In the right side of the page, there is a window full of ODD and you have the possibility, at the bottom, to generate your own
3. Give a filename and a title for display for your ODD (for example, workshop\_odd and Workshop ODD, or a name related to your corpus), then click on ![](https://cdn.icon-icons.com/icons2/1369/PNG/32/-create_90479.png)__Create__
4. Click on your ODD, add a new element "persName" and click on ![](https://cdn.icon-icons.com/icons2/1769/PNG/32/4115237-add-plus_114047.png)
5. Once your "persName" tab appears, click on the ![](https://cdn.icon-icons.com/icons2/1769/PNG/32/4115237-add-plus_114047.png) button in the far right, choose _Model_ in the dropdown
6. A grey window will appear (it contains the different parameters of the element): go to __Renditions__, click on ![](https://cdn.icon-icons.com/icons2/1769/PNG/32/4115237-add-plus_114047.png) and in the form that appears, enter  
`color: red;` and save it with ![](https://cdn.icon-icons.com/icons2/1369/PNG/32/-save_90104.png)
7. Do the same but with "placeName" and _green_ rather than _red_
8. Go back to the display of your text and with the __Menu__ icon ![](https://cdn.icon-icons.com/icons2/916/PNG/32/Menu_icon_2_icon-icons.com_71856.png), choose your ODD and see your changes

### Generating your own application
1. If you are logged in, you have in the menu bar, an __Admin__ button, with a dropdown: click on __App Generator__
2. It leads to a new page where you will enter information about your future application, in order to create it
3. Select the ODD you've created
4. Enter the URL for your app: `http://exist-db.org/apps/` then a name (if more than one work, no space, use hyphen or underscore) --> Example: `http://exist-db.org/apps/workshop-tei`
5. Use the same name for the short name (with the hyphen/underscore)
6. Don't change the name of the subcollection, data is fine
7. Give a title to your application --> Example: __Workshop TEI 2022__
8. Select _Shakespeare Play_ as the HTML Template by default (template with the facsimile which will be useful afterwards)
9. Select _By page_ as the browsing by choice, because we have pagebreaks in our TEI file
10. Leave the __Default Full Text Division__ as _Create on division_
11. Set a user and password for your application (you can stay simple as it is a beta version locally present: here, it is workshop/workshop)
12. Click on ![](https://cdn.icon-icons.com/icons2/1369/PNG/32/-save_90104.png)__SAVE/GENERATE__ and wait until a box open saying that your application has been generated
13. Go back to the dashboard of exist, refresh the page and your application should appear

### Modifying the application to your need
Firstly, to work on your application, you need to login the user and password you set, then add your file by using the ![](https://cdn.icon-icons.com/icons2/1369/PNG/32/-file-upload_90320.png) __Upload__ button.  
Now, here are different displays possible

#### Displaying the facsimile
1. Access your ODD by clicking on __Admin__ in the menubar, then __Edit OOD: nameofyourodd.odd__
2. Add the element "pb", open a new model and change the following setting `behaviour = webcomponent` and add the following parameters `name='pb-facs-link'; content=\@n; facs=replace(\@facs, '(.*)$', '$1')`
3. Save the changes and click on the ![](https://cdn.icon-icons.com/icons2/2368/PNG/32/reload_update_refresh_icon_143703.png)__Reload__ button in the toolbar
4. Acces exide via the dashboard or the menubar by clicking on __Download__ then __XML__ once you are on your text and login with the same user and password you used on the application
5. Open the template "facsimile.html" by clicking, in the left side of the page, on Directory-->the name of your application-->templates-->pages-->facsimile.html
6. Go to line 76 "\<pb-facsimile\>" and change the 'base-uri' to "http://localhost:8182/iiif/3/" to match the local Cantaloupe where we have our images
7. Save the changes, click on ![](https://cdn.icon-icons.com/icons2/685/PNG/32/run_icon-icons.com_61189.png)__Run__, which will lead you to your homepage; click on your file and you should see your image next to your text

#### Creating and displaying modes
1. Access your ODD
2. Go to the element "persName" (where we have a rendition setting that it should be red)
3. Add in the predicate `$parameters?mode="red"`
4. Copy this model by using the ![](https://cdn.icon-icons.com/icons2/933/PNG/32/copy-content_icon-icons.com_72793.png)__Copy__ in the far right
5. Paste it, while staying in the "persName" tab, by using the ![](https://cdn.icon-icons.com/icons2/933/PNG/32/clipboard-paste-button_icon-icons.com_72805.png)__Paste__ button above the models
6. Modify this new model by changing _red_ for _green_
7. Do the same with the "placeName" element
8. Go to exide and the 'facsimile.html' template
9. Replace  
`<pb-view id="view1" src="document1" column-separator=".tei-cb" append-footnotes="append-footnotes" subscribe="transcription" emit="transcription" wait-for="#facsimile"/>`  
by  
`<pb-panel id="view1" emit="transcription"><template title="Red"><pb-view src="document1" class=".transcription" subscribe="transcription" emit="transcription"><pb-param name="mode" value="red"/></pb-view></template><template title="Green"><pb-view src="document1" class=".transcription" subscribe="transcription" emit="transcription"><pb-param name="mode" value="green"/></pb-view></template></pb-panel>`
10. Save the changes, click on ![](https://cdn.icon-icons.com/icons2/685/PNG/32/run_icon-icons.com_61189.png)__Run__, which will lead you to your homepage; click on your file and you can now see a dropdown above your text, where you can choose the display you want

#### Working with the index
...  

#### Displaying the sourceDoc
...
