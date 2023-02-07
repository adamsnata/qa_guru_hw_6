from os import path
from pathlib import Path

import qa_guru_hw_6


def project():
    return Path(qa_guru_hw_6.__file__).parent.parent

def resources():
    return  path.join(project(), 'resources')

def tmp():
    return path.join(project(), 'tmp')
