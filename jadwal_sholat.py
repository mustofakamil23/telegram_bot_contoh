import pandas as pd
import requests
import urllib3

urllib3.disable_warnings()


def jadwal_sholat() -> str:
      url = "https://www.google.com/search?q=jadwal+sholat&oq=jadwal+sholat&aqs" \
            "=edge..69i57j0i402l2j0i131i433j0i512j0i433i512j0i131i433l2j69i64.3292j0j4&sourceid=chrome&ie=UTF-8"

      s = requests.get(url, verify=False).content
      df = pd.read_html(s)
      df = df[0]
      df = df.set_index(df[0])
      jadwal = df[1].to_dict()

      text = ""
      for k, v in jadwal.items():
            text = text + f"{k} : {v}" + "\n"
      return text.replace(": nan", "")

