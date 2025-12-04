// api.ts
// const ROOT = "http://www.jinriyi.top";
const ROOT = "http://192.168.1.6:8000";

function GetFullUrl (extUrl: string) {
  return ROOT + extUrl;
}

module.exports = {
  GetMainData: GetFullUrl('/get_main_data/'),
  GetAllProducts: GetFullUrl('/get_all_products/'),
  StartFeedback: GetFullUrl('/start_feedback/'),
  GetVersionCode: GetFullUrl('/get_verification_code/'),
  CheckVerificationValid: GetFullUrl('/check_verification_valid/'),
}

interface ProjData {
  img_url: string,
  title: string,
  sale_info: string,
  praise_info: string,
  tag_info: string,
  ori_price: number,
  exp_price: number,
  vip_price: number,
  buy_url: string
}

interface TypeProjData {
  product_type: number,
  product_type_name: string,
  detail_items: ProjData[]
}

interface MainData {
  swiper_data: string[];
  product_items: TypeProjData[];
}