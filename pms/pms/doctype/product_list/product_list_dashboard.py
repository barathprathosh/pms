from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'product_name',
		'transactions': [
			{
				'label': _('Stock'),
				'items': ['Stock Entry']
			},
		]
	}
