from pyscript import when, display
clicks = 0
@when("click", "#my-button")
def handle_click(event):
    display("Button clicked!")
    global clicks
    clicks += 1
    display(clicks, target="clicks", append=False)
    