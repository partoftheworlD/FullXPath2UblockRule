# FullXPath2UblockRule
The simplest converter from FullXPath to Adblock/Ublock custom rule. More and more sites have started using advertising blocks with random class names, xpath is a great solution to this problem. 


# Example
> ./FullXPath2UblockRule example.com /html/body/div/div[6]/div[5]/div[1]/div/div[8]

And we're getting:

> example.com##html > body > div > div:nth-of-type(6) > div:nth-of-type(5) > div:nth-of-type(1) > div > div:nth-of-type(8)
