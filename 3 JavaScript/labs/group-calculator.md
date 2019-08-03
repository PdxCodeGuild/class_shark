
# Lab: Calculator

Let's build a simple calculator. It should support the following functions at minimum.

- 0-9 and . (decimal place)
- = (show result)
- \+ \- \* \/ (basic arithmetic)
- CE (clear entry)
- AC (all clear)

Use event listeners to handle interaction:
- When the calculator buttons are pressed
- Enable keyboard input

## Advanced
### Version 2
Show the ongoing operation above the main calculator screen. E.g. if the user enters `5` and then presses `*`, erase the screen and show `5*` above the main screen. If the user then presses `2` and presses `=`, show `5*2=` above the main screen, and `10` in the main screen.

### Version 3
If the user presses an operator after the result is shown, take the result and make it the first operand. E.g. if the user hits `5`, `*`, `2`, `=`, show `10`. If they then press `*` again, `10` would become the first operand, and it would erase the screen for the user to enter the second operand.

If the user presses `=` multiple times, keep applying the operation to the result. E.g. the user enters 5, *, 2, then hits = showing 10. If they hit = again, it'd show 20, and again, it'd show 40.

