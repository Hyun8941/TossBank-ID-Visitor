import time
import requests

def sleepingtime(sec):
  for i in range (1,sec + 1):
    print(f'Waiting {i}/{sec}')
    time.sleep(1)
    if i == sec:
      print("Restarting main()")
      main()

def main():
  count = 0
  while True:
    time.sleep(0.1)
    response = requests.get("https://toss.me/hyun8941")
    if response.status_code == 200:
      count += 1
      print(f"Working Count : {str(count)}")
    else:
      print(f"Error! status code : {response.status_code}")
      sleepingtime(1000)

main()

