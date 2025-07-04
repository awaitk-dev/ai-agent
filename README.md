# ai-agent

## Overview

This project is a toy version of Claude Code, built using Google's free Gemini API. The goal is to demonstrate how you can create a (somewhat) effective custom coding agent with just a few tools and an LLM.

## What Does the Agent Do?

The program is a CLI tool that:

- Accepts a coding task from the user (e.g., "strings aren't splitting in my app, please fix").
- Chooses from a set of predefined functions to work on the task, such as:
  - Scanning the files in a directory
  - Reading a file's contents
  - Overwriting a file's contents
  - Executing the Python interpreter on a file
- Repeats the process of selecting and executing functions until the task is complete (or fails).

## How It Works

The agent uses the Gemini API to interpret user prompts and decide which function(s) to call in order to accomplish the coding task. It maintains context across multiple steps, allowing it to iteratively work towards a solution.

---

**Note:** This project is for educational purposes and is not intended for production use.