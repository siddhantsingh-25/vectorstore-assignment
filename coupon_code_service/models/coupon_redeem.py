
from pydantic import BaseModel, Field
from typing import Optional

class CouponRedeem(BaseModel):
    coupon_redeem_id: str # Primary key
    coupon_id: str # Foreign Key
    user_id: str #Foreign key
    coupon_application_date: int #Epoch time -  not datatime.  
    
    