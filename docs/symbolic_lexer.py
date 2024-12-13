import re

from pygments.lexer import RegexLexer, bygroups
from pygments.token import Text, Comment, Keyword, Name, String, Number, Punctuation, Operator


class SymbolicLexer(RegexLexer):
    """
    A Pygments lexer for the Symbolic language.
    """
    name = 'Symbolic'
    aliases = ['symbolic']
    filenames = ['*.sym', '*.symbolic']

    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Text),

            # Single-line and Multi-line Comments
            (r'#.*$', Comment.Single),
            (r'/\*', Comment.Multiline, 'multiline-comment'),

            # Keywords (sorted by length in descending order)
            (r'\b(try|static|const|finally|case|context|with|wait|loop|return|terminate|whenever|context|function|assert|extends|catch|default|import|match|skip|in|class|enum|fn|stop|to|from|and|or|if|else|while|id|as|false|true)\b', Keyword),

            # Symbols (sorted by length in descending order)
            (r'(>>=|<<=|\+\+|--|!=|==|:=|->|<=|>=|&&|\|\||\^=|\*=|/=|%=|\-=|\+=|<<|>>|\+|-|\*|/|%|\^|&|\||~|!|=|<|>|\[|\]|\{|\}|\(|\)|,|;|:|\.|\?|\@|°|\')', Operator),

            # Numbers: Integers, Floats (with e/E), Octal, Binary, Hexadecimal with underscore separators
            (r'(?<![a-zA-Z_])\b(?:\d{,3}(?:_?\d{3})+|\d+)', Number.Integer),  # Integer (with optional separators)
            ('(?<![a-zA-Z_])(?:(?:\\d{,3}(?:_\\d{3})+|\\d{,3}(?: \\d{3})+|\\d+)(?<![\\.])(?:\\.\\d+(?:[eE][\\-\\+]?\\d+)?)|(?:\\d{,3}(?:_\\d{3})+|\\d{,3}(?: \\d{3})+|\\d+)(?<![\\.])(?:(?:\\.\\d+)?[eE][\\-\\+]?\\d+)', Number.Float),  # Float with optional exponent and underscores
            (r'(?<![a-zA-Z_])0[oO][0-7]+(?![a-zA-Z_])', Number.Oct),            # Octal (e.g., 0o755, 0o7_55)
            (r'(?<![a-zA-Z_])0[bB][01]+(?![a-zA-Z_])', Number.Bin),             # Binary (e.g., 0b1010, 0b1_010)
            (r'(?<![a-zA-Z_])0[xX][0-9a-fA-F]+(?![a-zA-Z_])', Number.Hex),      # Hexadecimal (e.g., 0x1F4, 0x_FF_FF)
            
            # Ordinal Numerals
            (r'(?<![a-zA-Z\d])\b(?:\d{,3}(?:_?\d{3})+|\d+)(?P<ordinal>nd|rd|st|th)\b(?![a-zA-Z\d])', Number),

            # Strings
            (r'"(\\.|[^"\\])*"', String.Double),  # Double quoted string
            (r"'(\\.|[^'\\])*'", String.Single),  # Single quoted string

            # Triple-quoted Strings (Single and Double)
            (r'"""(\\.|[^"\\])*"""', String.Double),  # Triple double quoted string
            (r"'''(\\.|[^'\\])*'''", String.Single),  # Triple single quoted string

            # Containers
            (r'\[', Punctuation, 'list-container'),
            (r'\{', Punctuation, 'map-container'),

            # Identifiers
            (r'[a-zA-Z_][a-zA-Z0-9_]*', Name),

            # Assignment Operator `=`
            #(r'=', Operator),  # Explicitly handle `=`
        ],

        # Multi-line Comment
        'multiline-comment': [
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[^*]+', Comment.Multiline),
            (r'\*', Comment.Multiline),
        ],

        # List Container
        'list-container': [
            (r'\]', Punctuation, '#pop'),
            (r'[^]]+', Text),
        ],

        # Map Container
        'map-container': [
            (r'\}', Punctuation, '#pop'),
            (r':', Punctuation),
            (r'[^}]+', Text),
        ],
    }
