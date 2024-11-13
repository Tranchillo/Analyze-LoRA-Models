# Analyze LoRA Models 

## Description
With the `analyze_lora_models.py` script, you can automatically organize and group your LoRA models based on compatibility, reducing the time spent manually selecting the right models for each project.

Thanks to this script, you'll be able to:

- Speed up the search for LoRA models by organizing them into compatible groups, saving time in selection from hundreds of files.
- The generated report will allow you to quickly identify groups of compatible models. Each group will be assigned a simple identifying name, helping you recognize them easily and merge LoRA models quickly, optimizing your workflow without having to concatenate multiple separate models.
- Create a more organized and faster workflow, allowing you to spend more time creating your works while saving disk space.
- No longer waste time searching through your LoRA models. With `analyze_lora_models.py`, simplify and speed up your creative process, reducing both disk space usage and search time!

### Why I Created This Script
As a beginner in this field, I often struggled to find tools that would generate the report I needed. Instead of spending time searching for such a tool, I decided to create it myself. I hope this tool can be useful for others in the creative community.

If you find this tool useful, feel free to share it and give it a thumbs-up!

## Script Purpose
This script was created to optimize and simplify the management of LoRA models used in workflows. Its main functions are:

- Reducing the number of LoRA models to concatenate into a single workflow by identifying compatible models and allowing easier merging.
- Significantly reducing disk space usage by grouping LoRA models that share similar parameters, thus avoiding the need to store multiple copies of compatible models separately.
- Organizing LoRA models by creating groups based on parameter size and type, simplifying their selection and use in the future.

## What the Script Does
The script explores a specified folder, examines each LoRA model within the directory, and determines which models are compatible with each other based on parameter dimensions (such as `lora_up.weight` and `lora_down.weight`).

For each LoRA model found, the script:
- Loads the model.
- Identifies the most significant parameter (the largest dimension of the main parameter).
- Groups compatible LoRA models together, reducing the risk of duplication.
- Generates a `.txt` report listing compatible model groups so that the user can easily view which models can be merged together.

## How to Run the Script

### 1. Clone the Repository and Install Requirements
To ensure compatibility, clone the repository into `C:/` on your computer and install the required dependencies.

1. Open a terminal (CMD or PowerShell on Windows).
2. Execute the following commands:

   ```bash
   git clone https://github.com/Tranchillo/Analyze-LoRA-Models.git C:/Analyze-LoRA-Models
   cd C:/Analyze-LoRA-Models
   pip install -r requirements.txt
   ```

This will create the Analyze-LoRA-Models folder in C:/ and install all necessary dependencies.

### 2. Modify Script Directory (Optional)
By default, the script will analyze LoRA models in the default directory. If you want to analyze models in a different location:

1. Open the Python script and locate the `lora_directory` variable
2. Change the path to your desired location. For example:
   ```python
   lora_directory = "C:/Users/username/Documents/LoraModels/"
   ```
Make sure the specified folder contains only the .safetensors files for the LoRA models you want to analyze.

### 3. Place LoRA Files
Add all the .safetensors LoRA files you want to analyze into your chosen folder (either the default folder or your custom folder specified in step 2).

### 4. Run the Script
Open a terminal (CMD or PowerShell on Windows), navigate to the C:/Analyze-LoRA-Models folder where the Python script is located, and run the following command:

   ```bash
   python analyze_lora_models.py
   ```

### 5. View the Report
The script will generate a report file called Lora_Analysis_Report.txt in the same folder as the script. This file will contain the groups of compatible LoRA models, sorted by the main parameter dimension.

## Conclusion
This script provides an efficient way to organize and reduce the overall size of LoRA files, making them easier to use in more complex workflows. By grouping compatible models, it helps avoid duplication and improves the management of models over time.
