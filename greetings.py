def say_hello(name="World"):
  """Prints a greeting message.

  Args:
      name: (Optional) The name to greet. Defaults to "World".
  """
  print(f"Hello, {name}!")

# Example usage (optional, for demonstration within the library)
if __name__ == "__main__":
  say_hello()
  say_hello("Alice")
