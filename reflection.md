# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The hint doesn't work, it continuesly tell you to go higher when the secret number is lower and vice versa.

New Game didn’t reset the game properly. Even after clicking it, the app still stayed in ‘Game over’ mode and wouldn’t give hints anymore. 

The difficulty level is wrong too. Normal and hard mode are misplaced.Hard mode is actually easier than “Normal. When you select Hard, the secret number range becomes smaller instead of harder. 

The game always tells you “Guess a number between 1 and 100” even when difficulty changes.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot and Gemini to help me debug and fix the game. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One correct AI suggestion was to reset st.session_state.status back to "playing" inside the New Game button code, because the game was staying stuck in “Game over” mode. I verified it by running the app, losing on purpose, clicking New Game, and confirming the game restarted normally with hints working again instead of showing the game-over message.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

At first, the AI suggested using a try/except to avoid the TypeError when comparing numbers. That stopped the crash, but it didn’t fix the real problem, which was that the secret number sometimes became a string. I confirmed this by seeing the same issue happen again, and then fixing it properly by keeping the secret number as an integer.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  I decided that a bug was really fixed by first making the changes,then repeated the same steps to see if the issue was gone. I checked the app behavior in different situations (winning, losing, clicking New Game, and making high/low guesses) to make sure it stayed consistent. I also ran pytest to completelely varifying the issue has been fixed.

- Did AI help you design or understand any tests? How?

AI helped me understand tests better by helping me design the test cases in a that it is efffective. For example, like guessing 60 when the secret is 50, and losing then clicking New Game.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing in the original app because whenever I interect with the app, it reruns the script over the over. That's why the secret number was being created again during reruns even though I hadn’t started a new game.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit apps refresh the Python file every time you do something on the page. If you want something to stay the same, you store it in st.session_state, which is like a memory box that keeps values between reruns.

- What change did you make that finally gave the game a stable secret number?
I made sure the secret number is only set when starting a new game and kept it stored in st.session_state.secret as an integer, instead of changing it during normal guesses.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
One habit is always manually testing the code since you can't trust AI always and it can make mistakes that really hard to notice.

  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time I would, narrow down problem scope with asking AI for help. I will start with real small question that address the issue first and give overview of the code and one problem at a time.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated code can be really helpful however it need heavy human supervision to ensure accuaracy. You need to continuously manualy check and test the code. It can never give you the final accurate answers so you need always verify changes by running the app and tests. 