## Uploading pictures on your local Cantaloupe server

1. Cantaloupe must be downloaded on your computer and in an easily accessible place. See [Cantaloupe website](https://cantaloupe-project.github.io/).
2. Create a folder for images or choose an already existing folder with images and copy the absolute path of this folder.
3. Go to your Cantaloupe folder, make a copy of the file "cantaloupe.properties.sample", rename it by removing ".sample".
4. Open the file, search for `FilesystemSource.BasicLookupStrategy.path_prefix` and change the existing path to the path leading to your folder of images (step 2)
5. Open your command line interface (terminal), go to the folder of Cantaloupe by typing:
```$ cd /path/to/Cantaloupe```  
Then activate Cantaloupe with the following command:
```$ java -Dcantaloupe.config=cantaloupe.properties -Xmx2g -jar cantaloupe-5.0.5.jar```
6. Once this is done, open your browser and enter the following URL (change _name_of_the_file.extension_ with the name of one of your images)  
```http://localhost:8182/iiif/3/{name_of_the_file.extension}/full/max/0/default.jpg```.
7. Your image should be displayed on the browser.
