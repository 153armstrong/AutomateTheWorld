## Requires the installation of xaut ( http://xautomation.sourceforge.net )

import xaut 
from time import sleep
k = xaut.keyboard()

## Move from the terminal to the gmail login page using alt+tab
k.type("!{Tab}")

## Type in your email id and press enter 
k.type("enter you gmail id here")
k.type("{Return}")

## Wait for the password page to open
sleep(1)

## Type in your password and vroom.. 
k.type("enter your password")
k.type("{Return}")

## If you have two step verifcation enabled, then you might arrive at that page.
