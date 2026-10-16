from pathlib import Path
from rag_core import answer,index_documents
Path('documents').mkdir(exist_ok=True);Path('documents/refund-policy.txt').write_text('Refunds are accepted within 30 calendar days.',encoding='utf-8')
result=answer('What is refund policy?',index_documents('documents'));assert '30 calendar days' in result and 'refund-policy.txt' in result;print('PASS: grounded retrieval returned a cited answer')
