<div align="center">
  
# [AIs-API-Response-Collector.](https://github.com/BrenoFariasdaSilva/AIs-API-Response-Collector) <img src="https://github.com/BrenoFariasdaSilva/AIs-API-Response-Collector/blob/main/.assets/Icon/AI.svg"  width="4%" height="4%">

</div>

<div align="center">
  
---

This tool, developed in Python, interacts seamlessly with various AI APIs, including OpenAI's GPT-3.5, Google's PaLM, and Cohere's language models. Users can submit requests and retrieve responses for the same input, with collected responses organized and stored in a CSV file for easy comparison and analysis. The tool computes similarities based on the expected outputs of the AIs, enabling users to evaluate the performance of different models efficiently. With a focus on usability, this automated solution streamlines the process of performance assessment across multiple AI platforms.

The project aims to facilitate in-depth analysis and comparison of AI models, making it an essential resource for researchers, developers, and enthusiasts in the field of Artificial Intelligence.

---

</div>

<div align="center">

![GitHub Code Size in Bytes](https://img.shields.io/github/languages/code-size/BrenoFariasdaSilva/AIs-API-Response-Collector)
![GitHub Commits](https://img.shields.io/github/commit-activity/t/BrenoFariasDaSilva/AIs-API-Response-Collector/main)
![GitHub Last Commit](https://img.shields.io/github/last-commit/BrenoFariasdaSilva/AIs-API-Response-Collector)
![GitHub Forks](https://img.shields.io/github/forks/BrenoFariasDaSilva/AIs-API-Response-Collector)
![GitHub Language Count](https://img.shields.io/github/languages/count/BrenoFariasDaSilva/AIs-API-Response-Collector)
![GitHub License](https://img.shields.io/github/license/BrenoFariasdaSilva/AIs-API-Response-Collector)
![GitHub Stars](https://img.shields.io/github/stars/BrenoFariasdaSilva/AIs-API-Response-Collector)
![wakatime](https://wakatime.com/badge/github/BrenoFariasdaSilva/AIs-API-Response-Collector.svg)

</div>

<div align="center">
  
![RepoBeats Statistics](https://repobeats.axiom.co/api/embed/c3dc0781c48b858aa67277de5761edef5014aeb3.svg "Repobeats analytics image")

</div>

## Table of Contents
- [AIs-API-Response-Collector. ](#ais-api-response-collector-)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
    - [Clone the repository](#clone-the-repository)
    - [Generate API Key](#generate-api-key)
      - [1. **ChatGPT (OpenAI)**](#1-chatgpt-openai)
      - [2. **Gemini (Google)**](#2-gemini-google)
      - [3. **Llama (Meta)**](#3-llama-meta)
      - [4. **Mistral**](#4-mistral)
    - [Setting Up the `.env` File](#setting-up-the-env-file)
      - [1. Fill in the API Keys](#1-fill-in-the-api-keys)
      - [2. Rename the File](#2-rename-the-file)
  - [Installation:](#installation)
    - [Python and Pip](#python-and-pip)
      - [Linux](#linux)
      - [MacOS](#macos)
      - [Windows](#windows)
    - [Dependencies](#dependencies)
  - [Usage](#usage)
    - [Input Prompts/Texts](#input-promptstexts)
      - [Task Column](#task-column)
      - [Expected Output (Optional) Column](#expected-output-optional-column)
      - [Example of `input.csv`:](#example-of-inputcsv)
      - [Notes:](#notes)
  - [Results - Optional](#results---optional)
  - [Contributing](#contributing)
  - [Collaborators](#collaborators)
  - [License](#license)
    - [Apache License 2.0](#apache-license-20)

## Setup

### Clone the repository

1. Clone the repository with the following command:

```bash
git clone https://github.com/BrenoFariasDaSilva/AIs-API-Response-Collector.git
cd AIs-API-Response-Collector
```

### Generate API Key

To interact with the various AI models supported by this tool, you will need to generate API keys for each respective service. Below are the steps to obtain API keys for ChatGPT, Gemini, Llama, and Mistral.

#### 1. **ChatGPT (OpenAI)**
To access the ChatGPT API, follow these steps:

- Visit the [OpenAI Platform](https://platform.openai.com/docs/quickstart) and sign up or log in to your account.
- The ChatGPT API allows you to integrate AI capabilities into your applications, enabling natural language processing, semantic search, and more.
- Generate an API key in the OpenAI dashboard by going to [API Keys](https://platform.openai.com/api-keys).

For more details, you can explore the [OpenAI Developer Quickstart](https://platform.openai.com/docs/quickstart).

#### 2. **Gemini (Google)**
To obtain an API key for the Gemini API, follow these steps:

- Visit the [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key) to get a Gemini API key.
- Sign in with your Google account or create one if you don't have one already.
- Navigate to the [Google AI Studio API Key page](https://aistudio.google.com/app/apikey), and with a few clicks, generate your key.

#### 3. **Llama (Meta)**
To access the Llama API, follow these steps:

- Visit the [Llama API website](https://www.llama-api.com) and create an account by signing up.
- Once registered, note that Llama is currently in a private beta. You will be added to the waitlist after signing up.
- After receiving an invitation, log in and navigate to the **API Token** section to generate your token. 

More details on obtaining your token can be found in the [Llama API Documentation](https://docs.llama-api.com/api-token).

#### 4. **Mistral**
To use the Mistral API, follow these steps:

- Visit the [Mistral AI Documentation](https://docs.mistral.ai/docs/getting-started) to learn more about Mistral and its API.
- Sign in or create an account in the [Mistral Console](https://console.mistral.ai/api-keys/) and generate your API key.

For more information, refer to the [Mistral Getting Started Guide](https://docs.mistral.ai/docs/getting-started).

### Setting Up the `.env` File

To ensure the tool can properly authenticate with each AI API, you will need to provide your API keys in a `.env` file. Follow these steps to configure it:

#### 1. Fill in the API Keys
- Open the `.env_example` file in the root directory of the project.
- Replace the placeholder values with your actual API keys, which you should have obtained by following the instructions for each respective AI service.

Here’s what the `.env_example` file looks like:

```plaintext
CHATGPT_API_KEY=
GEMINI_API_KEY=
LLAMA_API_KEY=
MISTRAL_API_KEY=
```


#### 2. Rename the File
- After filling in the keys, rename the file from `.env_example` to `.env`.

You can do this using the command line:

```bash
mv .env_example .env
```

Now the tool will automatically load the API keys from your `.env` file when making requests to the respective AI models. Make sure the `.env` file is not shared publicly to keep your API keys secure.

## Installation:

In order to run the project, you must have Python and Pip installed in your machine. In this section, you will learn how to install Python and Pip in your machine.

### Python and Pip

In order to run the scripts, you must have python3 and pip installed in your machine. If you don't have it installed, you can use the following commands to install it:

#### Linux

In order to install python3 and pip in Linux, you can use the following commands:

```
sudo apt install python3 -y
sudo apt install python3-pip -y
```

#### MacOS

In order to install python3 and pip in MacOS, you can use the following commands:

```
brew install python3
```

#### Windows

In order to install python3 and pip in Windows, you can use the following commands in case you have `choco` installed:

```
choco install python3
```

Or just download the installer from the [official website](https://www.python.org/downloads/).

Great, you now have python3 and pip installed. Now, we need to install the project requirements/dependencies.

### Dependencies

This project depends on the following libraries:

- [Google.generativeai](https://pypi.org/project/google.generativeai/) -> Google Generative AI is used to interact with the Google API.
- [Mistralai](https://pypi.org/project/mistralai/) -> Mistral AI is used to interact with the Mistral API.
- [NumPy](https://numpy.org/) -> NumPy is used to generate the linear prediction of the linear regression and to many operations in the list of the metrics.
- [Openai](https://pypi.org/project/openai/) -> OpenAI is used to interact with the OpenAI API.
- [Pandas](https://pandas.pydata.org/) -> Pandas is used mainly to read and write the csv files.
- [SciKit-Learn](https://scikit-learn.org/stable/) -> SciKit-Learn is used to generate the linear prediction of the linear regression.

1. Install the project dependencies with the following command:

```bash
make dependencies
```

This command will generate virtual environment and install all the dependencies needed to run the project in the virtual environment.

## Usage

In this section, you will learn how to use the project. The project is a tool that interacts with various AI APIs, including OpenAI's GPT-3.5, Google's PaLM, and Cohere's language models. Users can submit requests and retrieve responses for the same input, with collected responses organized and stored in a CSV file for easy comparison and analysis. The tool computes similarities based on the expected outputs of the AIs, enabling users to evaluate the performance of different models efficiently. With a focus on usability, this automated solution streamlines the process of performance assessment across multiple AI platforms.

### Input Prompts/Texts

To set up the input for this project, you need to populate the `Inputs/input.csv` file. This file will contain the tasks or text prompts that the AI models will process and, optionally, the expected output for each task. The comparison between the models' outputs and the expected results will be based on these entries. Follow the steps below to properly configure the input file:

1. Navigate to the `Inputs` directory in the project folder.
2. Open the `input.csv` file.
3. Ensure that the file has the following header:
   ```
   Task,Expected Output (Optional)
   ```

#### Task Column
- This column is mandatory and should contain the task or input text you want to provide to the AI models and must be surrounded by double quotes, in order to avoid any issues with the commas that break the csv file.
- Each line represents a separate task for evaluation.
- Examples of tasks might include questions, statements, or instructions for the models to interpret and respond to.

#### Expected Output (Optional) Column
- This column is optional and should contain the expected output you anticipate from the AI models for the corresponding task and must be surrounded by double quotes, in order to avoid any issues with the commas that break the csv file.
- If provided, the model's output will be compared to this expected result, and a similarity score will be computed.
- Leaving this column blank will disable the comparison for that specific task.

#### Example of `input.csv`:
```csv
Task,Expected Output (Optional)
"Explain the 'sudo' command in Linux.","The 'sudo' command in Linux allows a permitted user to execute a command as the superuser or another user, as specified by the security policy."
"Explain the 'chmod' command in Linux.","The 'chmod' command in Linux changes the permissions of a file or directory."
```

#### Notes:
- Make sure each task is clear and concise to ensure the AI models can generate appropriate responses.
- If you want to test model outputs without expecting a specific result, you can leave the "Expected Output (Optional)" column blank. The system will still process the task but won't perform any comparisons.
- You can add as many tasks as needed, with or without expected outputs, to the `input.csv` file. The system will automatically process each task in the file.

After setting up the input file and the API keys, you must open the `main.py` file and modify a few constants in order to customize the project to your needs. The constants that you can modify are:
```python
EXECUTE_MODELS = {"ChatGPT": "ChatGPTModel", "Copilot": "CopilotModel", "Gemini": "GeminiModel", "Llama": "LlamaModel", "Mistral": "MistralModel"}
```

The `EXECUTE_MODELS` constant is a dictionary that contains the name of the model and the name of the class that will be executed. You can remove models from this dictionary if you don't want to execute them or if you simply don't have the API key for them. In order to add a new model, you must create a new class using the `template.py` file as a template and implement the new model's logic. After that, you can get the model's name and the class name and add them to the `EXECUTE_MODELS` dictionary.

Lastly, open the `utils.py` file and modify the `VERBOSE` constant to true if you want the program to output everything that is being done. I personally never set it to true, only for debugging purposes.

Finally, as you have set up the input file, the API keys, and the constants in the `main.py` file, you can run the project.
In order to run the project, run the following command:

```bash
make
```

This command will always ensure that the virtual env and the dependencies are installed and then run the project.

## Results - Optional

Discuss the results obtained in the project.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. If you have suggestions for improving the code, your insights will be highly welcome.
In order to contribute to this project, please follow the guidelines below or read the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on how to contribute to this project, as it contains information about the commit standards and the entire pull request process.
Please follow these guidelines to make your contributions smooth and effective:

1. **Set Up Your Environment**: Ensure you've followed the setup instructions in the [Setup](#setup) section to prepare your development environment.

2. **Make Your Changes**:
   - **Create a Branch**: `git checkout -b feature/YourFeatureName`
   - **Implement Your Changes**: Make sure to test your changes thoroughly.
   - **Commit Your Changes**: Use clear commit messages, for example:
     - For new features: `git commit -m "FEAT: Add some AmazingFeature"`
     - For bug fixes: `git commit -m "FIX: Resolve Issue #123"`
     - For documentation: `git commit -m "DOCS: Update README with new instructions"`
     - For refactorings: `git commit -m "REFACTOR: Enhance component for better aspect"`
     - For snapshots: `git commit -m "SNAPSHOT: Temporary commit to save the current state for later reference"`
   - See more about crafting commit messages in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

3. **Submit Your Contribution**:
   - **Push Your Changes**: `git push origin feature/YourFeatureName`
   - **Open a Pull Request (PR)**: Navigate to the repository on GitHub and open a PR with a detailed description of your changes.

4. **Stay Engaged**: Respond to any feedback from the project maintainers and make necessary adjustments to your PR.

5. **Celebrate**: Once your PR is merged, celebrate your contribution to the project!

## Collaborators

We thank the following people who contributed to this project:

<table>
  <tr>
    <td align="center">
      <a href="#" title="defina o titulo do link">
        <img src="https://github.com/BrenoFariasdaSilva/AIs-API-Response-Collector/blob/main/.assets/Images/Github.svg" width="100px;" alt="My Profile Picture"/><br>
        <sub>
          <b>Breno Farias da Silva</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o titulo do link">
        <img src="https://github.com/BrenoFariasdaSilva/AIs-API-Response-Collector/blob/main/.assets/Images/Github.svg" width="100px;" alt="My Profile Picture"/><br>
        <sub>
          <b>Breno Farias da Silva</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o titulo do link">
        <img src="https://github.com/BrenoFariasdaSilva/AIs-API-Response-Collector/blob/main/.assets/Images/Github.svg" width="100px;" alt="My Profile Picture"/><br>
        <sub>
          <b>Breno Farias da Silva</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## License

### Apache License 2.0

This project is licensed under the [Apache License 2.0](LICENSE). This license permits use, modification, distribution, and sublicense of the code for both private and commercial purposes, provided that the original copyright notice and a disclaimer of warranty are included in all copies or substantial portions of the software. It also requires a clear attribution back to the original author(s) of the repository. For more details, see the [LICENSE](LICENSE) file in this repository.
