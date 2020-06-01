# ¡Bienvenido a StackEdit!

¡Hola! Soy tu primer archivo Markdown en ** StackEdit ** . Si quieres aprender sobre StackEdit, puedes leerme. Si quieres jugar con Markdown, puedes editarme. Una vez que haya terminado conmigo, puede crear nuevos archivos abriendo el ** explorador de archivos ** en la esquina izquierda de la barra de navegación.


# Archivos

StackEdit almacena sus archivos en su navegador, lo que significa que todos sus archivos se guardan automáticamente y son accesibles ** sin conexión. ** **

## Crear archivos y carpetas

Se puede acceder al explorador de archivos usando el botón en la esquina izquierda de la barra de navegación. Puede crear un nuevo archivo haciendo clic en el botón ** Nuevo archivo ** en el explorador de archivos. También puede crear carpetas haciendo clic en el botón ** Nueva carpeta ** .

## Cambiar a otro archivo

Todos sus archivos y carpetas se presentan como un árbol en el explorador de archivos. Puede cambiar de uno a otro haciendo clic en un archivo en el árbol.

## Cambiar el nombre de un archivo

Puede cambiar el nombre del archivo actual haciendo clic en el nombre del archivo en la barra de navegación o haciendo clic en el botón ** Cambiar nombre ** en el explorador de archivos.

## Eliminar un archivo

Puede eliminar el archivo actual haciendo clic en el botón ** Eliminar ** en el explorador de archivos. El archivo se mueve a la carpeta ** Papelera ** y se elimina automáticamente después de 7 días de inactividad.

## Exportar un archivo

Puede exportar el archivo actual haciendo clic en ** Exportar una discoteca ** en el menú. Puede optar por exportar el archivo como Markdown simple, como HTML usando una plantilla de Manillares o como PDF.


# Synchronization

Synchronization is one of the biggest features of StackEdit. It enables you to synchronize any file in your workspace with other files stored in your **Google Drive**, your **Dropbox** and your **GitHub** accounts. This allows you to keep writing on other devices, collaborate with people you share the file with, integrate easily into your workflow... The synchronization mechanism takes place every minute in the background, downloading, merging, and uploading file modifications.

There are two types of synchronization and they can complement each other:

- The workspace synchronization will sync all your files, folders and settings automatically. This will allow you to fetch your workspace on any other device.
	> To start syncing your workspace, just sign in with Google in the menu.

- The file synchronization will keep one file of the workspace synced with one or multiple files in **Google Drive**, **Dropbox** or **GitHub**.
	> Before starting to sync files, you must link an account in the **Synchronize** sub-menu.

## Open a file

You can open a file from **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Open from**. Once opened in the workspace, any modification in the file will be automatically synced.

## Save a file

You can save any file of the workspace to **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Save on**. Even if a file in the workspace is already synced, you can save it to another location. StackEdit can sync one file with multiple locations and accounts.

## Synchronize a file

Once your file is linked to a synchronized location, StackEdit will periodically synchronize it by downloading/uploading any modification. A merge will be performed if necessary and conflicts will be resolved.

If you just have modified your file and you want to force syncing, click the **Synchronize now** button in the navigation bar.

> **Note:** The **Synchronize now** button is disabled if you have no file to synchronize.

## Manage file synchronization

Since one file can be synced with multiple locations, you can list and manage synchronized locations by clicking **File synchronization** in the **Synchronize** sub-menu. This allows you to list and remove synchronized locations that are linked to your file.


# Publication

Publishing in StackEdit makes it simple for you to publish online your files. Once you're happy with a file, you can publish it to different hosting platforms like **Blogger**, **Dropbox**, **Gist**, **GitHub**, **Google Drive**, **WordPress** and **Zendesk**. With [Handlebars templates](http://handlebarsjs.com/), you have full control over what you export.

> Before starting to publish, you must link an account in the **Publish** sub-menu.

## Publish a File

You can publish your file by opening the **Publish** sub-menu and by clicking **Publish to**. For some locations, you can choose between the following formats:

- Markdown: publish the Markdown text on a website that can interpret it (**GitHub** for instance),
- HTML: publish the file converted to HTML via a Handlebars template (on a blog for example).

## Update a publication

After publishing, StackEdit keeps your file linked to that publication which makes it easy for you to re-publish it. Once you have modified your file and you want to update your publication, click on the **Publish now** button in the navigation bar.

> **Note:** The **Publish now** button is disabled if your file has not been published yet.

## Manage file publication

Since one file can be published to multiple locations, you can list and manage publish locations by clicking **File publication** in the **Publish** sub-menu. This allows you to list and remove publication locations that are linked to your file.


# Markdown extensions

StackEdit extends the standard Markdown syntax by adding extra **Markdown extensions**, providing you with some nice features.

> **ProTip:** You can disable any **Markdown extension** in the **File properties** dialog.


## SmartyPants

SmartyPants converts ASCII punctuation characters into "smart" typographic punctuation HTML entities. For example:

|                |ASCII                          |HTML                         |
|----------------|-------------------------------|-----------------------------|
|Single backticks|`'Isn't this fun?'`            |'Isn't this fun?'            |
|Quotes          |`"Isn't this fun?"`            |"Isn't this fun?"            |
|Dashes          |`-- is en-dash, --- is em-dash`|-- is en-dash, --- is em-dash|


## KaTeX

You can render LaTeX mathematical expressions using [KaTeX](https://khan.github.io/KaTeX/):

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

> You can find more information about **LaTeX** mathematical expressions [here](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference).


## UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

` `  `
 secuencia de sirena Diagrama 
Alice - >> Bob: Hola Bob, ¿cómo estás? 
Bob - >> John: ¿Y tú, John? 
Bob - x Alice: Estoy bien, gracias! 
Bob-x John: Estoy bien, gracias! 
Nota a la derecha de John: Bob piensa mucho <br/> mucho tiempo, tanto <br/> que el texto <br/> no cabe en una fila. Bob -> Alice: Consultando con John ... Alice-> John: Sí ... John, ¿cómo estás? ` ` `





Y esto produce un diagrama de flujo:

` `  `
 gráfico de sirena LR 
A [Rect. Cuadrada] - Texto de enlace -> B ((Círculo)) 
A -> C (Rect. Redonda) 
B -> D {Rombo} 
C -> D `  ` `

<!--stackedit_data:
eyJoaXN0b3J5IjpbOTM3Mjg5ODE5XX0=
-->