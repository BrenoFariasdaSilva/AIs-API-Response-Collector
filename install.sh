#!/bin/bash

# How to Run:
# chmod +x ./install.sh
# ./install.sh

# Function to install gh and Copilot extension for macOS
install_mac() {
	echo "Detected macOS"
	if command -v brew &>/dev/null; then
		echo "Installing GitHub CLI with Homebrew"
		brew install gh
	elif command -v port &>/dev/null; then
		echo "Installing GitHub CLI with MacPorts"
		sudo port install gh
	elif command -v conda &>/dev/null; then
		echo "Installing GitHub CLI with Conda"
		conda install gh --channel conda-forge
	elif command -v spack &>/dev/null; then
		echo "Installing GitHub CLI with Spack"
		spack install gh
	else
		echo "Installing GitHub CLI with Webi"
		curl -sS https://webi.sh/gh | sh
	fi
}

# Function to install gh and Copilot extension for Linux
install_linux() {
	echo "Detected Linux"
	if command -v apt-get &>/dev/null; then
		echo "Installing GitHub CLI with APT"
		sudo apt-get update && sudo apt-get install gh
	elif command -v yum &>/dev/null; then
		echo "Installing GitHub CLI with YUM"
		sudo yum install gh
	elif command -v dnf &>/dev/null; then
		echo "Installing GitHub CLI with DNF"
		sudo dnf install gh
	elif command -v brew &>/dev/null; then
		echo "Installing GitHub CLI with Homebrew"
		brew install gh
	else
		echo "Installing GitHub CLI with Webi"
		curl -sS https://webi.sh/gh | sh
	fi
}

# Function to install gh and Copilot extension for Windows
install_windows() {
	echo "Detected Windows"
	if command -v winget &>/dev/null; then
		echo "Installing GitHub CLI with WinGet"
		winget install --id GitHub.cli
	elif command -v scoop &>/dev/null; then
		echo "Installing GitHub CLI with Scoop"
		scoop install gh
	elif command -v choco &>/dev/null; then
		echo "Installing GitHub CLI with Chocolatey"
		choco install gh
	else
		echo "Installing GitHub CLI with Webi"
		curl -sS https://webi.sh/gh | sh
	fi
}

# Function to install Copilot extension and authenticate
install_copilot_and_auth() {
	echo "Installing GitHub Copilot extension"
	gh extension install github/gh-copilot

	echo "Authenticating with GitHub CLI"
	gh auth login
}

# Function to test Copilot CLI commands
test_copilot_cli() {
	echo "Testing GitHub Copilot CLI..."
	echo "Requesting command explanation for 'sudo apt-get'"
	gh copilot explain "sudo apt-get"

	echo "Requesting command suggestion for 'Undo the last commit'"
	gh copilot suggest "Undo the last commit"
}

# Detect OS and proceed with the installation
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	install_linux
elif [[ "$OSTYPE" == "darwin"* ]]; then
	install_mac
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
	install_windows
else
	echo "Unsupported OS: $OSTYPE"
	exit 1
fi

# Install Copilot extension and authenticate
install_copilot_and_auth

# Test Copilot CLI functionality
test_copilot_cli

echo "Installation and tests complete!"
