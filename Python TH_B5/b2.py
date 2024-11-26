import datetime as dt

# Định dạng chuỗi thời gian
format = '%Y-%m-%dT%H:%M:%S'

# Chuyển đổi chuỗi thời gian thành đối tượng datetime
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# In ra ngày, tháng, phút và giây
print('Day ' + str(t1.day))
print('Month ' + str(t1.month))
print('Minute ' + str(t1.minute))
print('Second ' + str(t1.second))

# Xác định ngày và thời gian hiện tại
t2 = dt.datetime.now()

# Tính khoảng thời gian khác biệt
diff = t2 - t1

# In ra số ngày khác biệt
print('How many days difference? ' + str(diff.days))
