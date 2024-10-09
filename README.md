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
  - [Run Programing Language Code:](#run-programing-language-code)
    - [Dependencies](#dependencies)
    - [Dataset - Optional](#dataset---optional)
  - [Usage](#usage)
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
- Note: The ChatGPT API is a paid service. You will need to subscribe to a pricing plan after generating your API key.

For more details, you can explore the [OpenAI Developer Quickstart](https://platform.openai.com/docs/quickstart).

#### 2. **Gemini (Google)**
To obtain an API key for the Gemini API, follow these steps:

- Visit the [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key) to get a Gemini API key.
- Sign in with your Google account or create one if you don't have one already.
- Navigate to the [Google AI Studio API Key page](https://aistudio.google.com/app/apikey), and with a few clicks, generate your key.
- Gemini is free to use with your Google account. You can start using it right away without any additional cost, making it a good option for developers starting out with AI.

#### 3. **Llama (Meta)**
To access the Llama API, follow these steps:

- Visit the [Llama API website](https://www.llama-api.com) and create an account by signing up.
- Once registered, note that Llama is currently in a private beta. You will be added to the waitlist after signing up.
- After receiving an invitation, log in and navigate to the **API Token** section to generate your token. 

Llama API might have pricing details once you get access, so keep an eye on their [pricing page](https://www.llama-api.com/pricing).
More details on obtaining your token can be found in the [Llama API Documentation](https://docs.llama-api.com/api-token).

#### 4. **Mistral**
To use the Mistral API, follow these steps:

- Visit the [Mistral AI Documentation](https://docs.mistral.ai/docs/getting-started) to learn more about Mistral and its API.
- Sign in or create an account in the [Mistral Console](https://console.mistral.ai/api-keys/) and generate your API key.
- Note: Like ChatGPT, the Mistral API is a paid service. You will need to subscribe to a plan to use the API.

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
* Programing Language:

	* Manually:
		```bash
		# Programing Language:
		sudo apt install program-language -y
		```

  * Using Makefile:
    ```bash
    make install
    ```

  * Using ShellScript:
    ```bash
    chmod +x install.sh
    sudo ./install.sh
    ```  

## Run Programing Language Code:
```bash
# Command here 
```

### Dependencies

1. Install the project dependencies with the following command:

```bash
make dependencies
```

### Dataset - Optional

1. Download the dataset from [WEBSITE-HERE]() and place it in this project directory `(/AIs-API-Response-Collector)` and run the following command:

```bash
make dataset
```

## Usage

In order to run the project, run the following command:

```bash
make run
```

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
