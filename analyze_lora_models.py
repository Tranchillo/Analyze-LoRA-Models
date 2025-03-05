import os
import torch
import safetensors.torch
from datetime import datetime

# Imposta la directory relativa in cui cercare i modelli LoRA
script_directory = os.path.dirname(os.path.abspath(__file__))
lora_directory = os.path.join(script_directory, "put_here_your_lora")

def analyze_lora_models(directory):
    # Verifica che la directory esista
    if not os.path.exists(directory):
        print(f"Errore: La directory '{directory}' non esiste.")
        return
    
    # Filtra i file con estensione .safetensors
    lora_files = [f for f in os.listdir(directory) if f.endswith(".safetensors")]
    
    if not lora_files:
        print("Nessun file .safetensors trovato nella directory specificata.")
        return
    
    grouped_models = {}
    
    report_path = os.path.join(script_directory, "Lora_Analysis_Report.txt")
    with open(report_path, "w") as report_file:
        report_file.write("Raggruppamento dei modelli LoRA compatibili per parametri e dimensioni:\n\n")
        
        for lora_file in lora_files:
            file_path = os.path.join(directory, lora_file)
            
            try:
                state_dict = safetensors.torch.load_file(file_path)
                model_signature = None
                for key, param in state_dict.items():
                    if param.shape != torch.Size([]):
                        model_signature = (key, param.shape)
                        break
                
                if model_signature is None:
                    report_file.write(f"Nessun parametro valido trovato nel modello {lora_file}.\n")
                    continue
                
                file_size_kb = os.path.getsize(file_path) / 1024
                
                if model_signature not in grouped_models:
                    grouped_models[model_signature] = []
                grouped_models[model_signature].append((lora_file, file_size_kb))
            
            except Exception as e:
                report_file.write(f"Errore nel caricamento del modello {lora_file}: {e}\n")
        
        for model_signature, models in grouped_models.items():
            if len(models) > 1:
                report_file.write(f"\nGruppo (dimensione maggiore {model_signature[1]}):\n")
                for model, size_kb in models:
                    report_file.write(f" - {model} ({size_kb:.2f} KB)\n")
        
        report_file.write("\n\n---\n")
        report_file.write(f"Autore: Dany Tranchillo\n")
        report_file.write(f"Contributori: barracuda415, reditor_13\n")
        report_file.write(f"Report generato il: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"Report generato: {report_path}")

# Esegui l'analisi
analyze_lora_models(lora_directory)
