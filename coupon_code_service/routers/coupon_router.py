from fastapi import APIRouter
 
router = APIRouter()

router.post("/validate_coupon")
# returns 200 if coupon is valid else returns 422 status code

router.post("/create_coupon")
# returns 200 if coupon is not present and request is valid, else 5xx

# Not required for PRD
router.post("/update_coupon")

