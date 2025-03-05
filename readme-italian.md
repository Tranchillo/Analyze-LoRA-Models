# Analyze-LoRA-Models

## Descrizione

Questo script è progettato per analizzare i modelli LoRA (`.safetensors`) situati in una cartella specificata. Lo script carica i modelli, esamina le dimensioni dei parametri e li raggruppa in base alla compatibilità. Successivamente, genera un report testuale con dettagli sui modelli compatibili, incluse le loro dimensioni e dimensioni del file.

## Prerequisiti

- **Python 3.7+**
- **PyTorch**: La versione di PyTorch dipende dal fatto che tu abbia o meno una GPU NVIDIA. Se hai una GPU con supporto CUDA, installa la versione corrispondente di PyTorch; in caso contrario, installa la versione per CPU.

## Installazione

### 1. Clonare il Repository

Per prima cosa, clona il repository sul tuo computer locale:

```bash
git clone https://github.com/Tranchillo/Analyze-LoRA-Models.git
cd Analyze-LoRA-Models
```

### 2. Creare e Attivare un Ambiente Virtuale

Creare un ambiente virtuale aiuta a isolare le dipendenze del progetto.

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

Se hai una GPU NVIDIA con supporto CUDA, installa le dipendenze per CUDA:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements_cuda.txt
```

Se utilizzi solo la CPU (o non hai una GPU NVIDIA con CUDA), installa le dipendenze senza supporto CUDA:
```bash
pip install -r requirements_cpu.txt
```

### 4. Aggiungere i Modelli LoRA

Sposta i modelli LoRA `.safetensors` che vuoi analizzare nella cartella `put_here_your_lora/`.

Percorso: `put_here_your_lora/` (all'interno della directory dello script)

### 5. Eseguire lo Script

Esegui lo script per analizzare i modelli LoRA:
```bash
python analyze_lora_models.py
```

### 6. Controllare il Report

Lo script genererà un report chiamato `Lora_Analysis_Report.txt` nella stessa directory. Questo report conterrà dettagli sui modelli LoRA analizzati, raggruppati per compatibilità.

## Dettagli dello Script

Lo script analizza i modelli LoRA `.safetensors` nella cartella specificata ed esegue le seguenti operazioni:

- Filtra i file con estensione `.safetensors`.
- Verifica che la directory di destinazione esista.
- Analizza ciascun modello per ottenere parametri e dimensioni.
- Raggruppa i modelli compatibili in base alla stessa dimensione dei parametri.
- Genera un report contenente i modelli compatibili, indicando la dimensione di ciascun file.

## Licenza

Questo progetto è concesso in licenza sotto la GNU General Public License v3.0.
