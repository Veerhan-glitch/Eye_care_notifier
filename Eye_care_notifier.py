#imports
from win10toast import ToastNotifier
import time

while True:
	Toaster = ToastNotifier()
	title = "Take a brake"
	message = "You have been straying at the screen continuously for 20 minutes,take a 20 seconds brake by look at something away from the computer"
	icon_path = "Desktop_Notifier/clock.ico"
	Toaster.show_toast(title, message, icon_path)
	time.sleep(60*20)
