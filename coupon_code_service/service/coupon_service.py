def create_coupon_with_config(user_id: str, coupon_code: str, coupon_config: dict):

def update_coupon_with_config(user_id: str, coupon_code: str, coupon_config: dict): 

def validate_coupon(user_id: str, coupon_code: str):
    # fetch the coupon details using coupon_code
    coupon_details = fetch_coupon_details(user_id, coupon_code)
    
    #validate the coupon limits with daily, weekly, hourly, etc limits