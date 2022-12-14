import json
import yaml


def pars(file_path):
    '''File parser. Returs python format from json or yaml format'''
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    if file_path.endswith('.yml') or file_path.endswith('.yaml'):
        return yaml.safe_load(open(file_path))
