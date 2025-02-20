# aBot - Discord Moderation & AI Code Helper Bot

aBot is a powerful Discord bot designed to perform essential moderation tasks while also featuring an AI-powered code helper for programmers.

## Features
- **Moderation Commands**
  - Kick users
  - Ban users
  - Clear messages
- **Utility Commands**
  - Ping for bot latency
  - Fetch user info
  - Track inactive users
- **AI Code Helper**
  - Analyze and provide insights on code snippets using OpenAI GPT-4
- **Error Handling**
  - Handles missing permissions and missing arguments gracefully

## Project Structure
```
📂 aBot/
├── 📄 main.py         # Entry point to start the bot
├── 📄 bot_setup.py    # Initializes the bot and manages intents
├── 📄 moderation.py   # Contains moderation commands
├── 📄 utilities.py    # Contains general utility commands
├── 📄 ai_helper.py    # Implements AI-based code analysis
├── 📄 error_handling.py # Handles command errors globally
└── 📄 README.md       # Project documentation
```

## Installation
### Prerequisites
- Python 3.8+
- Discord Bot Token
- OpenAI API Key

### Setup Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/abot_project.git
   cd abot_project
   ```
2. Install required dependencies:
   ```bash
   pip install discord.py openai python-dotenv
   ```
3. Create a `.env` file and add:
   ```env
   DISCORD_BOT_TOKEN=your_token_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   **Important:** Never expose your API keys in public repositories. Use environment variables or a `.env` file to keep them secure.

4. Run the bot:
   ```bash
   python main.py
   ```

## Usage
### Moderation Commands
- `!kick @user [reason]` - Kicks a user from the server
- `!ban @user [reason]` - Bans a user from the server
- `!clear [number]` - Clears a specified number of messages

### Utility Commands
- `!ping` - Checks bot latency
- `!userinfo @user` - Displays user information
- `!inactive [days]` - Lists users inactive for more than a certain number of days

### AI Code Helper
- `!analyze [code]` - Analyzes and provides feedback on code snippets

## Contributing
Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, open an issue in the repository or reach out on Discord.

---
🚀 **aBot - Enhancing moderation and programming productivity for students and developers in Discord servers!**

