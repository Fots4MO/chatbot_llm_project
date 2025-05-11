import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

os.environ["TRANSFORMERS_CACHE"] = "./cache/transformers"
os.environ["HF_HOME"] = "./cache/huggingface"

def verificar_dispositivo():
    if torch.cuda.is_available():
        dispositivo = torch.device("cuda")
        props = torch.cuda.get_device_properties(0)
        print(f"✅ GPU disponible: {props.name}, Memoria: {props.total_memory/1e9:.1f} GB")
    else:
        dispositivo = torch.device("cpu")
        print("⚠️ GPU no disponible. Usando CPU.")
    return dispositivo

def cargar_modelo(nombre_modelo="gpt2"):
    tokenizador = AutoTokenizer.from_pretrained(nombre_modelo)
    tokenizador.pad_token = tokenizador.eos_token
    modelo = AutoModelForCausalLM.from_pretrained(
        nombre_modelo,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    modelo.eval()
    return modelo, tokenizador
