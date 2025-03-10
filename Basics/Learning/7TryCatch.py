# Try: Code
# Except: Handle Exception (Not Throw Error (No interrupt))
# If no exception occurs, the except clause is skipped and execution of the try statement is finished.
# If an exception occurs during execution of the try clause, the rest of the clause is skipped
# Raise: Allows the programmer to force a specified exception to occur
# Finally: If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or not the try statement produces an exception

while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError as verr:
        print("Oops! That was not valid "+ str(verr))
    except (RuntimeError, TypeError, NameError):
        pass
    finally:
        print("Hi Finally")

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())
