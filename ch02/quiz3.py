wage = 5 # 시급 (1시간에 5달러)
exchange_rate = 1142.16 # 환율 (1달러에 1142.16원)
print("{}시간에 {}달러 벌었습니다".format(1, 1* wage))
print("{}시간에 {}달러 벌었습니다".format(5, 5* wage))
print("{}시간에 {}원 벌었습니다".format(1, 1* wage*exchange_rate))
print("{0}시간에 {1:.2f}원 벌었습니다".format(5, 5* wage*exchange_rate))