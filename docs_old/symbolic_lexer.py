from pygments.lexer import Lexer
from pygments.token import Text, Comment, Keyword, Name, String, Number, Punctuation, Operator, Generic

from symbolic.parsing.lexer import Lexer as SymbolicLexer
from symbolic.parsing.tokens import TokenType, KEYWORDS

class SymbolicLexer(Lexer):
    """
    A Pygments lexer for the Symbolic language.
    """
    name = 'Symbolic'
    aliases = ['symbolic']
    filenames = ['*.sym', '*.symbolic']
    
    TOKEN_MAP = {
        # Keywords
        **{token_type: Keyword for token_type in KEYWORDS.keys()},
        
        # Numbers
        TokenType.NUMBER: Number,
        
        # Strings
        TokenType.STRING: String,
        
        # Comments
        TokenType.COMMENT: Comment,
        
        # Identifiers
        TokenType.IDENTIFIER: Name,
        
        # EOF
        TokenType.EOF: Text,
        
        # Container symbols - Punctuation
        TokenType.LEFT_PAREN: Punctuation,
        TokenType.RIGHT_PAREN: Punctuation,
        TokenType.LEFT_BRACKET: Punctuation,
        TokenType.RIGHT_BRACKET: Punctuation,
        TokenType.LEFT_BRACE: Punctuation,
        TokenType.RIGHT_BRACE: Punctuation,
        
        # Separators - Punctuation
        TokenType.COMMA: Punctuation,
        TokenType.SEMICOLON: Punctuation,
        TokenType.COLON: Punctuation,
        TokenType.DOUBLE_COLON: Punctuation,
        TokenType.FULL_STOP: Punctuation,
        
        # Assignment operators
        TokenType.ASSIGN: Operator,
        TokenType.COLON_EQUAL: Operator,
        TokenType.ARROW_LEFT: Operator,
        TokenType.PLUS_EQUAL: Operator,
        TokenType.MINUS_EQUAL: Operator,
        TokenType.ASTERISK_EQUAL: Operator,
        TokenType.SLASH_EQUAL: Operator,
        TokenType.MODULO_EQUAL: Operator,
        TokenType.CARET_EQUAL: Operator,
        TokenType.LEFT_SHIFT_ASSIGN: Operator,
        TokenType.RIGHT_SHIFT_ASSIGN: Operator,
        
        # Binary operators
        TokenType.PLUS: Operator,
        TokenType.MINUS: Operator,
        TokenType.ASTERISK: Operator,
        TokenType.SLASH: Operator,
        TokenType.DOUBLE_SLASH: Operator,
        TokenType.CARET: Operator,
        TokenType.MODULO: Operator,
        TokenType.PIPE: Operator,
        TokenType.DOUBLE_PIPE: Operator,
        TokenType.LEFT_SHIFT: Operator,
        TokenType.RIGHT_SHIFT: Operator,
        TokenType.NOT_EQUAL: Operator,
        
        # Comparison operators
        TokenType.LESS_THAN: Operator,
        TokenType.GREATER_THAN: Operator,
        TokenType.LESS_THAN_OR_EQUAL: Operator,
        TokenType.GREATER_THAN_OR_EQUAL: Operator,
        TokenType.EQUAL_TO: Operator,
        
        # Special operators
        TokenType.AT: Operator,
        TokenType.BANG: Operator,
        TokenType.TILDE: Operator,
        TokenType.QUESTION: Operator,
        TokenType.ARROW_RIGHT: Operator,
        TokenType.EQUAL_FORWARD: Operator,
        
        # Extended operators
        TokenType.XOR: Operator,
        TokenType.FORWARD_PIPE: Operator,
        TokenType.BACKWARD_PIPE: Operator,
        TokenType.EXCLUSIVE_RANGE: Operator,
        TokenType.NULL_COALESCE: Operator,
        TokenType.SPACESHIP: Operator,
        TokenType.STRICT_EQUAL: Operator,
        
        # Matrix operators
        TokenType.MATRIX_ADD: Operator,
        TokenType.MATRIX_SUB: Operator,
        TokenType.MATRIX_MUL: Operator,
        TokenType.MATRIX_DIV: Operator,
        
        # Set operators
        TokenType.INTERSECTION: Operator,
        TokenType.UNION: Operator,
        TokenType.SUBSET: Operator,
        TokenType.SUBSET_EQ: Operator,
        
        # Other
        TokenType.ELLIPSIS: Punctuation,
        TokenType.DOLLAR_SIGN: Operator,
    }

    def get_tokens_unprocessed(self, text):
        """
        Tokenize the input text using the existing Symbolic lexer.
        """
        try:
            # Use the existing Symbolic lexer with error reporting disabled
            lexer = SymbolicLexer(text, include_comments=True, dont_report_error=True)
            tokens = lexer.lex()
            
            for token in tokens:
                if token.type == TokenType.EOF:
                    continue
                    
                # Map Symbolic token type to Pygments token type
                pygments_token = self.TOKEN_MAP.get(token.type, Text)
                
                # Special handling for different token categories
                if token.type in KEYWORDS:
                    # Highlight control flow keywords more prominently
                    if token.type in ['IF', 'ELSE', 'WHILE', 'FOR', 'RETURN', 'MATCH', 'CASE']:
                        pygments_token = Keyword.Reserved
                    # Highlight type-related keywords
                    elif token.type in ['FN', 'CLASS', 'ENUM', 'EXTENDS', 'IMPORT']:
                        pygments_token = Keyword.Declaration
                    else:
                        pygments_token = Keyword
                
                elif token.type == TokenType.NUMBER:
                    # Add metadata about number type for better highlighting
                    if token.metadata and token.metadata.get('number_type') == 'float':
                        pygments_token = Number.Float
                    elif token.metadata and token.metadata.get('number_type') == 'complex':
                        pygments_token = Number.Complex
                    else:
                        pygments_token = Number.Integer
                
                elif token.type == TokenType.STRING:
                    if token.text.startswith('"""') or token.text.startswith("'''"):
                        pygments_token = String.Doc
                    else:
                        pygments_token = String
                
                elif token.type == TokenType.COMMENT:
                    if token.text.startswith('#'):
                        pygments_token = Comment.Single
                    else:
                        pygments_token = Comment.Multiline
                
                # Yield the token with position information
                yield (token.span[0], pygments_token, token.text)
                
        except Exception as e:
            # Fallback: yield the entire text as plain text if lexing fails
            yield (0, Text, text)
