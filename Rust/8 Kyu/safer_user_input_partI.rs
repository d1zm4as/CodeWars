
fn html_special_chars(form_data: &str) -> String {
    form_data.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace("\"", "&quot;")
}