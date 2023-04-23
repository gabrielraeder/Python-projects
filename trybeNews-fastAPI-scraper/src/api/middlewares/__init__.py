from fastapi import HTTPException


class Middleware:
    @staticmethod
    def amount(amount):
        if amount == 0:
            raise HTTPException(
                status_code=400, detail="Amount must be greater than zero"
            )
