import requests

resp = requests.get(
    "https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+%28%22Chief+Product+Officer%22%29+%28%22United+States%22%29+%28%22Automotive%22%29&sca_esv=c5f02fd2b2be415a&sxsrf=ACQVn0-34X-ugeniEQUP9_2eAdrC7zg8FA%3A1709610395290&ei=m5XmZaC0EYTdptQP0biH0AM&ved=0ahUKEwjg7cKCm9yEAxWErokEHVHcAToQ4dUDCBA&uact=5&oq=site%3Alinkedin.com%2Fin%2F+%28%22Chief+Product+Officer%22%29+%28%22United+States%22%29+%28%22Automotive%22%29&gs_lp=Egxnd3Mtd2l6LXNlcnAiUHNpdGU6bGlua2VkaW4uY29tL2luLyAoIkNoaWVmIFByb2R1Y3QgT2ZmaWNlciIpICgiVW5pdGVkIFN0YXRlcyIpICgiQXV0b21vdGl2ZSIpSABQAFgAcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAKAHAA&sclient=gws-wiz-serp"
)

print(resp.text)
