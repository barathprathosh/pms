# Copyright (c) 2021, Barath Prathosh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StockEntry(Document):
	def on_submit(self):
		for child_t in self.stock_detail:
			product_list = frappe.get_doc("Product List",child_t.product_name)
			total = child_t.sku + child_t.qty
			product_list.sku = total
			product_list.save(ignore_permissions=True)
			frappe.db.commit()
	
	def on_cancel(self):
		for child_t in self.stock_detail:
			product_list = frappe.get_doc("Product List",child_t.product_name)
			total = product_list.sku - child_t.qty
			product_list.sku = total
			product_list.save(ignore_permissions=True)
			frappe.db.commit()