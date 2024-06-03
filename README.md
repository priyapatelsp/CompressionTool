<h1>Compression Tool  </h1>

Compression Tool is a tool prepared using Leveraging Huffman coding, it efficiently compresses files, optimizing storage and enhancing data management using Python . 

<h1>Get started </h1>
This tool is in Python , so please ensure that you have latest Python version installed in your device 
<br><br>

step 1: git clone https://github.com/priyapatelsp/CompressionTool.git

step 2: Follow the below steps to start the program 
<h3>Compressing :: </h3>
Please type the below command to execute this python program <br><br>

Step 1: Navigate to the location of the folder and then type below code(since I've used Python3)
````
Python3
````
Step 2: Then import the compressionTool
````
from compressionTool import CompressionTool
````
Step 3: Define a path variable - it's the location of the text file you need to compress.
````
path="{PATH OF THE TEXT FILE YOU NEED TO COMPRESS}"
````
Step 4: Make an object for compression tool 
````
compressionObj=CompressionTool(path)
````
Step 5: Call the function to compress the file 
````
compressionObj.compress()
````
<h5>You will get the path of compressed file, you can observe the decresed file size. To get it decompressed and open the file you can follow below steps<h5>

<h3>Decompressing :: </h3>
Please type the below command to open the compressed file <br><br>

Step 1: Define a path variable - it's the location of the compressed text file.
````
pathCompressedFile="{PATH OF THE COMPRESSED .BON FILE YOU GOT}"
````
Step 2:Call the function to compress the file on terminal after following above steps 
````
compressionObj.decompress(pathCompressedFile)
````

<h3> Useful resources for Huffman coding </h3>
<a href="https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/">huffman-coding-greedy</a>
<br>
<a href="https://www.geeksforgeeks.org/huffman-coding-using-priority-queue/?ref=lbp">huffman-coding-using-priority-queue</a><br>
<a href="https://www.youtube.com/watch?v=JCOph23TQTY">huffman-coding-python</a>

<h1>Author</h1><br>
Priya Patel <br>
Github : <a href="https://github.com/priyapatelsp">priyapatelsp</a>
