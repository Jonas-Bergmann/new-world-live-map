# New World Live Map

This is a tool that shows a minimap with your live location for **New World**.

It grabs your in-game location from the location text ingame that's being displayed when enabling the *"Show FPS Counter"* option.  
Since it uses absolute values that depend on your monitors resolution this tool ***can*** work for you but I cannot guarantee it.

The **New World Live Map** shows the map using matplotlib since it has a zoom and move feature and I don't know how to code that so we will use matplotlib for now.


## Installing Tesseract

This project uses tesseract. You can install tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki).
You may need to add tesseract to your *PATH*.


## Preview

Here is the whole map with the current position marker:

![Image](https://user-images.githubusercontent.com/61794769/137268466-ff75e324-27a0-4b77-8cd9-62c9bdaf9945.png)

You can also zoom in with matplotlib to get a more detailed map:

![Image2](https://user-images.githubusercontent.com/61794769/137268559-69444f7b-f1d3-4329-8319-726aca9d8e7f.png)
