# Analyze-LoRA-Models

## Descrizione

Questo script è progettato per analizzare i modelli LoRA (.safetensors) presenti in una cartella specificata. Lo script carica i modelli, esamina le dimensioni dei parametri e li raggruppa in base alla compatibilità. Genera quindi un report testuale con i dettagli sui modelli compatibili, incluse le loro dimensioni e dimensioni dei file.

## Prerequisiti

- **Python 3.7+**
- **PyTorch**: La versione di PyTorch dipende dal fatto che si disponga o meno di una GPU NVIDIA. Se si dispone di una GPU con supporto CUDA, installare la versione corrispondente di PyTorch; in caso contrario, installare la versione solo CPU.

## Installazione

### 1. Clonare il Repository

Per prima cosa, clonare il repository sulla macchina locale:

```bash
git clone https://github.com/Tranchillo/Analyze-LoRA-Models.git
cd Analyze-LoRA-Models
```

### 2. Creare e Attivare un Ambiente Virtuale

La creazione di un ambiente virtuale aiuta a isolare le dipendenze per il progetto.

Su Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

Su Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installare le Dipendenze

Se si dispone di una GPU NVIDIA con supporto CUDA, installare le dipendenze per CUDA:
```bash
pip install -r requirements_cuda.txt
```

Se si utilizza una CPU (o non si dispone di una GPU NVIDIA con CUDA), installare le dipendenze senza supporto CUDA:
```bash
pip install -r requirements_cpu.txt
```

### 4. Aggiungere i Modelli LoRA

Spostare i modelli LoRA `.safetensors` che si desidera analizzare nella cartella `put_here_your_lora/`.

Percorso: `C:/Analyze-LoRA-Models/put_here_your_lora/`

### 5. Eseguire lo Script

Eseguire lo script per analizzare i modelli LoRA:
```bash
python analyze_lora_models.py
```

### 6. Controllare il Report

Lo script genererà un report chiamato `Lora_Analysis_Report.txt` nella stessa directory. Questo report conterrà i dettagli sui modelli LoRA analizzati, raggruppati per compatibilità.

## Dettagli dello Script

Lo script analizza i modelli LoRA `.safetensors` nella cartella specificata e:

- Filtra i file con estensione `.safetensors`.
- Analizza ogni modello per recuperare parametri e dimensioni.
- Raggruppa i modelli compatibili per dimensione dei parametri.
- Genera un report contenente i modelli compatibili, mostrando la dimensione del file di ciascun modello.

## Licenza

Questo progetto è rilasciato sotto la GNU General Public License v3.0.
