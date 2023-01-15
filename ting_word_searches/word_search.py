from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    result = []

    for item in instance._data:
        lines = []
        for index, line in enumerate(item["linhas_do_arquivo"]):
            if word.upper() in line.upper():
                lines.append({"linha": index + 1})
        if (len(lines) > 0):
            result.append({
                    'palavra': word,
                    "arquivo": item["nome_do_arquivo"],
                    "ocorrencias": lines
                })
    return result


def search_by_word(word, instance: Queue):
    result = []

    for item in instance._data:
        lines = []
        for index, line in enumerate(item["linhas_do_arquivo"]):
            if word.upper() in line.upper():
                lines.append({"linha": index + 1, "conteudo": line})
        if (len(lines) > 0):
            result.append({
                    'palavra': word,
                    "arquivo": item["nome_do_arquivo"],
                    "ocorrencias": lines
                })
    return result
