## Working with TEI Publisher
As I recommended it in the presentation of the workshop, you should have TEI Publisher installed on your computer, whether it is with eXist or Docker. To work with it, you will first need to launch it. Then, you will have to login to the instance by using the username and password given on the homepage (tei-demo; demo).

### Discovering the playground
1. Go to the __Playground__.
2. Add your XML file into TEI Publisher with the ![](https://cdn.icon-icons.com/icons2/1369/PNG/32/-file-upload_90320.png)__Upload__ box on the right.
3. Once it added, click on it to have it displayed by TEI Publisher.
4. In the toolbar, click on the __Menu__ icon ![](https://cdn.icon-icons.com/icons2/916/PNG/32/Menu_icon_2_icon-icons.com_71856.png) in the far right.
5. Here you can select other ODD and/or templates to see different display of your text. You can also click on _Page view_ to have your text displayed with the page break.

### Developing your own ODD
1. If you are not already there, go back to the homepage of TEI Publisher.
2. In the right side of the page, there is a window full of ODD and you have the possibility, at the bottom, to generate your own.
3. Give a filename and a title for display for your ODD (for example, workshop\_odd and Workshop ODD, or a name related to your corpus), then click on ![](https://cdn.icon-icons.com/icons2/1369/PNG/32/-create_90479.png)__Create__.
4. Click on your ODD, add a new element "persName" and click on ![](https://cdn.icon-icons.com/icons2/1769/PNG/32/4115237-add-plus_114047.png).
5. Once your "persName" tab appears, click on the ![](https://cdn.icon-icons.com/icons2/1769/PNG/32/4115237-add-plus_114047.png) button in the far right, choose _Model_ in the dropdown.
6. A grey window will appear (it contains the different parameters of the element): go to __Renditions__, click on ![](https://cdn.icon-icons.com/icons2/1769/PNG/32/4115237-add-plus_114047.png) and in the form that appears, enter  
`color: red;` and save it with ![](https://cdn.icon-icons.com/icons2/1369/PNG/32/-save_90104.png).
7. Do the same but with "placeName" and _green_ rather than _red_.
8. Go back to the display of your text and with the __Menu__ icon ![](https://cdn.icon-icons.com/icons2/916/PNG/32/Menu_icon_2_icon-icons.com_71856.png), choose your ODD and see your changes.

### Generating your own application
1. If you are logged in, you have in the menu bar, an __Admin__ button, with a dropdown: click on __App Generator__.
2. It leads to a new page where you will enter information about your future application, in order to create it.
3. Select the ODD you've created.
4. Enter the URL for your app: `http://exist-db.org/apps/` then a name (if more than one work, no space, use hyphen or underscore) --> Example: `http://exist-db.org/apps/workshop-tei`.
5. Use the same name for the short name (with the hyphen/underscore).
6. Don't change the name of the subcollection, 'data' is fine.
7. Give a title to your application --> Example: __Workshop TEI 2022__.
8. Select _Shakespeare Play_ as the HTML Template by default (template with the facsimile which will be useful afterwards).
9. Select _By page_ as the browsing by choice, because we have pagebreaks in our TEI file.
10. Leave the __Default Full Text Division__ as _Create on division_.
11. Set a user and password for your application. As your application is only accessible locally and is made for demonstration purposes, your credentials can be basic. For the demonstration, we are using workshop/workshop).
12. Click on ![](https://cdn.icon-icons.com/icons2/1369/PNG/32/-save_90104.png)__SAVE/GENERATE__ and wait until a box open saying that your application has been generated.
13. Go back to the Exist dashboard, refresh the page and your application should now appear.

### Modifying the application to your need
Firstly, to work on your application, you need to login the user and password you've just set, then add your file by using the ![](https://cdn.icon-icons.com/icons2/1369/PNG/32/-file-upload_90320.png) __Upload__ button.  

Now, here are different ways of displaying your files:

#### Displaying the facsimile
1. Access your ODD by clicking on __Admin__ in the menubar, then __Edit OOD: nameofyourodd.odd__.
2. Add the element "pb", open a new model and change the following setting `behaviour = webcomponent` and add the following parameters `name='pb-facs-link'; facs=replace(\@facs, '(.*)$', '$1')`.
3. Save the changes and click on the ![](https://cdn.icon-icons.com/icons2/2368/PNG/32/reload_update_refresh_icon_143703.png)__Reload__ button in the toolbar.
4. Access eXide via the dashboard or the menubar by clicking on __Download__ then __XML__ once you are on your text and login with the same user and password you used to log in your application.
5. Open the template "facsimile.html" by clicking, in the left side of the page, on Directory-->the name of your application-->templates-->pages-->facsimile.html.
6. Go to line 76 "\<pb-facsimile\>" and change the 'base-uri' to "http://localhost:8182/iiif/3/" to match the local Cantaloupe where we have our images.
7. Save the changes, click on ![](https://cdn.icon-icons.com/icons2/685/PNG/32/run_icon-icons.com_61189.png)__Run__, which will lead you to your homepage; click on your file and you should see your image next to your text.

---

#### Creating and displaying modes
1. Access your ODD.
2. Go to the element "persName" (we configured earlier that the rendition should be in red).
3. Add in the predicate `$parameters?mode="red"`.
4. Copy this model by using the ![](https://cdn.icon-icons.com/icons2/933/PNG/32/copy-content_icon-icons.com_72793.png)__Copy__ in the far right.
5. Paste it, while staying in the "persName" tab, by using the ![](https://cdn.icon-icons.com/icons2/933/PNG/32/clipboard-paste-button_icon-icons.com_72805.png)__Paste__ button above the models.
6. Modify this new model by changing _red_ for _green_.
7. Do the same with the "placeName" element.
8. Go to exide and the 'facsimile.html' template.
9. Replace  
`<pb-view id="view1" src="document1" column-separator=".tei-cb" append-footnotes="append-footnotes" subscribe="transcription" emit="transcription" wait-for="#facsimile"/>`  
by  
`<pb-panel id="view1" emit="transcription"><template title="Red"><pb-view src="document1" class=".transcription" subscribe="transcription" emit="transcription"><pb-param name="mode" value="red"/></pb-view></template><template title="Green"><pb-view src="document1" class=".transcription" subscribe="transcription" emit="transcription"><pb-param name="mode" value="green"/></pb-view></template></pb-panel>`
10. Save the changes, click on ![](https://cdn.icon-icons.com/icons2/685/PNG/32/run_icon-icons.com_61189.png)__Run__, which will lead you to your homepage; click on your file and you can now see a dropdown above your text, where you can choose the display you want.

---

#### Working with the index
1. Go to eXide and log in.
2. Open the template "facsimile.html" by clicking, in the left side of the page, on Directory-->the name of your application-->templates-->pages-->facsimile.html.
3. Go to the end of the file and paste after the `\<pb-facsmile\>` the following sequence:  
`<pb-view id="view1" src="document1" column-separator=".tei-cb" append-footnotes="append-footnotes" subscribe="transcription" emit="letter"><pb-param name="mode" value="facets"/></pb-view>`
4. Go to your ODD.
5. Add the element "div", open a _modelSequence_ (second choice on the dropdown) and put in the predicate: `$parameters?mode="facets"`.
6. Add a new model inside the _modelSequence_ with the ![](https://cdn.icon-icons.com/icons2/1769/PNG/32/4115237-add-plus_114047.png) button and put the following informations:
    - Predicate: `descendant::persName`
    - Behaviour: `heading`
    - Parameters: `content='Persons'; level=2`
    - Renditions: `font-weight: 200; border-bottom: 1px solid #A0A0A0;`
 7. Add a new model inside the _modelSequence_ and after this one and put the following informations:
 	- Behaviour: `block`
    - Parameters: `content=for $n in .//persName group by $ref := $n/@ref order by $ref return $n[1]`
 8. Do those tasks again but change both content:
    - 'Places' instead of 'Persons'
    - 'for $n in .//placeName group by $ref := $n/\@ref order by $ref return $n[1]' instead of 'for $n in .//persName group by $ref := $n/\@ref order by $ref return $n[1]'
9. Similarly to what we did with the facsimile, we are going to transform the "placeName" and "persName" we already took care of into webcomponent to make the index appears. Create a new model in each of this element and put the following information:
    - Predicate: `$parameters?mode="facets"`
    - Behaviour: `webcomponent`
    - Parameters: `name='pb-highlight'; key"=substring-after(@ref, '#'); subscribe='letter'; emit='facets'; content=id(substring-after(@ref, '#'), root($parameters?root))`
10. The model in green/red will also be adapted in order to match what we just did. Change the behaviour into _webcomponent_ and add the following parameters:
	- `name='pb-highlight'; content=.; key=substring-after(@ref, '#'); scroll=true(); emit='letter'`
11. Finally, still in each element, add a new model, in first position, with the following information:
	- Predicate: `parent::person` (persName) or `parent::place` (placeName)
    - Behaviour: `inline`
12. Go back to your text, reload the ODD and the index should appear clearly on the right side of the page

---

#### Displaying the sourceDoc
1. Create a new HTML file called "sourcedoc.html" in _Templates_.
2. Replace  
`<pb-view id="view1" src="document1" column-separator=".tei-cb" append-footnotes="append-footnotes" subscribe="transcription" emit="transcription" wait-for="#facsimile"/>`  
by  
`<pb-panel id="view1" emit="transcription"><template title="Body"><pb-view src="document1" subscribe="transcription" emit="transcription"/></template></pb-panel><pb-panel id="view1" emit="transcription"><template title="sourceDoc"><pb-view id="view1" src="document1" xpath="//sourceDoc" view="single" emit="transcription"><pb-param name="mode" value="sourcedoc"/></pb-view></template></pb-panel>`
3. Go to your TEI-XML file with the sourceDoc and add, in the first line of the file, `<?teipublisher template="sourceDoc.html"?>`.
4. Go to your ODD.
5. Add the element "graphic" and change the behaviour of the already existing model that appears from `graphic` to `omit`.
6. Add the elements "sourceDoc" and "surfaceGrp" and put the following informations:
    - Predicate: `$parameters?mode="sourcedoc"`
    - Behaviour: `block`
 7. Add the element "surface" and put the following informations:
    - Predicate: `$parameters?mode="sourcedoc"`
    - Behaviour: `list`
    - Template: `<h5>[[head]]</h5><ul style="border: 1px solid black; padding: 5px;">[[surface]]</ul>`
    - Parameters: `head=upper-case(replace(@type, '_', ' ')); surface=.`
8. Add the element "zone" and put the following informations:
    - Predicate: `$parameters?mode="sourcedoc"`
    - Behaviour: `listItem`
    - Rendition: `list-style: none;`
9. Save the changes, go back to your text, reload the ODD and go see your sourceDoc.

---

#### Creating a collection
1. Go to eXide and login.
2. Click on _File_ at the top of the eXide page, then ![](https://cdn.icon-icons.com/icons2/37/PNG/32/database_theapplication_3365.png)_Manage_.
3. Once the __DB Manager__ opened, go to your app by double-clicking on apps-->name of your application-->data.
4. Click on ![](https://cdn.icon-icons.com/icons2/1365/PNG/32/folder_89347.png)_Create collection_, give a name to your collection and click on __OK__.
5. Cut and paste your XML files into this new collection.
6. Create a new file with ![](https://cdn.icon-icons.com/icons2/1456/PNG/32/mbrinewfile_99512.png)__New__, put _HTML_ as the type and click on __Create__.
7. Copy/paste the following sequence:  
`<div class="collection" data-template="browse:clear-facets"><ul class="documents"><li class="document"><div class="document-info"><h3><a href="#" data-collection="name_of_your_collection">Name of your collection</a></h3><p>Description of your collection.</p></div></li></ul></div>`
8. Save the changes, click on ![](https://cdn.icon-icons.com/icons2/685/PNG/32/run_icon-icons.com_61189.png)__Run__, which will lead you to your homepage to see your collection appears.
