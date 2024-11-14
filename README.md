
# Analyze-LoRA-Models

## Description

This script is designed to analyze LoRA models (.safetensors) located in a specified folder. The script loads the models, examines the parameter dimensions, and groups them based on compatibility. It then generates a text report with details about the compatible models, including their dimensions and file sizes.

## Prerequisites

- **Python 3.7+**
- **PyTorch**: The version of PyTorch depends on whether or not you have an NVIDIA GPU. If you have a GPU with CUDA support, install the corresponding version of PyTorch; otherwise, install the CPU-only version.

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Tranchillo/Analyze-LoRA-Models.git
cd Analyze-LoRA-Models
```

### 2. Create and Activate a Virtual Environment

Creating a virtual environment helps isolate dependencies for the project.

On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

On Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

If you have an NVIDIA GPU with CUDA support, install the dependencies for CUDA:
```bash
pip install -r requirements_cuda.txt
```

If you're using a CPU (or do not have an NVIDIA GPU with CUDA), install dependencies without CUDA support:
```bash
pip install -r requirements_cpu.txt
```

### 4. Add LoRA Models

Move the LoRA `.safetensors` models you want to analyze into the `put_here_your_lora/` folder.

Path: `C:/Analyze-LoRA-Models/put_here_your_lora/`

### 5. Run the Script

Execute the script to analyze the LoRA models:
```bash
python analyze_lora_models.py
```

### 6. Check the Report

The script will generate a report called `Lora_Analysis_Report.txt` in the same directory. This report will contain details about the analyzed LoRA models, grouped by compatibility.

## Script Details

The script analyzes `.safetensors` LoRA models in the specified folder and:

- Filters files with the `.safetensors` extension.
- Analyzes each model to retrieve parameters and dimensions.
- Groups compatible models by the same parameter dimension.
- Generates a report containing compatible models, showing the file size of each model.

## License

This project is licensed under the GNU General Public License v3.0.
