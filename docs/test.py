from pygments import highlight
from pygments.formatters import HtmlFormatter
from symbolic_lexer import SymbolicLexer

code = '''
# Example Symbolic code
fn factorial(n) {
    if n <= 1 {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

print(factorial(5));  # Output: 120
'''

formatter = HtmlFormatter()
lexer = SymbolicLexer()

result = highlight(code, lexer, formatter)
print(result)
