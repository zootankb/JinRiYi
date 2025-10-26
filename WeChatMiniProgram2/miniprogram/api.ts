// api.ts
const ROOT = "http://192.168.1.2:8000";

function GetFullUrl (extUrl: string) {
  return ROOT + extUrl;
}

module.exports = {
  GetAllProducts: GetFullUrl('/feedback/get_all_products'),
  StartFeedback: GetFullUrl('/feedback/start_feedback/'),
}