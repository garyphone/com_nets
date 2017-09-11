# Usage of Cube index.html File

In this page, I would like to write a tutorial of the cube index.html in visualization of the OpenStack.

## Background

In CSS part, I should firstly define a background image. The ```background-image``` property specifies an image to use as the background of an element. 

The background image for the page can be set like this:

```
svg {
	background-image: url("https://i.imgur.com/VjZjdtU.jpg");
    }
```

By default, the image is repeated so it covers the entire element. Thus I should be certain the size of the background image. And then define the specific width and height of the **SVG**.

> **Note**: In the OpenStack, the local file path is quite similar as the normal situation. I did not find the exact path to import file with the local path. But with the URL or a specific link I could import the image as the background.

## Other properties in CSS part

With the class of **.link**, I define the properties of the link line. We could change the properties as we need under the configuration of the CSS property.

```
.link {
	fill: none;
	stroke:red;
 	stroke-width: 2px;
}
```
## Main part of HTML

In the part of HTML, I use the JavaScript to build the methods of plotting nodes and connecting nodes. 

1. Import the data file as a JSON format. Here I just did a fake data to achieve the cube network. With a python program, I could convert the XML-file to the json-file and import it in the HTML file.

2. Define the size of the SVG. Here we must note that the size is same as the background image.

```
var svg = d3.select("#body")
   .append("svg")
   .attr("width", 600)
   .attr("height", 480);
```

3. **edges** shows the method of connecting nodes, **nodes** shows the method of plotting nodes, **marks** shows the icons replaces of circles in plotting nodes. Please note that we have to use either **nodes** or **marks** method in HTML.







