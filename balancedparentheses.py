"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

    # use a stack
    # if see an opening (, add to stack
    # when encountering a closing ), pop the opening one off the stack
    # if stack is empty then it's balanced

    stack = []

    for char in phrase:
      if char == '(':
        stack.append(char)
      if char == ')':
        try:
          stack.pop()
        except IndexError:
          return False

    return len(stack) == 0


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n"
