README.md


Assumptions - 
Assuming that coupon codes are unique. There is no nested layer where same coupon code with different scope for users are to be impplemented. Keeping that out of scope for the current implementation

Requirements: 
2 APIs

- Injest API -> INPUT(Coupon Config) - > POST API 
- validate coupon API -> INPUT(user_id, coupon_id)-> 200/422 status code


LLD:

Router

Controllers

Service

DAO 

DB_Utils


Class: 
- Coupon
- CouponRedeem

