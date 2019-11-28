password = 'a123456'
error = 3 # 有三次機會
while error > 0:
    guess = input('請輸入密碼： ')
    error = error - 1 # 機會少一次
    if guess == password:
        print('登入成功')
        break
    elif error >= 1:
        print('密碼錯誤! 還有',error,'次機會')
    else:
        print('你的帳號被鎖了')
        print('剩餘可嘗試次數:',error)
        
        
        
    
        
