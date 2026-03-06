### Practice with the strerror method.

In this program, I used the 'strerror' method, which translates system error codes into messages that humans 
can understand.

### How it works:
The 'try' block is used to attempt to read the program's contents.

* **Opening the file:** 'open('file', 'rt')' opens the file in **read** and text mode.

* **Initial Read: ** Then, 'stream.readline()' reads the first line of the file so that the while loop has something to execute.

* **line Counting: ** 'line_counter += 1' increments the line count each time the while loop enters.

* **Character Iteration: ** A 'for' loop iterates through each letter on the line containing the text.

* **Printing: ** 'print(letter, end = '')' prints the letter as is, and the end prevents Python from adding an unnecessary line break.

* **Character Counting: ** 'character_counter += 1' adds 1 for each character (including spaces and line breaks).

Finally, 'stream.close()' closes the stream to free system memory. With all the above completed, it 
displays the total counts.





