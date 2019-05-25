import requests
import jmespath


def main():

    try:
        r=requests.get("http://127.0.0.1:5000?output=json")
    except requests.exception.RequestException as e:
        print(e)
        exit(1)
    if r.status_code !=200:
        print("FAILED: wywolanie nie powiodlo sie:" +r.text)
        exit(2)
    print(r.text)
    print(r.json())

    def checkOutput(rj):
        actual = jmespath.search('imie',rj)
        expected="Stefan"
        if actual !=expected:
            print("FAILED: We expected: " +expected + "but was" +actual)

if __name__ == "__main__":

    main()
