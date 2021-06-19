// Copyright (c) 2021, Barath Prathosh and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product List', {
	// refresh: function(frm) {

	// },
	quantity(frm){
		frm.set_value("sku",frm.doc.quantity)
	}
});
