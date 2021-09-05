def calculateTotalPrice(articlePrice: int, n=9):
    cgst_sgst = articlePrice * (n/100)
    totalPrice = articlePrice + cgst_sgst
    return totalPrice


print(calculateTotalPrice(105))
