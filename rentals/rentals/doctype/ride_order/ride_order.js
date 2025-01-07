// Copyright (c) 2024, praveen and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
        frm.add_custom_button("Accept",()=>{
            frm.set_value("status","Accepted")

            frm.save()
    

	})
}
});
