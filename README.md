# CowChat

CowChat is a Python-based command-line tool that allows users to interact with the ChatGPT API using the whimsical charm of the `cowpy` utility. The tool gives you responses in a fun, cow-themed speech bubble format.

## Features

- Use ChatGPT directly from the command line.
- Display responses using `cowpy` for a fun visual touch.
- Support for incremental response display.
- Configurable model settings with `gpt-3.5-turbo` as the default.
- Flexible API key management via environment variables or `.env` file.
- Additional command-line options for customizing performance and output.

## Requirements

- Python 3.9 or above
- Poetry for dependency management

## Installation

1. **Clone the repository:**
   
   ```sh
   git clone https://github.com/your-username/cowchat.git
   cd cowchat
   ```

2. **Install Poetry (if not already installed):**
   
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   Alternatively, you can install Poetry with Homebrew:
   
   ```sh
   brew install poetry
   ```

3. **Install dependencies:**
   
   ```sh
   poetry install
   ```

4. **Set up your OpenAI API key:**
   - Create a file named `.env` in the project root directory and add your API key:
   
     ```plaintext
     OPENAI_API_KEY=your-api-key-here
     ```

   Alternatively, you can set the environment variable in your shell:
   
   ```sh
   export OPENAI_API_KEY=your-api-key-here
   ```

## Usage

### Basic Usage

Run the program with a prompt:

```sh
poetry run cowchat "Tell me a joke"
```

### Command-line Options

- `prompt`: The user prompt for ChatGPT (positional argument).
- `--model`: Choose the ChatGPT model (default: `gpt-3.5-turbo`). Available options: `gpt-3.5-turbo`, `davinci`, `curie`.
- `--max_tokens`: Max tokens for the ChatGPT response (default: 150).
- `--temperature`: Temperature for chat generation (default: 0.7).
- `--cowfile`: Specify a custom cowpy template.
- `--version`: Display the version of CowChat.

Example with additional options:

```sh
poetry run cowchat "Can you tell me a story?" --model "gpt-3.5-turbo" --max_tokens 100 --temperature 0.9 --cowfile "tux"
```

### Sample Output

```plaintext
 __________________________
< ChatGPT Response Goes Here >
 --------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Hans-Peter Bretz - [bretzhanspeter@gmail.com](mailto:bretzhanspeter@gmail.com)

Follow me on GitHub: [hpbretz](https://github.com/hpbretz)
