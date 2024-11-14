import os
import torch
import safetensors.torch
from datetime import datetime

# Directory path containing LoRA models
lora_directory = "C:/Analyze-LoRA-Models/put_here_your_lora/"

def analyze_lora_models(directory):
    # Filter the .safetensors files in the directory
    lora_files = [f for f in os.listdir(directory) if f.endswith(".safetensors")]
    
    # Check if the directory contains LoRA files
    if not lora_files:
        print("No .safetensors files found in the specified directory.")
        return

    # Dictionary to group LoRA models by parameter and dimension
    grouped_models = {}

    # Open a log file for the report
    with open("Lora_Analysis_Report.txt", "w") as report_file:
        report_file.write("Grouping compatible LoRA models by parameter and dimension:\n\n")
        
        # Analyze each LoRA file
        for lora_file in lora_files:
            file_path = os.path.join(directory, lora_file)
            
            try:
                # Load the LoRA model using safetensors
                state_dict = safetensors.torch.load_file(file_path)
                
                # Find the first parameter with a non-empty dimension
                model_signature = None
                for key, param in state_dict.items():
                    if param.shape != torch.Size([]):  # Take the first parameter with a valid dimension
                        model_signature = (key, param.shape)
                        break
                
                if model_signature is None:
                    report_file.write(f"No valid parameter found in LoRA model {lora_file}.\n")
                    continue
                
                # Get the file size in KB
                file_size_kb = os.path.getsize(file_path) / 1024
                
                # Group LoRA models by parameter dimension signature
                if model_signature not in grouped_models:
                    grouped_models[model_signature] = []
                grouped_models[model_signature].append((lora_file, file_size_kb))
                
            except Exception as e:
                report_file.write(f"Error loading LoRA model {lora_file}: {e}\n")
        
        # Add the groups of compatible LoRA models to the report
        for model_signature, models in grouped_models.items():
            if len(models) > 1:  # Only show groups with more than one model (compatible)
                report_file.write(f"\nGroup (largest dimension {model_signature[1]}):\n")
                for model, size_kb in models:
                    report_file.write(f" - {model} ({size_kb:.2f} KB)\n")

        # Add the author and contributor info at the end of the report
        report_file.write("\n\n---\n")
        report_file.write(f"Author: Dany Tranchillo\n")
        report_file.write(f"Contributors: barracuda415, reditor_13\n")
        report_file.write(f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        print("Report generated as 'Lora_Analysis_Report.txt'")

# Run the analysis function
analyze_lora_models(lora_directory)
