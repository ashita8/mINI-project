from win10toast import ToastNotifier
import time

tim= input('enter time in format (H:M:S): ')

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == tim:
        print(current_time)
        break
    else:
        pass



hr = ToastNotifier()
hr.show_toast("alarm", "this is the message")





















































