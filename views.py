from utils import load_data, load_template, add_note_to_json, build_response
from urllib.parse import unquote_plus

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        partes = request.split('\n\n')  # Separa cabeçalho e corpo
        corpo = partes[1]
        params = {}

        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[chave] = unquote_plus(valor)

        # Adiciona a nova anotação ao arquivo JSON
        add_note_to_json(params['titulo'], params['detalhes'])

        # Retorna uma resposta de redirecionamento para requisições POST
        return build_response(code=303, reason='See Other', headers='Location: /')

    # Processamento para requisições GET ou após processar o POST
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    # Retorna a página principal para requisições GET
    body = load_template('index.html').format(notes=notes)
    return build_response(body)


