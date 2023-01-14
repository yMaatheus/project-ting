from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    for item in instance._data:
        return item["nome_do_arquivo"] == path_file

    text = txt_importer(path_file)
    queue_item = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text,
    }

    print(queue_item)
    instance.enqueue(queue_item)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
