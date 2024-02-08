import json

def read_file(filepath):
    with open(filepath, 'rb') as file:
        return file.read()

def extract_route(request):
    return request.split()[1].lstrip('/')

def load_data(filename):
    # Constrói o caminho do arquivo assumindo que ele está na pasta 'data'
    filepath = f"data/{filename}"

    # Abre o arquivo e carrega o conteúdo
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo {filename}. Verifique se é um JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o arquivo {filename}: {e}")

def load_template(filename):
    # Constrói o caminho do arquivo assumindo que ele está na pasta 'templates'
    filepath = f"templates/{filename}"

    try:
        # Abre o arquivo para leitura
        with open(filepath, 'r', encoding='utf-8') as file:
            # Lê o conteúdo do arquivo e o retorna
            return file.read()
    except FileNotFoundError:
        print(f"Arquivo {filepath} não encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo {filepath}: {e}")
        return None