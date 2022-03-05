A single <code><b>try</b></code> statement can have multiple except 
statements. This is useful when the try block contains 
statements that may throw different types of exceptions.
- You can also provide a generic except clause, which 
handles any exception.
- After the except clause(s), you can include an else-clause. 
The code in the else-block executes if the code in the try: 
block does not raise an exception.
- The else-block is a good place for code that does not 
need the try: block's protection.