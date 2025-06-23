# AI-Powered Text Completion Writeup

### Part 1: Building the Application
I decided to use OpenAI as my GenAI model becuase I've had past experience working with its API.
For this, I had to download openai to work with the platform. I did so in the terminal: 
```pip install openai```
I had a pretty easy time setting it up and used free trial tokens to generate text and play around with the API.

### Part 2: Debugging and Improving the Application
I had the hardest time dealing with how to safely use API keys.
I learned that hardcoding the key directly is insecure, especially because I'm sharing the project to a GitHub repo.
So I decided to load the API key from an environment variable using Python's ```os``` module.
Before running the script, in the terminal, you'd have to:
```export OPEN_API_KEY="the-api-key"```.
I accidentally kept labeling the api-key as "OPENAI_API_KEY" rather than "OPEN_API_KEY", which was a typo that wouldn't let me access my credits.

I added basic input validation, so the chatbot would prompt the user to try again on empty inputs and exit when the user types ```exit``` or ```quit```.
I also used ```.strip()``` to catch white-space only input.
To catch common API errors like invalid keys or exceeding usage quota, I wrapped the request in a try/except block to catch all exceptions.
This helped the application run smoothly if there was a network error or bad request without crashing.
These minor changes helped streamline the user experience and improved the application/

### Part 3: Experimentation and Evaluation
I tried a lot of different prompts accross different domains. Here are three different examples of prompts and their outputs:

writeup1.png

The first prompt asks for a short haiku, which is pretty creative and lets the chatbot create something one of a kind. 
The second prompt is very creative as well. 
Asking the model to continue a story gives it a lot of variability, but including that it should be about a “student” makes the output more straightforward. 
The third and final prompt is instructional, giving the model a little less variability with its output. 
All of the outputs are very realistic and helpful, as the model rarely hallucinates and generates realistic outputs for all kinds of prompts. 

For these few prompts, the responses were realistic and helpful to the prompt type. 
One reason for this consistency is the system message I set in the chatbot’s prompt structure.
in line 34 of ```text_completion_app.py```, you can see that I told the app “You are a helpful assistant.” 
This message establishes the assistant’s tone and behavior, which is why the output was consistently polite and useful, even for more creative prompts.

writeup2.png

I experimented with many different system messages, and the generated responses were pretty much spot on to what I described. 
Below is the output for the same three prompts when the system message is changed to “You answer questions like a pirate.”

writeup3.png

You can see that the chatbot added a lot of phrases we associate with pirates, like “arr!”, even though it was answering the same prompts.
I found it very cool how it managed to hit the question while still maintaining a pirate’s way of speech.
It was so fun experimenting with these different prompts and discovering how the GenAI would react!

One way I could improve the output is by saving the entire chat history and having the model questions based on that too, to improve customer experience.


