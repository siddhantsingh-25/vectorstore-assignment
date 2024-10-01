
from pydantic import BaseModel, Field
from typing import Optional

class Coupon(BaseModel): 
    coupon_id : str = Field() # Primary key - index created on coupon_id
    coupon_code: str # Primary Key - index created on coupon_code
    user_id: str = Field() # Foreign Key - index created on user_id 
    coupon_global_limit: str # Coupon Config limits
    coupon_per_user_limit: int
    coupon_per_hour_limit: int
    coupon_per_day_limit: int
    coupon_per_week_limit: int
    coupon_per_month_limit: int
    coupon_per_year_limit: int
    
    
