// Copyright (c) 2025, Infintrix Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Daraz Setting', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('Daraz Setting', 'authenticate_seller_center', function(frm) { 
	console.log(frm.doc)
	const REDIRECT_URI = 'https://2478-39-45-161-158.ngrok-free.app/api/method/erpnext_daraz.api.auth.login_daraz'
	const BASE_URL = 'https://api.daraz.pk'
	window.open(`${BASE_URL}/oauth/authorize?response_type=code&force_auth=true&redirect_uri=${REDIRECT_URI}&client_id=${frm.doc.app_id}`, "_blank");

});