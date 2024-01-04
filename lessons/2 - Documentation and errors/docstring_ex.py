def say_hello(name: str) -> str:
    """ A simple function to say hello.
    
    Prints the phrase "Hello, {name}!" to stdout / the console and 
    returns the string that was printed.

    Parameters
    ----------
    name : str
        The name of the person or thing to greet.

    Returns
    -------
    greeting : str
        The string that was printed to stdout.

    Examples
    --------
    >>> say_hello("World")
    Hello, World!

    >>> say_hello("Alice")
    Hello, Alice!
    """

    greeting = f"Hello, {name}!"
    print(greeting)

    return greeting


