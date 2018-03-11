def NER_map():
	labels = [
		'',
		'PERSON',
		'NORP',
		'FAC',
		'ORG',
		'GPE',
		'LOC',
		'PRODUCT',
		'EVENT',
		'WORK_OF_ART',
		'LAW',
		'LANGUAGE',
		'DATE',
		'TIME',
		'PERCENT',
		'MONEY',
		'QUANTITY',
		'ORDINAL',
		'CARDINAL'
	]
	return {label: i for i, label in enumerate(labels)}

def POS_map():
	labels = [
		'ADJ',
		'ADP',
		'ADV',
		'AUX',
		'CONJ',
		'CCONJ',
		'DET',
		'INTJ',
		'NOUN',
		'NUM',
		'PART',
		'PRON',
		'PROPN',
		'PUNCT',
		'SCONJ',
		'SYM',
		'VERB',
		'X',
		'SPACE'
	]

	return {label: i for i, label in enumerate(labels)}
