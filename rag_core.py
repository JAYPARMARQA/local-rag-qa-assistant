from dataclasses import dataclass
from pathlib import Path
@dataclass
class Chunk: source: str; text: str
def index_documents(folder): return [Chunk(p.name,p.read_text(encoding='utf-8')) for p in Path(folder).glob('*.txt')]
def answer(question,chunks):
    terms=set(question.lower().split()); hit=max(chunks,key=lambda c:len(terms & set(c.text.lower().split())),default=None)
    return f'Source: {hit.source}\n{hit.text}' if hit else 'No supporting source found.'
