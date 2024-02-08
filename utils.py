import json

def read_file(filepath):
    with open(filepath, 'rb') as file:
        return file.read()

def extract_route(request):
    # Divide a requisição em linhas
    lines = request.split('\n')
    
    # Pega a primeira linha (linha de requisição)
    request_line = lines[0]
    
    # Divide a linha de requisição em espaços e pega a rota
    route = request_line.split(' ')[1]
    
    # Remove o primeiro caractere (/) da rota
    return route[1:]

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
    
def add_note_to_json(title, details, filename='notes.json'):
    try:
        # Carrega as notas existentes
        with open(filename, 'r', encoding='utf-8') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    # Adiciona a nova nota
    notes.append({'titulo': title, 'detalhes': details})

    # Salva as notas de volta no arquivo JSON
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(notes, file, indent=4)